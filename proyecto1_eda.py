print("Hello")

import pandas as pd
import numpy as np

request_df = pd.read_csv("//home/biomedmax/github/project-1-ironhack-payments-es/project_dataset/extract - cash request - data analyst.csv")
fees_df = pd.read_csv("//home/biomedmax/github/project-1-ironhack-payments-es/project_dataset/extract - fees - data analyst - .csv")


print(request_df.describe())
print(fees_df.describe())

print(request_df.head())
print(fees_df.head())

print(request_df.info())
print(fees_df.info())

import matplotlib.pyplot as plt
first_plot=request_df[["created_at", "amount"]]
request_df['created_at_normal'] = pd.to_datetime(request_df['created_at'])
monthly_sales = request_df.groupby(request_df['created_at_normal'].dt.to_period("D"))['amount'].sum()
monthly_sales
monthly_sales.plot(figsize=(12, 6))
plt.title('Evolution of loans')
plt.xlabel('Day')
plt.ylabel('Amount')
#plt.show()

print(request_df["user_id"].value_counts())

