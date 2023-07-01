# Diabetes Predictive Modeling Project

This project focuses on building predictive models for diabetes based on various health-related variables. The dataset used for this project is stored in the "diabetes.csv" file.

## Prerequisites

Make sure you have installed the following Python packages:

- pandas
- numpy
- seaborn
- matplotlib
- plotly
- scikit-learn
- yellowbrick

## Project Structure

The project is organized in a Jupyter Notebook and consists of the following sections:

1. **Base Libraries**: Importing the necessary libraries for data analysis, visualization, and modeling.

2. **Modeling Libraries**: Importing the libraries specifically required for the predictive modeling tasks.

3. **Warning Skip**: Suppressing warning messages to improve code readability.

4. **Settings**: Adjusting the settings for data display and visualization.

5. **Functions for Use**: Defining custom functions to be used in the analysis.

6. **Read Data**: Loading the "diabetes.csv" file into a pandas DataFrame.

7. **Data Overview**: Displaying basic information about the dataset, such as the data types and summary statistics.

8. **Data Cleaning**: Handling missing values and outliers in the dataset.

9. **Data Visualization**: Creating visualizations to explore the distribution of variables and their relationship with the outcome variable (diabetes).

10. **Data Preprocessing**: Splitting the dataset into features (X) and the target variable (y) and performing train-test split.

11. **Logistic Regression**: Fitting a logistic regression model, evaluating its performance, and generating a confusion matrix, ROC curve, and classification report.

12. **Random Forest**: Fitting a random forest classifier, evaluating its performance, and generating a confusion matrix, ROC curve, and classification report.

13. **Decision Tree**: Fitting a decision tree classifier, evaluating its performance, and generating a confusion matrix, ROC curve, and classification report.

14. **High Correlated Features**: Creating a new dataset by excluding high-correlated features, repeating the modeling steps, and comparing the results.

15. **Model Comparison**: Compiling the accuracy and evaluation metrics of the models for comparison.

16. **Results Visualization**: Visualizing the accuracy results of different models using a bar chart.

Please note that this README provides an overview of the project structure and the steps involved. For detailed explanations and code implementation, refer to the Jupyter Notebook file.