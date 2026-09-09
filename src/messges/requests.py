from typing import Optional
from uagents import Model, Field

class RagRequest(Model):
    question: str = Field(
        description="The question that the user wants to have an answer for."#url of question that user asked
    )
    url: str = Field(description="The url of the docs where the answer is.") #url of where the answer is going to be found
    deep_read: Optional[str] = Field(
        description="Specifies weather all nested pages referenced from the starting URL should be read or not. The value should be yes or no.",
        default="no",
    )# if no the agent would only focus on the page linked to the url if yes the agent is able to go to another page linking from that url