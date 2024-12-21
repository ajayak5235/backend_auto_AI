import openai
def analyze_diff_with_openai(diff):
    import os
    # Set the API key
    openai.api_key =os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("API key not found. Set the 'OPENAI_API_KEY' environment variable.")
    
    try:
        # Call the ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Analyze this code diff for issues and improvements."},
                {"role": "user", "content": diff},
            ],
        )
        print("response_ai", response)
        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        raise

