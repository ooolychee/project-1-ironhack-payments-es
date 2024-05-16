# ReadMe for Cohort Analysis of Cash Requests and Fees

## Overview
This Jupyter Notebook performs a cohort analysis on cash requests and associated fees. The objective is to understand user behavior and trends over time, particularly focusing on the types of cash requests and the incidence of issues.

## Datasets
1. **Cash Requests Data (`filtered_cash`)**
   - Contains details about individual cash requests.
2. **Fees Data (`filtered_fees`)**
   - Contains information about fees associated with cash requests.

## Data Preprocessing
- **Datetime Conversion**: Convert relevant columns to datetime format.
- **User ID Handling**: Fill NaNs in `user_id` with values from `deleted_account_id` and convert to integer.
- **Cohort Creation**: Generate cohorts based on the month of the first request for each user.

## Analysis and Visualizations

### Distribution of Cash Requests by Cohort
- **Histogram**: Visualize the distribution of cash requests across different cohorts.

### Transfer Type Analysis
- **Pie Charts**: Display the proportion of instant vs. regular cash transfers for each cohort.
- **Bar Chart**: Show the count of different transfer types across cohorts.

### Cash Requests Over Time
- **Heatmap**: Show the number of cash requests received each month for each cohort.

### Amount Analysis
- **Binned Heatmap**: Display the distribution of cash request amounts across cohorts.

### Incident Analysis
- **Joining Datasets**: Combine the cash requests and fees data.
- **Incident Categories**: Fill missing values in the `category` column with "No incident".
- **Grouped Analysis**: Group data by incident category and cohort to observe trends.

### Incidence Rates
- **Stacked Area Chart**: Visualize the percentage of rejected direct debit and month delay incidents for each cohort.

### Fee Analysis
- **Total Fees by Cohort**: Sum the total fees collected from each cohort.
- **Line Plot**: Plot the total income in fees over time on a logarithmic scale.

## Instructions to Run the Notebook
1. Ensure the paths to the datasets (`filtered_cash` and `filtered_fees`) are correct.
2. Run the cells sequentially to preprocess the data, perform the analysis, and generate visualizations.
3. Adjust visualization parameters (e.g., figure size, titles) as needed for better clarity.

## Requirements
- Python 3.x
- Pandas
- Numpy
- Seaborn
- Matplotlib

## Conclusion
This notebook provides insights into the behavior of users across different cohorts, highlighting trends in cash request types, incidents, and associated fees. The visualizations help in understanding these patterns clearly and facilitate data-driven decision-making.

---

Please feel free to reach out if you have any questions or need further assistance with the analysis!
