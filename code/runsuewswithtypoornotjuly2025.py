import supy as sp
import pandas as pd


t = 'typo'

if t == 'typo':
    # Aggregated Typology data using DB
    yaml_path = 'C:/GitHub/SUEWS_DB_Typology_test/postsub/fa_1.yml'

    config = sp.data_model.init_config_from_yaml(yaml_path)
    df_state_init = config.to_df_state()
    grid = df_state_init.index[0]
    
    df_forcing = sp.load_forcing_grid(yaml_path, grid, df_state_init = df_state_init)

    df_state_init['netradiationmethod'] = 3
    df_state_init['storageheatmethod'] = 6

    fy = '2017'

    df_output_typo_1_5, df_final_state_typo_1_5 = sp.run_supy(df_forcing.loc[fy], df_state_init.loc[[1,2,3,4,5]], chunk_day=31)
    df_output_typo_6_10, df_final_state_typo_6_10 = sp.run_supy(df_forcing.loc[fy], df_state_init.loc[[6,7,8,9,10]], chunk_day=31)
    df_output_typo_11_15, df_final_state_typo_11_15 = sp.run_supy(df_forcing.loc[fy], df_state_init.loc[[11,12,13,14,15]], chunk_day=31)

    fy = '2018'
    sty= '2018-01-01'
    
    df_output_typo_1_5, df_final_state_typo_1_5 = sp.run_supy(df_forcing.loc[fy], df_final_state_typo_1_5.loc[sty], chunk_day=31)
    df_output_typo_6_10, df_final_state_typo_6_10 = sp.run_supy(df_forcing.loc[fy], df_final_state_typo_6_10.loc[sty], chunk_day=31)
    df_output_typo_11_15, df_final_state_typo_11_15 = sp.run_supy(df_forcing.loc[fy], df_final_state_typo_11_15.loc[sty], chunk_day=31)

    sp.save_supy(
        pd.concat([df_output_typo_1_5, df_output_typo_6_10, df_output_typo_11_15]), 
        pd.concat([df_final_state_typo_1_5, df_final_state_typo_6_10, df_final_state_typo_11_15]),
        path_dir_save= 'C:/GitHub/SUEWS_DB_Typology_test/postsub/typo' )

else:

    # Only Landshövdingegus
    yaml_path2 = 'C:/GitHub/SUEWS_DB_Typology_test/postsub/fa_notypo.yml'
    config2 = sp.data_model.init_config_from_yaml(yaml_path2)
    df_state_init2 = config2.to_df_state()
    grid = df_state_init2.index[0]
    df_forcing = sp.load_forcing_grid(yaml_path2, grid, df_state_init = df_state_init2)
    
    df_state_init2['netradiationmethod'] = 3
    df_state_init2['storageheatmethod'] = 6

    fy = '2017'

    df_output_notypo_1_5, df_final_state_notypo_1_5 = sp.run_supy(df_forcing.loc[fy], df_state_init2.loc[[1,2,3,4,5]], chunk_day=31)
    df_output_notypo_6_10, df_final_state_notypo_6_10 = sp.run_supy(df_forcing.loc[fy], df_state_init2.loc[[6,7,8,9,10]], chunk_day=31)
    df_output_notypo_11_15, df_final_state_notypo_11_15 = sp.run_supy(df_forcing.loc[fy], df_state_init2.loc[[11,12,13,14,15]], chunk_day=31)

    fy = '2018'
    sty= '2018-01-01'
    df_output_notypo_1_5, df_final_state_notypo_1_5 = sp.run_supy(df_forcing.loc[fy], df_final_state_notypo_1_5.loc[sty], chunk_day=31)
    df_output_notypo_6_10, df_final_state_notypo_6_10 = sp.run_supy(df_forcing.loc[fy], df_final_state_notypo_6_10.loc[sty], chunk_day=31)
    df_output_notypo_11_15, df_final_state_notypo_11_15 = sp.run_supy(df_forcing.loc[fy], df_final_state_notypo_11_15.loc[sty], chunk_day=31)

    df_notypo = pd.concat([df_output_notypo_1_5.SUEWS, df_output_notypo_6_10.SUEWS, df_output_notypo_11_15.SUEWS])

    sp.save_supy(
    pd.concat([df_output_notypo_1_5, df_output_notypo_6_10, df_output_notypo_11_15]), 
    pd.concat([df_final_state_notypo_1_5, df_final_state_notypo_6_10, df_final_state_notypo_11_15]),
    path_dir_save= 'C:/GitHub/SUEWS_DB_Typology_test/postsub/notypo' )