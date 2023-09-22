# hsibotbs2023
## Project: Hearty Healthy

Hearty Healthy is a web application that is in the processing of developing. We succesfully developed and designed an API that can integrate with chatGPT api using GPT3.5 model. In this folder, we added a screenshot of our expected output and some error handlings
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
### Figma (Web app mock up)
Due to our time constraint, we were not able to develop all the functionalities and features of the app. Here is the lonk of our UI/UX design of Hearty Healthy.
https://www.figma.com/file/GXdIOU0ikDRYFat6XZ7rI0/Hearty-Healthy?type=design&node-id=0%3A1&mode=design&t=eYaYop8juvUjOZtg-1

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
    {"role": "user", "content": f"I want you to provide me with meal plans for people facing obesity, diabetes, cancer, or high cholesterol."},
    {"role": "user", "content": f"These individuals are in their 30-40 years old."},
    {"role": "user", "content": f"My dietary restrictions are: {', '.join(selected_labels)}"},
    {"role": "assistant", "content": 'Generate a JSON response with the following structure as an example:\n' +
                                       '{"mealPlan": [' +
                                       '{"mealID": "1", "mealName": "", "mealDescription": "", "recipeName": ""},' +
                                       '{"mealID": "2", "mealName": "", "mealDescription": "", "recipeName": ""},' +
                                       '{"mealID": "3", "mealName": "", "mealDescription": "", "recipeName": ""}' +
                                       ']}'
    }

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
  
