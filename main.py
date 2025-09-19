import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    # Load environment from .env
    load_dotenv()

    # Check for prompt in CLI args
    args = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    # Fetch API key from .env
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create a new instance of a Gemini client
    client = genai.Client(api_key=api_key)

    # Combine all arguments into a single user prompt
    user_prompt = " ".join(args)

    # Create a list of messages for future use in conversations
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages)


# Print out a response from Gemini passing in conversation history in 'messages'
def generate_content(client, messages):

    # Get a response from Gemini using a hard-coded model and user prompt
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )

    # Print the response

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
