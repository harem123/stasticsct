import pandas as pd
import json
csvFile = r"F:\Users\jcportilla\python-csv\Centro.csv"
df_factu = pd.read_csv(csvFile, delimiter=';')



# Reshape the DataFrame from wide to long format
df_melted = df_factu.melt(id_vars=['NUI'], var_name='Date', value_name='Value')

# Filter out rows where 'Value' is empty
df_melted = df_melted[df_melted['Value'].notna()]

# Write the transformed DataFrame to a new CSV file
output_path = r"F:\Users\jcportilla\python-csv\CentroMelt.csv"
df_melted.to_csv(output_path, index=False)