import pandas as pd
import json
from dictionaries import target_kwh_by_city,contract_to_city,activities_normal,generation_unity

csvFile = r"F:\Users\jcportilla\python-csv\activities.csv"
df_actividades = pd.read_csv(csvFile, delimiter=',')

anomalieFile = r"F:\Users\jcportilla\python-csv\anomalies.csv"
df_anomalies = pd.read_csv(anomalieFile, delimiter=';')


def kwh_calculator(df):

      df['city'] = df['Contrato'].map(contract_to_city)
      df_filtered = df.dropna(subset=['city'])
      kwh_by_city = df_filtered.groupby('city')['kWhRec'].sum()

      print(kwh_by_city)

#kwh_calculator(df_anomalies)



df_actividades['activities_norm'] = df_actividades['Actividad'].map(activities_normal)
df_actividades['datetime'] = pd.to_datetime(df_actividades['Ejecucion'], errors='coerce')
# Extract month and create a new column 'mes'
df_actividades['mes'] = df_actividades['datetime'].dt.month
df_actividades['city'] = df_actividades['Contrato'].map(contract_to_city)
activity_counts = df_actividades.groupby(['city', 'activities_norm']).size().reset_index(name='count')

filtered_by_unity = df_actividades[df_actividades['N. Unidad'].isin(generation_unity)]
unity_counts = filtered_by_unity.groupby(['city', 'N. Unidad']).size().reset_index(name='count')



# dictionary

city_activity_dict = activity_counts.groupby('city')['count'].apply(list).to_dict()
unity_activity_dict = unity_counts.groupby('city')['count'].apply(list).to_dict()
#print("\nDictionary of counts by city:")
print(unity_counts)
#print(unity_activity_dict)

# Convert the dictionary to a JSON string
city_activity_json = json.dumps(city_activity_dict)
unity_activity_json = json.dumps(unity_activity_dict)



act_counts_by_month = df_actividades.groupby(['mes', 'activities_norm']).size().reset_index(name='count')
pivot_df = act_counts_by_month.pivot(index='mes', columns='activities_norm', values='count').fillna(0).reset_index()

result = {}
for activity in pivot_df.columns[1:]:  # Skip the 'month' column
    result[activity] = list(pivot_df[activity].astype(int))

by_month_json = json.dumps(result, indent=4)
by_unity_json = json.dumps(unity_activity_dict, indent=4)
print(by_unity_json)

# Display the JSON string
#print("\nJSON string of counts by city:")
#print(city_activity_json)