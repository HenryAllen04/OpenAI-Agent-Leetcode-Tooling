from openai import OpenAI
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

# Define my leetcode tools or Tool (tools is a list)

tools = [
    {
        "type": "function",
        "name": "binarySearch"
        "description": "Perform a binary search on a array, when we know the target."
        "parameters": {
            "type": "object",
            "properties": {
                ""
            }
        }
    }
]