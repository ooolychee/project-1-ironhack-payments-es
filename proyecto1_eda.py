print("Hello")

import pandas as pd
import numpy as np
import seaborn as sns


request_df = pd.read_csv("//home/biomedmax/github/project-1-ironhack-payments-es/project_dataset/extract - cash request - data analyst.csv")
fees_df = pd.read_csv("//home/biomedmax/github/project-1-ironhack-payments-es/project_dataset/extract - fees - data analyst - .csv")

### Sumarios y visualizacion rapida ###
print(request_df.describe())
print(fees_df.describe())

print(request_df.head())
print(fees_df.head())

print(request_df.info())
print(fees_df.info())

# Ver como la cantidad de prestamos evoluciona con el tiempo #
import matplotlib.pyplot as plt
first_plot=request_df[["created_at", "amount"]]
request_df['created_at_normal'] = pd.to_datetime(request_df['created_at'])
monthly_sales = request_df.groupby(request_df['created_at_normal'].dt.to_period("M"))['amount'].sum()
monthly_sales
monthly_sales.plot(figsize=(12, 6))
plt.title('Evolution of loans')
plt.xlabel('Day')
plt.ylabel('Amount')
#plt.show()

#Ver si hau users que han pedido multiples loans
print(request_df["user_id"].value_counts())

#Cuanto ha pedido cada usuario en total
print(request_df.groupby("user_id")["amount"].sum())

#Cual es el maximo que un unico usuario pidio prestado en total
grouped = (request_df.groupby("user_id")["amount"].sum())
print(grouped.max())

#Ver las fees VS type of fee
by_type = fees_df.groupby('type')['total_amount'].sum()

print(by_type)

by_type.plot(kind="bar")
plt.title('Total fees by type')
plt.xticks(rotation=0)
#plt.show()

#Correlaciones entre todas las variables
print(fees_df.apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1))
print(sns.countplot(fees_df["charge_moment"]))


print(fees_df["category"])