from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Literal
from openai import OpenAI
# Warning control
import warnings
import os

warnings.filterwarnings('ignore')

api_key = os.getenv("AI_CREDIT_KEY")
base_url = os.getenv("AI_CREDIT_URL")
# Instantiate the client
client = OpenAI(api_key=api_key, base_url=base_url)

class Mention(BaseModel):
    # The model chooses the product the mention is about,
    # as well as the social media post's sentiment
    product: Literal['app', 'website', 'not_applicable']
    sentiment: Literal['positive', 'negative', 'neutral']

    # Model can choose to respond to the user
    needs_response: bool
    response: Optional[str]

    # If a support ticket needs to be opened, 
    # the model can write a description for the
    # developers
    support_ticket_description: Optional[str]

# Example mentions
mentions = [
    # About the app
    "@techcorp your app is amazing! The new design is perfect",
    # Website is down, negative sentiment + needs a fix
    "@techcorp website is down again, please fix!",
    # Nothing to respond to
    "hey @techcorp you're so evil"
]

def analyze_mention(
    mention: str, 
    personality: str = "friendly"
) -> Mention:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"""
                Extract structured information from 
                social media mentions about our products.

                Provide
                - The product mentioned (website, app, not applicable)
                - The mention sentiment (positive, negative, neutral)
                - Whether to respond (true/false). Don't respond to 
                  inflammatory messages or bait.
                - A customized response to send to the user if we need 
                  to respond.
                - An optional support ticket description to create.

                Your personality is {personality}.
            """},
            {"role": "user", "content": mention},
        ],
        response_format=Mention,
    )
    return completion.choices[0].message.parsed

print("User post:", mentions[0])
processed_mention = analyze_mention(mentions[0])
print("Processed mention:", processed_mention)

rude_mention = analyze_mention(mentions[0], personality="rude")
print("Rude mention response:", rude_mention.response)

mention_json_string = processed_mention.model_dump_json(indent=2)
print(mention_json_string)