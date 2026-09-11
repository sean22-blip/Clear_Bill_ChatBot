from uagents import Agent, Context, Protocol
from ..messages.requests import RagRequest
from ai_engine import UAgentResponse
from uagents.setup import fund_agent_if_low

QESTION= "How to install agent using pip"
URL = "https://web.archive.org/web/20250127103829/https://fetch.ai/docs/guides/agents/installing-uagent"
DEEP_READ = (
    "no" # this mean the agent should only read the main page
)

RAG_AGENT_ADDRESS= "YOUR_LANGCHAIN_RAG_AGENT_ADDRESS" # this is where it retreives and process the user quesiton
user= Agent(
    name="langchain_rag_user",
    port=8000,
    endpoint=["https://web.archive.org/web/20250127103829/http://127.0.0.1:8000/submit"],
)
fund_agent_if_low(user.wallet.address())
rag_user = Protocol("Langchain RAG user")

@rag_user.on_interval(60, messages=RagRequest)
async def ask_question(ctx: Context):
    ctx.logger.info(f"Ask RAG agent to answer {QESTION} based on the document located at {URL}, reading nested pages too: {DEEP_READ}")
    await ctx.send(
        RAG_AGENT_ADDRESS, RagRequest(question=QESTION, url=URL, deep_read=DEEP_READ)
    )
@rag_user.on_message(model=UAgentResponse)
async def handle_data(ctx: Context, sender: str, data: UAgentResponse):
    ctx.logger.info(f"Got response from RAG agent: {data.message}")

user.include(rag_user, publish_manifest=True)

if __name__ == "__main__":
    user.run();

#Note
# Remember to provide the QUESTION, URL, DEEP_READ, RAG_AGENT_ADDRESS, name, seed and endpoint parameters to correctly run this code.