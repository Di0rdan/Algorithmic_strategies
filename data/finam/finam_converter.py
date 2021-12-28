from sys import argv
import pandas as pd


if len(argv) < 2:
    raise ValueError(
        f'''
        expected file name
        example of usage:
        
        python3 {argv[0]} GAZP_211223_211224-min.csv
        ''')

file_name = argv[1]

df_raw = pd.read_csv(f'raw/{file_name}')

df = pd.DataFrame(columns=['Timestamp', 'Price'])
df['Price'] = df_raw['<CLOSE>']
df['Timestamp'] = pd.to_datetime(df_raw['<DATE>'] + 'T' + df_raw['<TIME>'])

df.to_csv(f'{file_name.split("_")[0]}_{df.Timestamp[0]}_{df.Timestamp[df.shape[0] - 1]}.csv', index=False)
