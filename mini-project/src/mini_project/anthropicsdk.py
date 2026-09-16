import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  

client =  Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=512,
    system="You are a helpful assistant that translates English to French.",
    content=[
        {
            "type": "text",
            "text": "Translate the following English text to French: 'Hello, how are you?'"
        }
    ]
)
    
for block in message.content:
    if block.type == "text":
        print(block.text)