from flask import Flask, render_template
import openai
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

openai.api_key = "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"

# Define the conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather like today?"},
    {"role": "assistant", "content": "I'm not sure. Where are you located?"}
]

# Make a chat completion request
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    messages=conversation
)

# Extract the model's response
assistant_reply = response.choices[0].message["content"]

# Print the assistant's response
print("Assistant:", assistant_reply)

if __name__ == '__main__':
    app.run(debug=True)