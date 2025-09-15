import os
import sys
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: Set your OpenAI API key in the OPENAI_API_KEY environment variable.")
        return

    if len(sys.argv) < 2:
        print("Usage: python chatgpt_ask.py [your question]")
        return

    question = " ".join(sys.argv[1:])
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=512,
            temperature=0.7
        )
        print(response.choices[0].message["content"].strip())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()