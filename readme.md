# AI Exam project: PyHousr

![image](https://github.com/SoftDev2425/AI_exam/assets/90389865/d5ca55f3-eb15-42bf-a809-8ce1382bbb6b)


House Price Predictor with Custom Generative AI for Real Estate Agents.
This project aims to provide a comprehensive tool for real estate agents, combining a house price predictor with custom generative AI capabilities for generating professional reports.


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
This is group ARO's exam project for the AI course 2024.
The project was developed by Andreas, Owais and Rasmus from CPH-business academy.

Data Collection:
Housing prices for the Hovedstadsområdet area will be scrapped from dingeo.dk. A curated list of zip codes will be selected to ensure a representative dataset.
features include:

Supervised Machine Learning:
Utilizing the scraped data, supervised machine learning techniques will be employed to train a predictive model. The model will analyze various house features to accurately predict prices.
User Interface:
A user-friendly Python GUI (using Custom-Tkinter) will be developed to facilitate interaction with the model. Real estate agents can input house data for different features via the GUI, and the trained model will provide predicted prices.
Custom Generative AI:
Upon receiving the predicted price, users can opt to generate a professional report. This process will involve a custom generative AI solution trained on relevant real estate documents and websites.
PDF Report Generation:
The generated report will be formatted into a PDF document. Users can download the report locally to their machines for further review or presentation to clients.


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

### Design
The project is divided up in directories.
Scraping directory has files with methods which can gather data from dingeo.dk, a website with houses for sale.
Data directory stores the data webscraped from dingeo.dk, and also holds the vector database.
Notebooks directory is where we do our data wrangling, with the data stored in data directory, to train various models and pick the best one.
Models directory stores the best performing model based on its R^2-score.
GenAI directory trains the generative AI. We load data from websites revolving real estate, split it into chunks and save them in the vector database in data directory.
GUI directory has one file, the GUI which uses the best model and generative AI. This is also the file to start project.

### Code
Our code is written in Python.

### Artefacts
Data scaped from dingeo.dk is saved in csv files based on zip codes. For the model training we collect the data into datasets with columns based on the features gathered from the webscraping. 
To find the best model, we train multiple models such as Linear Regression and Random Forest Regression.
A vector database is used to store chuncks of data, used for training a generative AI. We use the large language model Ollama as the generative AI.

### Outcomes
The best trained model became Gradient Boosting based on the R^2-score of 0.83. 
When predicting house prices, the result is not 100% accurate if compared to the origin source from the webscraped site, but it is fairly close.
The generative AI can take the input and predicted price result from our GUI and generate a text, which gets saved as a PDF file.


## Setup project instructions
1. Clone repository.
2. Have Ollama running. Type ollama serve in a terminal if it is not already running.
3. Run UI.py file in the terminal to start GUI. Path to the file is AI_Exam/GUI/UI.py

## Status
After starting the GUI, users can input information about a house. Based on this information, a price is predicted using a selected model trained specifically for this task. If Ollama is running, the AI will generate a descriptive document about the house, detailing its features. This text is then saved as a PDF file, which real estate agents can use.

For future improvements, we could focus on training a new model to achieve a better performance score than our current best model. One challenge we faced was determining the optimal number of features needed to accurately predict house prices. The current features were all sourced from the same website, which describes each house using these features. However, we believe that additional factors also significantly impact its value, but were not included in the website's data, for example the distance to nearest ocean or the current state of the economics in the society.

In summary, while the house price predictor does generate a price estimate, it is not 100% accurate compared to the original source.
