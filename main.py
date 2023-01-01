from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

terminal_command_request = input("Generate a bash script ")

response = openai.Completion.create(
    model="code-cushman-001",
    prompt="Generate a bash script " + terminal_command_request+"\n```bash\n#!/bin/bash",
    temperature=0,
    max_tokens=54,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["```"]
)

print(response)
