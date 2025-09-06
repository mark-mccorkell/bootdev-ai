import os
from dotenv import load_dotenv
from google import genai

def main():
    # Get the Gemini API key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create a new instance of a Gemini client
    client = genai.Client(api_key=api_key)

    # Get a response from Gemini using a hard-coded model and prompt
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    )

    # Print the response

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
