
# Azure for MCP: Registry & AI Gateway

This repository provides resources and guidance on leveraging Azure API Center as your enterprise MCP registry and Azure API Management as your AI Gateway for secure and governed remote MCP servers.

## 1. Azure API Center: Your Enterprise MCP Registry

Azure API Center empowers organizations to build their own centralized registry for Model Context Protocol (MCP) servers. This means your teams can easily discover, share, and reuse MCP servers across the entire organization. This registry isn't limited to internally-developed MCP servers; you can also register publicly available MCP servers, providing a single, comprehensive source of truth for all MCP servers relevant to your organization.

By establishing a private MCP registry, you can:
* **Centralize Discovery:** Provide a single source of truth for remote MCP servers, whether internally built or publicly available.
* **Promote Reuse:** Encourage developers to leverage existing MCP servers, accelerating development.
* **Enhance Governance:** With an AI gateway as a proxy, you can apply organizational standards and policies to your MCP server ecosystem.

## 2. MCP Discovery Page in Azure (Official Partners)

Azure API Center is featuring a MCP discovery page within the Azure portal. This page will showcase remote MCP servers from approved, official partners who have successfully completed our verification process.

Becoming an official partner and being featured on the Azure MCP discovery page offers significant advantages:
 * **Expanded Reach & Discoverability:** Your MCP servers will be prominently displayed within the Azure portal, making them easily discoverable by a vast audience of Azure customers and AI developers. 
 * **Seamless Integration with MCP Hosts:** Every newly created API Center registry will automatically have access to these official partner MCP servers. This allows customers to effortlessly expose your remote MCP servers to popular MCP hosts like **VS Code, Copilot Studio, and Azure AI Foundry (coming soon)**, facilitating rapid integration and adoption of your solutions within their AI workflows. 
 * **Increased Adoption:** By simplifying the discovery and connection process, you'll drive greater adoption of your MCP servers among organizations leveraging Azure's AI capabilities. 

**Interested in becoming an official partner and featured on the Azure MCP discovery page?** 
We are actively looking for partners to expand Azure's remote MCP server ecosystem. If you're interested in connecting with our business team to explore becoming an officially featured partner, please feel free to create a Pull Request (PR) in this repository. We will review your PR and get in contact with you to discuss the approval process.

## 3. Azure AI Gateway (Azure API Management) with MCP Support

Azure API Management serves as your robust AI Gateway, providing comprehensive support for Model Context Protocol (MCP) servers. It's a critical component for managing and securing your remote MCP server deployments.

### Why API Management is Crucial for Remote MCP Servers

Remote MCP servers, by their nature, are exposed to the internet, making robust governance and security very critical. Azure API Management provides essential capabilities to ensure consistency and control across these distributed systems:

* **Centralized Security:** Enforce authentication, authorization, and threat protection for all incoming requests to your MCP servers, safeguarding your valuable AI assets.
* **Traffic Management:** Efficiently handle high volumes of requests from numerous AI agents, implementing rate limiting to prevent abuse and caching to improve performance and reduce load on your backend.
* **Monitoring and Analytics:** Gain deep insights into how your AI agents are interacting with the MCP servers and their underlying API tools, enabling performance optimization and usage analysis.

### Capabilities of Azure API Management and MCP

Azure API Management extends its powerful features to the MCP landscape, enabling:

#### Expose Existing APIs as MCP Servers

Seamlessly expose any APIM-managed REST API as a remote MCP server, supporting both Server-Sent Events (SSE) and Streamable HTTP.

* [✅ Documentation](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
* [✅ Blog Post](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)

#### Enhancing Security for Remote MCP Servers

Utilize Azure API Management as your primary authentication gateway for remote MCP servers, ensuring secure access and robust control.

**Protect your remote MCP servers with OAuth:**
* [✅ Blog Post](https://devblogs.microsoft.com/blog/preventing-confused-deputy-attacks-in-mcp-with-azure-api-management/)
* [✅ APIM lab – Client Auth](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
* [✅ Python – azd up](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
* [✅ .NET – azd up](https://github.com/Azure-Samples/remote-mcp-apim-functions-csharp) (Assuming .NET sample exists or will exist)
* [✅ On-Behalf-Of Auth](https://learn.microsoft.com/en-us/azure/api-management/oauth2-client-credentials-onbehalfof) (General APIM OAuth, can be adapted)
* [✅ Detailed flow chart](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/docs/media/sequence-diagram.png)

**Use credential manager to authorize access to your backend MCP servers:**
* [✅ Blog Post](https://learn.microsoft.com/en-us/azure/api-management/credentials-overview)
* [✅ APIM lab](https://learn.microsoft.com/en-us/azure/api-management/credentials-overview) (Refers to general credential manager overview, specific lab might be needed)
* [✅ YouTube Demo](https://www.youtube.com/watch?v=kY6g_6oE5jI)
