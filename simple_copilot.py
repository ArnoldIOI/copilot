import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_code_suggestion(context):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Provide concise code suggestions based on the given context."},
                {"role": "user", "content": f"Suggest the next line or block of code for this context:\n\n{context}"}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def ai_copilot():
    print("Welcome to AI-powered Copilot!")
    print("Start typing your Python code. Type 'exit' to quit.")

    context = []
    while True:
        try:
            current_line = input(">>> ")
            if current_line.lower() == 'exit':
                break

            context.append(current_line)
            suggestion = get_code_suggestion("\n".join(context))
            print(f"Suggestion:\n{suggestion}")

            use_suggestion = input("Use this suggestion? (y/n): ").lower()
            if use_suggestion == 'y':
                context.append(suggestion)
                print("Suggestion added to context.")

            # Keep context to last 10 lines to manage token limit
            context = context[-10:]
        except KeyboardInterrupt:
            break

    print("Thank you for using AI-powered Copilot!")

if __name__ == "__main__":
    ai_copilot()
