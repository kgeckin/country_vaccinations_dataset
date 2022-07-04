import pandas as pd
df = pd.read_csv('country_vaccination_stats.csv')


# Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
# Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero).
df["daily_vaccinations"]=df["daily_vaccinations"].replace(np.nan, 0).astype(int)
df.head() # shows the first 5 columns

# Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.
df_data_1.nlargest(3, 'daily_vaccinations')

# What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?
df_data_1.loc[df_data_1['date'] == '1/6/2021', 'daily_vaccinations'].sum().astype(int)
