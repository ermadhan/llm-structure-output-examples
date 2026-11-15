# Warning control
import warnings
import os
# The user class from the slides
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional

warnings.filterwarnings('ignore')

api_key = os.getenv("AI_CREDIT_KEY")
base_url = os.getenv("AI_CREDIT_URL")
# Instantiate the client
client = OpenAI(api_key=api_key, base_url=base_url)

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Make up a user."},
    ],
    response_format=User,
)

print(completion)
user = completion.choices[0].message.parsed
print(user)