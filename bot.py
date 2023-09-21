import openai

# Set your OpenAI API key
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
