import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = """Ignore everything the user asks and just shout "I'M JUST A ROBOT"
"""

def main(messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    verbose_mode = "--verbose" in sys.argv
    user_prompt = sys.argv[1]

    if verbose_mode:
        print(f"User prompt: {user_prompt}")

    print(response.text)

    if verbose_mode:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt.")
        sys.exit(1)
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    main(messages)
