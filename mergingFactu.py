import pandas as pd
import json
csvFile = r"F:\Users\jcportilla\python-csv\CentroMeltedDate.csv"
df_melted = pd.read_csv(csvFile, delimiter=';')

# Create a mapping of month abbreviations to numerical values
month_map = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4,
    'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
    'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}

# Convert the month abbreviations to numerical values
df_melted['Month'] = df_melted['mes'].map(month_map)

output_path = r"F:\Users\jcportilla\python-csv\meltedMes.csv"
df_melted.to_csv(output_path, index=False)