# 🚀 Azure API Management 💜 MCP

The **Model Context Protocol (MCP)** is an open standard designed to standardize how AI applications (specifically Large Language Models or LLMs, often referred to as "agents") interact with external tools and data.

## Understanding Remote MCP Servers

- Traditionally, most MCP servers run locally (e.g., on a user's laptop).
- Remote MCP servers, however, are hosted on cloud platforms or other internet-accessible environments. They allow AI agents to connect to tools and data sources over the internet, enabling more powerful and complex AI applications.
- These servers essentially expose specific capabilities and provide context, tools, and prompts to AI clients. They can connect to various services, databases, and third-party APIs.

## The Relationship between MCP servers and APIs

The relationship between MCP servers and APIs is a hierarchical and complementary one. It's not a case of one replacing the other; rather, MCP servers often use APIs to achieve their purpose, and APIs provide the underlying functionality that MCP servers expose to AI agents.

💡APIs are the Backend, Remote MCP Servers are the AI-Friendly Frontend💡

- APIs are the fundamental building blocks of almost all digital services. They define how different software components communicate and interact. For example, a weather service might expose an API to get forecasts, a CRM system has an API to manage customer data, and a payment gateway has an API to process transactions. These APIs are designed for programmatic consumption by developers and applications.
- Remote MCP Servers (built on JSON-RPC 2.0) act as an abstraction layer on top of these underlying APIs (and other data sources like databases or file systems). Their primary purpose is to expose the capabilities of these backend systems to AI agents (like Large Language Models or AI assistants) in a standardized, "AI-native" way, using the MCP.

Remote MCP Servers Leverage APIs: "Tools" are often API calls: When an MCP server exposes a "tool" (a callable function for an AI agent), that tool's internal implementation very frequently involves making calls to one or more traditional APIs.

## Why API Management is Crucial for Remote MCP Servers

Because remote MCP servers are exposed to the internet, they greatly benefit from API Management solutions. This allows teams to apply well-established governance and security practices, ensuring consistency and control across distributed systems. API Management provides crucial features for these remote connections:
- **Centralized Security**: Enforcing authentication, authorization, and threat protection for all incoming requests to the MCP server.
- **Traffic Management**: Handling high volumes of requests from many AI agents, rate limiting, and caching.
- **Monitoring and Analytics**: Gaining insights into how AI agents are using the MCP server and its underlying API tools.
- **Discovery and Governance**: Making remote MCP servers discoverable for AI developers and maintaining consistency across multiple MCP server deployments.

## Capabilities of API Management and MCP

### Expose Existing APIs as MCP Servers
Expose any APIM-managed REST API as a remote MCP server (SSE & Streamable HTTP)

1️⃣**Currently APIM instance must be on a SKUv1 tier**: Premium, Standard, or Basic
2️⃣**Your service must be enrolled in the [AI Gateway release channel](https://aka.ms/apimdocs/updategroups)** (activation may take up to 2 hours)
3️⃣**Use the Azure Portal with feature flag**: ➤ Append `?Microsoft_Azure_ApiManagement=mcp` to your portal URL to access the MCP server configuration experience

> **Note:** We are working on getting this out to SKUv2 tier as well.

🔗 Useful Links:
✅[Documentation](https://aka.ms/apimdocs/exportmcp)
✅[Blog Post](https://aka.ms/build25-apim-mcp)


### Enhancing Security for remote MCP Servers
API Management as your Auth Gateway for remote MCP Servers

Protect your remote MCP servers with OAuth:
- ✅[Blog Post](https://aka.ms/remote-mcp-apim-auth-blog)
- ✅[APIM lab – Client Auth](https://aka.ms/ai-gateway-lab-mcp-client-auth)
- ✅[Python – azd up](https://aka.ms/mcp-remote-apim-auth)
- ✅[.NET – azd up](https://aka.ms/mcp-remote-apim-auth-dotnet)
- ✅[On-Behalf-Of Auth](https://aka.ms/mcp-obo-sample)
- ✅[Detailed flow chart](https://aka.ms/mcp-remote-apim-auth-diagram)


Use credential manager to authorize access to your backend MCP servers:
- ✅[Blog Post](https://aka.ms/remote-mcp-apim-lab-blog)
- ✅[APIM lab](https://aka.ms/ai-gateway-lab-mcp)
- ✅[YouTube Demo](https://aka.ms/ai-gateway-lab-demo)


### Private MCP Registry for Organizations
Enable MCP Discovery and Consumption across the Enterprise:

✅[APIC lab](https://aka.ms/apic-lab)

## What's Next

- MCP support in SKUv2 tiers
- MCP passthrough capabilities

  ## 🤝 How to Contribute

We love contributions! Here's how you can help make APIM and MCPs even better:

1. Create an issue or feature request

---

💻 Made with ❤️ by the API Management Team
