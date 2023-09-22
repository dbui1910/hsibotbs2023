from flask import Flask, redirect, render_template, request, url_for
import openai
import json
app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def index():
    
    return render_template('form.html')


@app.route('/', methods=['POST'])
def process_form():
    # # Process the form data here
    # first_name = request.form.get('firstName')
    # last_name = request.form.get('lastname')
    # gender = request.form.get('gender')
    # ethnicity= request.form.get('ethnicity')
    # selected_restrictions = request.form.getlist('dietary_restrictions')
    # print(selected_restrictions)
    # print(first_name)
    # print(last_name)
    # Redirect to the "generate.html" page after processing
    return redirect(url_for('generate'))

@app.route('/generate', methods=['GET','POST'])
def generate():
    selected_values = request.form.getlist('dietary_restrictions[]')
    print(selected_values)
    selected_labels = []

    # Map selected values to their corresponding labels
    labels_mapping = {
        "Dairy-free": "Dairy-free",
        "Gluten-free": "Gluten-free",
        "Vegetarian": "Vegetarian",
        "Pescatarian": "Pescatarian",
        "Halal": "Halal",
        "Kosher": "Kosher",
        "Nut allergy": "Nut allergy",
        "Shellfish": "Shellfish"
    }

    for value in selected_values:
        if value in labels_mapping:
            selected_labels.append(labels_mapping[value])

    print(selected_labels)
    # Define the conversation as a list of message dictionaries
    conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I want you get data from people who are facing obesity, diebities, cancer, high cholesterol"},
            {"role": "user", "content": f"They are in their 30-40 years old"},
            {"role": "user", "content": f"My dietary restrictions are: {', '.join(selected_labels)}"},
            {"role": "assistant", "content": "Suggest 3 meal plan for them. ONLY give output of JSON array of mealPlan object which is a list of meal objects including mealID, meal's name, meal's description, recipe's name"}
        ]
    # Make a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract the model's response
    assistant_reply = response['choices'][0]['message']['content']
    # print(assistant_reply)

    # Assuming 'assistant_reply' contains the JSON string
    response_json = json.loads(assistant_reply)

    # Check if the response contains a "mealPlan" key
    if "mealPlan" in response_json:
        # Access the list of meal objects
        meal_plan = response_json["mealPlan"]

        # Iterate through each meal object in the list
        for meal_info in meal_plan:
            # Access properties of the meal object
            meal_id = meal_info.get("mealId")
            meal_name = meal_info.get("mealName")
            meal_description = meal_info.get("mealDescription")
            recipe_name = meal_info.get("recipeName")
    else:
        print("Response does not contain a 'mealPlan' key.")
    print(meal_plan)

    # Return the assistant's response
    return render_template('generate.html')


if __name__ == '__main__':
    app.run(debug=True)
