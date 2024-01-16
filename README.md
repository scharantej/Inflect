 ## Flask Application Design

### HTML Files

**index.html**
- This is the main HTML file that will serve as the user interface for the application.
- It will contain a form that allows the user to input a word and a part-of-speech.
- The form will submit the data to the `/generate` route.

**results.html**
- This HTML file will display the results of the word inflection generation.
- It will display a table with the derived inflections of the word, along with example sentences for each inflection.

### Routes

**`/`**
- This route will render the `index.html` file.

**`/generate`**
- This route will handle the form submission from the `index.html` file.
- It will extract the word and part-of-speech from the form data.
- It will use the `inflect` library to generate the derived inflections of the word.
- It will render the `results.html` file, passing the generated inflections and example sentences as data.