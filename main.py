import openai

# Load your API key from an environment variable
openai.api_key = "you api key"

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":

    while True:
        user_input = input("You: ")

        if user_input.lower() in [ 'exit','quit' , 'bye']:
            print("Goodbye!")
            break

        response = chat_with_openai(user_input)
        print("Chatbot:",response)
