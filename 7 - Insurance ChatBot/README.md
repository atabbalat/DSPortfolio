# Insurance Chatbot

This project is an implementation of an insurance chatbot using a deep learning model. The chatbot utilizes Natural Language Processing (NLP) to understand user inputs and provide appropriate responses. It is trained using a JSON file with data relevant to the insurance domain.

## Prerequisites

Ensure you have installed the following Python packages:

- Flask
- Flask-SocketIO
- Tensorflow
- sklearn
- json
- numpy

You'll also need:

- HTML/CSS for the chat interface
- JSON for data storage

## Project Structure

The project is composed of Python scripts, an HTML file, a CSS file, and a JSON data file. It includes the following sections:

1. **app.py**: This is the Flask application file, where the chatbot model is loaded and used to provide responses for user input. 
2. **training.py**: This Python script is used for training the chatbot model. 
3. **index.html**: The HTML file for the chatbot interface.
4. **main.css**: The CSS file for styling the chatbot interface.
5. **data.json**: The JSON file storing the intents data for the chatbot.

The full code for each file is provided in the final section of this README. 

## Installation and Usage

1. Install the required Python packages.
2. Clone the repository or download the files.
3. Run `python training.py` to train the chatbot model.
4. Run `python app.py` to start the Flask server.
5. Open a web browser and navigate to the server's address to interact with the chatbot.

## app.py

The Flask application file, where the chatbot model is loaded and used to provide responses for user input.

## training.py

This script trains the chatbot model. It loads the intents data from the JSON file, preprocesses the data, creates the model, trains it, and saves it along with the tokenizer and label encoder.

## index.html

This is the HTML file for the front end of the chatbot interface. It creates a simple chat interface where users can type in their messages, and the bot's responses are displayed.

## main.css

This is the CSS file for styling the chatbot interface. It provides simple styles to make the chat interface look good.

## data.json

The JSON file storing the intents data for the chatbot.


