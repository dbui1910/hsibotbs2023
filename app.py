from flask import Flask, render_template
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

openai.api_key = "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"

@app.route('/chat', methods=['GET'])
def chat():
    # Define the conversation as a list of message dictionaries
    conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"My name is Katie and I am 39 years old."},
            {"role": "user", "content": f"My health concerns are: diebetic"},
            {"role": "user", "content": f"My dietary restrictions are: vegan."},
            {"role": "assistant", "content": "What recipe should I recommend for you today?"}
        ]

    # Make a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract the model's response
    assistant_reply = response['choices'][0]['message']['content']
    print(assistant_reply)

    # Return the assistant's response
    return assistant_reply

if __name__ == '__main__':
    app.run(debug=True)
