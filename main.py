from openai import OpenAI
from dotenv import load_dotenv
from mem0 import Memory
import os
import json
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "1.0",
    "embedder": {
        "type": "openai",
        "config": {
            "model": "text-embedding-3-small",
            "api_key": OPENAI_API_KEY
                    }
                },
    "llm": {
         "provider": "openai",
         "config":{
            "model": "gpt-4o-mini",
            "api_key": OPENAI_API_KEY
         }
    },
    "vector_store": {
       "provider": "qdrant",
       "config": {
           "url": "https://2c2ac114-a259-42c6-ade7-bb35cb0ac092.us-east4-0.gcp.cloud.qdrant.io:6333",
           "api_key": os.getenv("QDRANT_API_KEY")
       }
    }
}

mem_client=  Memory.from_config(config)
client = OpenAI()

def chat():
    print("Welcome to the chat! Type 'ctr+c' to quit.")
    while True:
        user_input = input("input: ")

        relevent_memory = mem_client.search(query=user_input, user_id="gaurav")
        
        memories = [
            f"ID: {mem.get('id')}, Memory: {mem.get('memory')}" 
            for mem in relevent_memory.get("results", [])
        ]

        # print("memories:", memories)
        
        SYSTEM_PROMPT = f""" 
            You are a memory aware assistant which responds to user with context.
            You are given relevant memories from the past interactions about the user.
            
            Memory of user:
           {json.dumps(memories)}

        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}],
        )
        print("Bot:", response.choices[0].message.content)

        mem_client.add([
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": response.choices[0].message.content }
        ],user_id="gaurav")

chat()