# AI Exam project: [insert title here (e.g. PyHousr)]

[insert images of product here]

House Price Predictor with Custom Generative AI for Real Estate Agents.
This project aims to provide a comprehensive tool for real estate agents, combining a house price predictor with custom generative AI capabilities for generating professional reports.



the Readme document includes problem statement, motivation, theoretical foundation, argumentation of
choices, design, code, artefacts, outcomes, and implementation instructions, as appropriate. the URL of the cloud location, where the application runs (if any)

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

### Motivation

### Theoretical Foundation

### Argumentation of Choices

### Design

### Code

### Artefacts

### Outcomes


## Extend Project


## Setup project instructions


## Status

hvor langt vi kom, any challenges?
forbedringer?
