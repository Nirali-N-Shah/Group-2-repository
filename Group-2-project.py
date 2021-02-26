import pandas as pd    
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
dates_confirmed = confirmed_df.columns[4:]
dates_death = deaths_df.columns[4:]
#changing dataframe format to long id_vars=identifiers
confirmed_df_unpivoted = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates_confirmed, 
    var_name='Date', 
    value_name='Confirmed cases'

)
print('Daily confirmed cases Dataframe: ' )
print(confirmed_df_unpivoted)
deaths_df_unpivoted = deaths_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates_death, 
    var_name='Date', 
    value_name='Deaths'

)
print('Daily death cases Dataframe: ' )
print(deaths_df_unpivoted)
merged_df = confirmed_df_unpivoted.merge(
  right=deaths_df_unpivoted, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)
merged_df['Sum_global_cases'] = merged_df['Confirmed cases'] + merged_df['Deaths']
print('Dataframe showing sum of confirmed cases & Deaths: ')
print(merged_df)