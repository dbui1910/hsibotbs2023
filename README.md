# hsibotbs2023
## Project: Hearty Healthy

This project is made in the backend in Python 3.11 and Flask, while the frontend is designed in HTML and CSS
### Built With

***

- Python

- Flask

- HTML5

- CSS
### Installation
Install with pip
```
$ pip install flask
$ pip install openai
```
Install with pip3
```
$ pip3 install flask
$ pip3 install openai
```
### Run the server

```
$ python app.py
$  OR python3 app.py
```
### Expected output and error handling

```
![Alt Text](https://github.com/dbui1910/hsibotbs2023/blob/main/firstpage.png)
```
### Use of libraries
To open a Flask application you need to create a Flask instance with the following lines:
```
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('yourfile.html')
```
To create a conection with CHAT GPT you need to you need to obtain an api key.
Below is an example of how to make a query to CHAT GPT.
```
openai.api_key = "############################################"



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

```

### Backend and frontend structure
- /static
  - forms.css: Styles used in HTML programs
  - g.jpg: Image
- /templates
  - form.html: Main tab when starting the web page
  - generate.html: Generate the recipe with the CHAT GPT API call
- app.py: Main program, generate an aplitacion web

### Reference
- Official Web Sites:
   - [openai](https://platform.openai.com/docs/introduction/overview)
   - [flask](https://flask.palletsprojects.com/en/2.3.x/)
  
