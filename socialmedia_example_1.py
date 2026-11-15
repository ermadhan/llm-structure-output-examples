from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Literal
from openai import OpenAI
# Warning control
import warnings
import os

from socialmedia_example import analyze_mention

warnings.filterwarnings('ignore')

api_key = os.getenv("AI_CREDIT_KEY")
base_url = os.getenv("AI_CREDIT_URL")
# Instantiate the client
client = OpenAI(api_key=api_key, base_url=base_url)

class UserPost(BaseModel):
    message: str

def make_post(output_class):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
                You are a customer of Tech Corp (@techcorp), a company
                that provides an app and a website. Create a small 
                microblog-style post to them that sends some kind of 
                feedback, positive or negative.
            """},
            {"role": "user", "content": "Please write a post."},
        ],
        response_format=output_class,
    )
    return completion.choices[0].message.parsed

print("--------------------------------------------------")
new_post = make_post(UserPost)
print("New post:", new_post)

print("--------------------------------------------------")
processed_mention = analyze_mention(new_post.message)
print("Processed mention:", processed_mention)

class UserPostWithExtras(BaseModel):
    user_mood: Literal["awful", "bad", "evil"]
    product: Literal['app', 'website', 'not_applicable']
    sentiment: Literal['positive', 'negative', 'neutral']
    internal_monologue: List[str]
    message: str

print("--------------------------------------------------")
new_post = make_post(UserPostWithExtras)
print("New post with extras:", new_post)
print("--------------------------------------------------")
processed_mention_with_extras = analyze_mention(new_post.message)
print("Processed mention with extras:", processed_mention_with_extras)

from helper import print_mention
print("--------------------------------------------------")
print("Processing example mentions:")
# Example mentions
mentions = [
    # About the app
    "@techcorp your app is amazing! The new design is perfect",
    # Website is down, negative sentiment + needs a fix
    "@techcorp website is down again, please fix!",
    # Nothing to respond to
    "hey @techcorp you're so evil"
]

# Loop through posts that tagged us and store the results in a list
rows = []
for mention in mentions:
    # Call the LLM to get a Mention object we can program with
    processed_mention = analyze_mention(mention)

    # Print out some information
    print_mention(processed_mention, mention)
    
    # Convert our processed data to a dictionary
    # using Pydantic tools
    processed_dict = processed_mention.model_dump()
    
    # Store the original message in the dataframe row
    processed_dict['mention'] = mention
    rows.append(processed_dict)
    
    print("") # Add separator to make it easier to read

import pandas as pd

df = pd.DataFrame(rows)
print(df)