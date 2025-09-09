import os
import sys
from dotenv import load_dotenv
from google import genai

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
    user_prompt = " ".join(args)


    # Fetch API key from .env
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create a new instance of a Gemini client
    client = genai.Client(api_key=api_key)

    # Get a response from Gemini using a hard-coded model and prompt
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=user_prompt,
    )

    # Print the response

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
