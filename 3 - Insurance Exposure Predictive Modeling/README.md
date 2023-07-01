# Insurance Predictive Modeling Project

This project focuses on insurance predictive modeling using a dataset related to insurance premiums, losses, and building exposures. The goal is to analyze the data and build a linear regression model to predict insurance premiums based on various factors. The project involves data preprocessing, data visualization, feature engineering, model training, and evaluation.

## Prerequisites

Make sure you have installed the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- sklearn

## Project Structure

The project consists of a Jupyter Notebook file that performs the insurance predictive modeling. The file is structured into several steps:

1. **Loading Data**: The data is imported from a CSV file using Pandas' `read_csv` function.

2. **Data Exploration**: This step involves exploring the dataset, grouping data by state, and creating visualizations such as bar charts and scatter plots.

3. **Data Preprocessing**: The data is preprocessed by adding a new column for the age of the home, calculating ratio metrics for ceded premium and ceded losses, dropping irrelevant columns, handling missing values, and applying dummy variables.

4. **Correlation Analysis**: A correlation coefficient matrix is created to analyze the relationships between variables, with a focus on the correlation with total premiums.

5. **Data Splitting**: The dataset is split into training and testing sets using the `train_test_split` function from the `sklearn.model_selection` module.

6. **Model Training**: A linear regression model is trained using the training data to predict insurance premiums. Additionally, a Ridge model is trained for comparison purposes.

7. **Model Evaluation**: The trained models are evaluated using metrics such as R-squared (R2), root mean squared error (RMSE), and mean absolute error (MAE).

## Running the Project

To run the project, follow these steps:

1. Make sure you have Python and Jupyter Notebook installed on your machine.

2. Clone the repository to your local machine.

3. Navigate to the cloned repository.