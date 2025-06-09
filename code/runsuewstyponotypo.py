import supy as sp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions.util import *
from matplotlib import cm


yaml_path = 'C:/GitHub/SUEWS_DB_Typology_test/postsub/test1.yml'

value = sp.data_model.init_config_from_yaml(yaml_path)
config_typo = value.to_df_state()

yaml_path = 'C:/GitHub/SUEWS_DB_Typology_test/postsub/test2.yml'

value = sp.data_model.init_config_from_yaml(yaml_path)
config_notypo = value.to_df_state()

config_typo['storageheatmethod'] = 6
config_notypo['storageheatmethod'] = 6

met_path = 'C:/GitHub/SUEWS_DB_Typology_test/postsub/forcing_OB1.txt'
df_forcing = sp._load.load_SUEWS_Forcing_met_df_yaml(met_path)

df_forcing['U'][df_forcing['U'] < 0.5] = 0.5

df_output_2017_typo, df_final_state_2017_typo = process_in_chunks(config_typo, df_forcing.loc['2017-01': '2017-10'], chunk_size = 3)
df_output_2017_notypo, df_final_state_2017_notypo = process_in_chunks(config_notypo, df_forcing.loc['2017-01': '2017-10'], chunk_size = 3)

start_date = '2017-11-01'

df_output_typo, df_final_state_typo = process_in_chunks(df_final_state_2017_typo.loc[start_date], df_forcing.loc[start_date: '2017-12'], chunk_size = 1)
# p2
df_output_notypo, df_final_state_notypo = process_in_chunks(df_final_state_2017_notypo.loc[start_date], df_forcing.loc[start_date: '2017-12'], chunk_size = 1)

