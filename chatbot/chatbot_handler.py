import openai

def get_ai_response(user_query):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Answer this customer query: {user_query}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print(get_ai_response("How can I reset my password?"))