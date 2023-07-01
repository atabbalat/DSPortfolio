# COVID-19 Analysis Project

This project analyzes COVID-19 related data such as the number of cases, deaths, vaccinations, and population for each country. The data is obtained from various sources, including a flat file, a webpage, and an API. The project involves data wrangling, data storage in a SQLite database, data combination using SQL JOIN operations, and data visualization.

## Prerequisites

Make sure you have installed the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- sqlite3
- requests

## Project Structure

The project consists of a Notebook file that performs the data analysis. The file is structured into several steps:

1. **Loading Data**: The data is imported from the flat file using Pandas' `read_csv` function. Additionally, data from a webpage and an API are fetched using the `requests` library.

2. **Data Wrangling**: This step involves cleaning and transforming the data. The column names in the flat file are updated for clarity. Columns that are not required for the analysis are removed. The data is summarized by grouping it by country and calculating the mean for missing reported dates. The webpage data is cleaned by replacing "N.A." with `None`, and the population column is converted to the float type. The API data is converted to a DataFrame, and the column names are updated. Data types for the confirmed cases and deaths columns are changed to float.

3. **Data Storing**: The cleaned data from each source is stored in separate tables within a SQLite database named "Covid_DB".

4. **Data Combination**: The data from different tables is combined using SQL JOIN operations. The combined data is retrieved as a DataFrame.

5. **Adding New Columns**: Additional columns are added to the combined DataFrame to calculate the ratio of each variable to the total population.

6. **Data Visualization**: Various data visualizations are created using matplotlib and seaborn. These include scatter plots, bar charts, histograms, density plots, and line graphs.

7. **Database Closure**: The database connection is closed after all operations.

## Running the Project

To run the project, follow these steps:

1. Make sure you have Python and Jupyter Notebook installed on your machine.

2. Clone the repository to your local machine.

3. Navigate to the cloned repository.