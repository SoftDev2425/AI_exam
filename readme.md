# AI Exam project: PyHousr

![image](https://github.com/SoftDev2425/AI_exam/assets/90389865/d5ca55f3-eb15-42bf-a809-8ce1382bbb6b)



the Readme document includes problem statement, motivation, theoretical foundation, argumentation of
choices, design, code, artefacts, outcomes, and implementation instructions, as appropriate.

## Table of content

- [Table of content](#table-of-content)
- [About](#about)
  - [Problem Statement](#problem-statement)
  - [Motivation](#motivation)
  - [Theoretical Foundation](#theoretical-foundation)
  - [Argumentation of Choices](#argumentation-of-choices)
  - [Design](#design)
  - [Code](#code)
  - [Artefacts](#artefacts)
  - [Outcomes](#outcomes)
- [Extend project](#Extend-project)
- [Setup project instructions](#Setup-project-instructions)
- [Status](#status)


## About
This project was developed by Andreas, Owais and Rasmus from CPH-business academy.
Its use is for the AI course exam project 2024.
The project is a house price predictor with a GUI that can generate a report about the house's details.

### Data Wrangling / Preparation
- Scraping House Data and ensuring the data includes relevant features.
- Data Cleaning, handling missing values, outliers, and any inconsistencies in the dataset.
- Feature Engineering, creating new features if necessary (e.g., price per square meter).

### Building the Machine Learning Model
- Spliting the data into training and testing sets.
- Choosing a suitable supervised learning algorithm (e.g., Linear Regression, Decision Tree, Random Forest, etc.).
- Training our model using the training dataset.
- Evaluating our model using the testing dataset and fine-tune hyperparameters if necessary.

### Creating the GUI with Custom-Tkinter
- Input Form: Creating fields for the user to input house features.
- Predict Button: Implementing a button that, when clicked, will use the trained model to predict the house price.
- Output Display: Show the predicted price on the GUI

### Generative AI for House Report
- Using a generative AI model to create a house report based on the features and predicted price.
- Convert the generated HTML report format to PDF.
- Providing a button to download the generated PDF report.

### Problem Statement
Accurate house price predictions are essential for the real estate market.
We want to develop an AI model to predict house prices and a generative AI to assist real estate agents in document creation for the houses.
We hope to answer these research questions:
1. Can AI models predict house prices accurately using features such as zip code, the house type, size, number of rooms, and proximity to amenities?
2. Can a generative AI trained on real estate data create useful documents for real estate agents?

Our hypotheses is AI models can achieve high accuracy in predicting house prices based on relevant features. A generative AI can effectively produce structured documents for real estate agents using data from house sales websites.

### Motivation
The real estate market is complex and influenced by numerous factors. If AI can predict the price for a house from these factors, it would be ideal, to implement it to this business area. Reducing workload for real estate agents.

### Theoretical Foundation

### Argumentation of Choices

### Design
The project is divided up in directories.
Scraping directory has files with methods which can gather data from dingeo.dk, a website with houses for sale.
Data directory stores the data webscraped from dingeo.dk, and also holds the vector database.
Notebooks directory is where we do our data wrangling, with the data stored in data directory, to train various models and pick the best one.
Models directory stores the best performing model based on its R-score.
GenAI directory trains the generative AI. We load data from websites revolving real estate, split it into chunks and save them in the vector database in data directory.
GUI directory has one file, the GUI which uses the best model and generative AI. This is also the file to start project.

### Code

### Artefacts

### Outcomes
The best trained model became Gradient Boosting based on the R-score of 73. 
When predicting house prices, the result is not 100% accurate if compared to the origin source from the webscraped site, but it is fairly close.
The generative AI can take the input and predicted price result from our GUI and generate a text, which gets saved as a PDF file.

## Extend Project


## Setup project instructions
1. Clone repository.
2. Have Ollama running. Type ollama serve in a terminal if it is not already running.
3. Run UI.py file in the terminal to start GUI. Path to the file is AI_Exam/GUI/UI.py

## Status
After starting the GUI, a user can input information about a house. From the information a price is predicted thanks to chosen model trained for this task. 
If Ollama is running, the AI will generate a text in the format of a document describing the house with its features. The text then gets saved as a PDF file, which the real estate agents can use.

For future improvements we could try to train one of our models to achieve a better score than that of the best one we currently have. A challenge has been to determine, how many features are needed to predict a house price. The current chosen features are all taken from the same website, which uses the features to describe each house. However, we think a house value are also determined by its distance to the ocean, which the website did not show. 
In the end the house price predict does predict a price, but it is not 100% accurate to the origin source.
