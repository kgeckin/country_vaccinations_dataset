# country_vaccinations_dataset

## Q1
Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero).

```
import pandas as pd
df = pd.read_csv('country_vaccination_stats.csv')
df["daily_vaccinations"]=df["daily_vaccinations"].replace(np.nan, 0).astype(int)
df.head() # shows the first 5 columns
```
![alt text](https://i.ibb.co/9p9d1qb/1.png)

## Q2
Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.

```
df = pd.read_csv('country_vaccination_stats.csv')
df.nlargest(3, 'daily_vaccinations')
```
![alt text](https://i.ibb.co/5jvHcGX/2.png)

## Q3
What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?

```
df.loc[df['date'] == '1/6/2021', 'daily_vaccinations'].sum().astype(int)

```
![alt text](https://i.ibb.co/sbqRvkB/3.png)
