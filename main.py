 
# Import necessary libraries
from flask import Flask, render_template, request
from inflect import engine

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle form submission
@app.route('/generate', methods=['POST'])
def generate():
    # Extract the word and part-of-speech from the form data
    word = request.form['word']
    pos = request.form['pos']

    # Use the inflect library to generate derived inflections
    inflector = engine()
    inflections = inflector.inflect(word, pos)

    # Generate example sentences for each inflection
    examples = []
    for inflection in inflections:
        example = f"Example: {inflection} - The {inflection} of the word '{word}'."
        examples.append(example)

    # Render the results page with the generated inflections and examples
    return render_template('results.html', inflections=inflections, examples=examples)

# Run the app
if __name__ == '__main__':
    app.run()
