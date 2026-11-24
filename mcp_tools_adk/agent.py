import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams,
    StreamableHTTPConnectionParams,
)
from mcp import StdioServerParameters

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(exist_ok=True)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for MCP tools questions.',
    instruction='Answer user questions to the best of your knowledge by using MCP filesystem and MCP github',
    tools = [
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args = ["-y","@modelcontextprotocol/server-filesystem",str(folder)],
                )
            )
        ),

        #Github MCP tool
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
            url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {github_token}",
                    "X-MCP-Toolsets": "all",
                }
            )
        )
    ]
)
     