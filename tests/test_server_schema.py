import json
import unittest
from pathlib import Path

from jsonschema import ValidationError
from jsonschema.validators import validator_for


class ServerSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema_path = Path(__file__).resolve().parents[1] / "partners" / "server-schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator_class = validator_for(schema)
        validator_class.check_schema(schema)
        cls.validator = validator_class(schema)

    def setUp(self):
        self.server = {
            "name": "client-credentials-test",
            "title": "Client credentials test",
            "summary": "An MCP server supporting client credentials.",
            "description": "An MCP server used to validate partner submissions.",
            "kind": "mcp",
            "license": {"name": "MIT", "url": "https://example.com/license"},
            "icon": "https://example.com/icon.svg",
            "externalDocumentation": {
                "title": "Server documentation",
                "url": "https://example.com/docs",
            },
            "useCases": [],
            "vendor": "Partner",
            "categories": "Developer Tools",
            "versionName": "original",
            "supportContactInfo": {
                "name": "Support",
                "url": "https://example.com/support",
            },
            "customProperties": {"x-ms-preview": False},
            "remote": "https://example.com/mcp",
            "authSchemas": ["ClientCredential"],
            "securitySchemes": {
                "exampleClientCredentials": {
                    "type": "oauth2",
                    "description": "Authenticate using the OAuth 2.0 client credentials flow.",
                    "flows": ["clientCredentials"],
                    "tokenUrl": "https://example.com/oauth2/token",
                    "scopes": ["read"],
                }
            },
        }

    def test_accepts_client_credential_submission(self):
        self.validator.validate(self.server)

    def test_accepts_client_credential_with_existing_auth_schemas(self):
        self.server["authSchemas"].extend(
            ["OAuth2", "UserEntraToken", "AgentOnBehalfOfUser", "ManagedIdentity", "AgentIdentity"]
        )
        self.validator.validate(self.server)

    def test_rejects_invalid_auth_schemas(self):
        for auth_schema in ["clientcredential", "clientCredentials", "UnknownAuth"]:
            with self.subTest(auth_schema=auth_schema):
                self.server["authSchemas"] = [auth_schema]
                with self.assertRaises(ValidationError):
                    self.validator.validate(self.server)


if __name__ == "__main__":
    unittest.main()
