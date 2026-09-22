# %%
import fastf1
import pandas as pd
pd.set_option('display.max_columns', None)

# %%
# Pegando os dados generalistas da corrida e carrega os dados
session = fastf1.get_session(2021, 7, 'R')
session.load()

# %%
# Exibe e salva os dados obtidos
session.results
session.results.to_parquet("data/2021_07_R.parquet")

# %%
# Le os dados do ambiente local
df = pd.read_parquet(r'data\2021_07_R.parquet')
df
