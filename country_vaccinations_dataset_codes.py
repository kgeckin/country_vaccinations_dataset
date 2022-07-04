import pandas as pd

df_data_1 = pd.read_csv(body)
df_data_1.head()


# Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
# Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero).
df_data_1['daily_vaccinations']=df_data_1['daily_vaccinations'].replace(np.nan, 0).astype(int)
df_data_1.head()

# Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
df_data_1.nlargest(3, 'daily_vaccinations')

# What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?
df_data_1.loc[df_data_1['date'] == '1/6/2021', 'daily_vaccinations'].sum().astype(int)
