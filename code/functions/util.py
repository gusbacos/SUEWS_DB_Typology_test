import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import supy as sp


def merge_grids_to_df(smh5, grids, start_date, end_date, variable):
    # Initialize an empty list to store DataFrames
    df_list = []
    
    # Iterate over each grid and extract the relevant slice
    for grid in grids:
        df_slice = smh5.loc[grid].loc[start_date:end_date, variable]
        df_slice = df_slice.reset_index()  # Reset index to avoid issues with concatenation
        df_slice['grid'] = grid  # Add a column to identify the grid
        df_list.append(df_slice)
    
    # Concatenate all slices into a single DataFrame
    merged_df = pd.concat(df_list, ignore_index=True)
    
    # Pivot the DataFrame to have grids as columns
    pivot_df = merged_df.pivot(index='datetime', columns='grid', values=variable)
    
    return pivot_df


list_var_forcing = [
    "kdown",
    "Tair",
    "RH",
    "pres",
    "U",
    "rain",
]
dict_var_label = {
    "kdown": "Incoming Solar\n Radiation ($ \mathrm{W \ m^{-2}}$)",
    "Tair": "Air Temperature (C°)",
    "RH": r"Relative Humidity (%)",
    "pres": "Air Pressure (hPa)",
    "rain": "Rainfall (mm)",
    "U": "Wind Speed (m $\mathrm{s^{-1}}$)",
}

def process_in_chunks(df_state_init, df_forcing, chunk_size=5):
    df_output_list = []
    df_state_final_list = []
    
    # Calculate the number of chunks needed
    num_iterations = (len(df_state_init) + chunk_size - 1) // chunk_size
    print(num_iterations)

    for i in range(num_iterations):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        df_chunk = df_state_init.iloc[start_idx:end_idx]
        
        df_output, df_state_final = sp.run_supy(df_forcing, df_chunk)
        df_output_list.append(df_output)
        df_state_final_list.append(df_state_final)
    
    # Concatenate all chunks
    df_output_merge = pd.concat(df_output_list)
    df_state_final_merge = pd.concat(df_state_final_list)
    
    return df_output_merge, df_state_final_merge

# def plot_var(df_suews, start_date, end_date, var, figsize=False):
#     # Filter the DataFrame for the specified date range and variable
        
#     df_filtered = df_suews.loc[(slice(None), slice(start_date, end_date)), [var, 'Kdown']]
    
#     # Pivot the DataFrame to have grids as columns
#     df_plot = df_filtered[var].unstack(level=0)
#     kdown_plot = df_filtered['Kdown'].unstack(level=0)

#     if figsize is False:
#         figsize = (10, 5)
    
#     # Check if df_plot is empty
#     if df_plot.empty:
#         print("No data available for the specified date range and variable.")
#         return
#     figsize=(10,5)
#     # Plot the data
#     fig, ax = plt.subplots(figsize=figsize)
#     df_plot.plot(ax=ax, title=var, cmap ='tab20')
#     ax.axhline(y=0, linestyle='--', alpha=0.3, color='grey', linewidth = 0.9)
#     ax.legend(bbox_to_anchor=(1.0, 1.0))
#     plt.ylabel('Flux ($ \mathrm{W \ m^{-2}}$)')
    
#     # Shade areas where Kdown is 0
#     for column in kdown_plot.columns:
#         zero_regions = kdown_plot[column] < 5
#         for start, end in zip(zero_regions.index[zero_regions & ~zero_regions.shift(1, fill_value=False)], 
#                               zero_regions.index[zero_regions & ~zero_regions.shift(-1, fill_value=False)]):
#             ax.axvspan(start, end, color='grey', alpha=0.058, linewidth= 0)




# def plot_var(df_suews, start_date, end_date, var, var2=None, figsize=False):
#     # Filter the DataFrame for the specified date range and variables
#     columns = [var, 'Kdown']
#     if var2:
#         columns.append(var2)
#     df_filtered = df_suews.loc[(slice(None), slice(start_date, end_date)), columns]
    
#     # Pivot the DataFrame to have grids as columns
#     df_plot = df_filtered[var].unstack(level=0)
#     kdown_plot = df_filtered['Kdown'].unstack(level=0)
#     if var2:
#         df_plot2 = df_filtered[var2].unstack(level=0)

#     if figsize is False:
#         figsize = (10, 5)
    
#     # Check if df_plot is empty
#     if df_plot.empty:
#         print("No data available for the specified date range and variable.")
#         return
    
#     # Plot the data
#     fig, ax = plt.subplots(figsize=figsize)
#     df_plot.plot(ax=ax, title=var, cmap='tab20')
#     ax.axhline(y=0, linestyle='--', alpha=0.3, color='grey', linewidth=0.9)
#     ax.legend(bbox_to_anchor=(1.0, 1.0))
#     ax.set_ylabel('Flux ($ \mathrm{W \ m^{-2}}$)')
    
#     # Plot var2 on secondary axis if provided
#     if var2:
#         ax2 = ax.twinx()
#         df_plot2.plot(ax=ax2, linestyle='--')
#         # ax2.set_ylabel(f'{var2} ($ \mathrm{W \ m^{-2}}$)')
#         ax2.legend(bbox_to_anchor=(1.0, 0.9))
    
#     # Shade areas where Kdown is 0
#     for column in kdown_plot.columns:
#         zero_regions = kdown_plot[column] < 5
#         for start, end in zip(zero_regions.index[zero_regions & ~zero_regions.shift(1, fill_value=False)], 
#                               zero_regions.index[zero_regions & ~zero_regions.shift(-1, fill_value=False)]):
#             ax.axvspan(start, end, color='grey', alpha=0.058, linewidth=0)

#     plt.show()

def plot_var_other(df_suews, df_kdown, start_date, end_date, var, var2=None, figsize=False):
    # Filter the DataFrame for the specified date range and variables
    columns = [var]
    if var2:
        columns.append(var2)
    df_filtered = df_suews.loc[(slice(None), slice(start_date, end_date)), columns]
    df_kdown_filtered = df_kdown.loc[(slice(None), slice(start_date, end_date)), 'Kdown']
    
    # Pivot the DataFrame to have grids as columns
    df_plot = df_filtered[var].unstack(level=0)
    kdown_plot = df_kdown_filtered.unstack(level=0)
    if var2:
        df_plot2 = df_filtered[var2].unstack(level=0)

    if figsize is False:
        figsize = (10, 5)
    
    # Check if df_plot is empty
    if df_plot.empty:
        print("No data available for the specified date range and variable.")
        return
    
    # Plot the data
    fig, ax = plt.subplots(figsize=figsize)
    df_plot.plot(ax=ax, title=var, cmap='tab20')
    ax.axhline(y=0, linestyle='--', alpha=0.3, color='grey', linewidth=0.9)
    ax.legend(bbox_to_anchor=(1.0, 1.0))
    ax.set_ylabel('Flux ($ \mathrm{W \ m^{-2}}$)')
    
    # Plot var2 on secondary axis if provided
    if var2:
        ax2 = ax.twinx()
        df_plot2.plot(ax=ax2, linestyle='--')
        ax2.legend(bbox_to_anchor=(1.0, 0.9))
    
    # Shade areas where Kdown is 0
    for column in kdown_plot.columns:
        zero_regions = kdown_plot[column] < 5
        for start, end in zip(zero_regions.index[zero_regions & ~zero_regions.shift(1, fill_value=False)], 
                              zero_regions.index[zero_regions & ~zero_regions.shift(-1, fill_value=False)]):
            ax.axvspan(start, end, color='grey', alpha=0.058, linewidth=0)

    plt.show()


def plot_vars(df_suews, start_date, end_date, vars, figsize=False):
    # Filter the DataFrame for the specified date range and variables
    df_filtered = df_suews.loc[(slice(None), slice(start_date, end_date)), vars + ['Kdown']]
    
    # Pivot the DataFrame to have grids as columns
    df_plots = {var: df_filtered[var].unstack(level=0) for var in vars}
    kdown_plot = df_filtered['Kdown'].unstack(level=0)

    if not figsize:
        figsize = (10, 5 * len(vars))
    
    # Check if any df_plot is empty
    if any(df_plot.empty for df_plot in df_plots.values()):
        print("No data available for the specified date range and variables.")
        return
    
    # Plot the data
    fig, axes = plt.subplots(nrows=len(vars), ncols=1, figsize=figsize, sharex=True)
    
    if len(vars) == 1:
        axes = [axes]
    
    for ax, var in zip(axes, vars):
        df_plots[var].plot(ax=ax, title=var, cmap='tab20')
        ax.axhline(y=0, linestyle='--', alpha=0.3, color='grey', linewidth=0.9)
        ax.legend(bbox_to_anchor=(1.0, 1.0))
        ax.set_ylabel('Flux ($ \mathrm{W \ m^{-2}}$)')
        
        # Shade areas where Kdown is 0
        for column in kdown_plot.columns:
            zero_regions = kdown_plot[column] < 5
            for start, end in zip(zero_regions.index[zero_regions & ~zero_regions.shift(1, fill_value=False)], 
                                  zero_regions.index[zero_regions & ~zero_regions.shift(-1, fill_value=False)]):
                ax.axvspan(start, end, color='grey', alpha=0.058, linewidth=0)
    
    plt.xlabel('Date')
    plt.tight_layout()
    plt.show()

def plot_var(df_suews, start_date, end_date, var, var2=None, figsize=False):
    # Filter the DataFrame for the specified date range and variables
    columns = [var, 'Kdown']
    if var2:
        columns.append(var2)
    df_filtered = df_suews.loc[(slice(None), slice(start_date, end_date)), columns]
    
    # Pivot the DataFrame to have grids as columns
    df_plot = df_filtered[var].unstack(level=0)
    kdown_plot = df_filtered['Kdown'].unstack(level=0)
    if var2:
        df_plot2 = df_filtered[var2].unstack(level=0)

    if figsize is False:
        figsize = (10, 5)
    
    # Check if df_plot is empty
    if df_plot.empty:
        print("No data available for the specified date range and variable.")
        return
    
    # Plot the data
    fig, ax = plt.subplots(figsize=figsize)
    df_plot.plot(ax=ax, title=var, cmap='tab20')
    ax.axhline(y=0, linestyle='--', alpha=0.3, color='grey', linewidth=0.9)
    ax.legend(bbox_to_anchor=(1.0, 1.0))
    ax.set_ylabel('Flux ($ \mathrm{W \ m^{-2}}$)')
    
    # Plot var2 on secondary axis if provided
    if var2:
        ax2 = ax.twinx()
        df_plot2.plot(ax=ax2, linestyle='--')
        # ax2.set_ylabel(f'{var2} ($ \mathrm{W \ m^{-2}}$)')
        ax2.legend(bbox_to_anchor=(1.0, 0.9))
    
    # Shade areas where Kdown is 0
    for column in kdown_plot.columns:
        zero_regions = kdown_plot[column] < 5
        for start, end in zip(zero_regions.index[zero_regions & ~zero_regions.shift(1, fill_value=False)], 
                              zero_regions.index[zero_regions & ~zero_regions.shift(-1, fill_value=False)]):
            ax.axvspan(start, end, color='grey', alpha=0.058, linewidth=0)

    plt.show()


runcontrol_dict = {
    'stabilitymethod' : {
        0: "Not used.",
        1: "Not used.",
        2: "Momentum: unstable: Dyer [1974] modified by Högström [1988], stable: Van Ulden and Holtslag [1985], Heat: Dyer [1974] modified by Högström [1988], Comments: Not recommended in this version.",
        3: "Momentum: Campbell and Norman [1998] (Eq 7.27, Pg97), Heat: unstable: Campbell and Norman [1998], stable: Campbell and Norman [1998], Comments: Recommended in this version.",
        4: "Momentum: Businger et al. [1971] modified by Högström [1988], Heat: Businger et al. [1971] modified by Högström [1988], Comments: Not recommended in this version."
    },
    'storageheatmethod': {
        0: "Uses observed values of ΔQS supplied in meteorological forcing file.",
        1: "ΔQS modelled using the objective hysteresis model (OHM) [Grimmond et al., 1991] using parameters specified for each surface type.",
        3: "ΔQS modelled using AnOHM [Sun et al., 2017]. Not recommended in this version.",
        4: "ΔQS modelled using the Element Surface Temperature Method (ESTM) [Offerle et al., 2005]. Not recommended in this version.",
        5 : "EHC Module"
    },
    'netradiationmethod': { 
        0: "Uses observed values of Q* supplied in meteorological forcing file.",
        1: "Q* modelled with L↓ observations supplied in meteorological forcing file. Zenith angle not accounted for in albedo calculation.",
        2: "Q* modelled with L↓ modelled using cloud cover fraction supplied in meteorological forcing file [Loridan et al., 2011]. Zenith angle not accounted for in albedo calculation.",
        3: "Q* modelled with L↓ modelled using air temperature and relative humidity supplied in meteorological forcing file [Loridan et al., 2011]. Zenith angle not accounted for in albedo calculation.",
        11: "Same as 1 but with L↑ modelled using surface temperature. Not recommended in this version.",
        12: "Same as 2 but with L↑ modelled using surface temperature. Not recommended in this version.",
        13: "Same as 3 but with L↑ modelled using surface temperature. Not recommended in this version.",
        100: "Q* modelled with L↓ observations supplied in meteorological forcing file. Zenith angle accounted for in albedo calculation. SSss_YYYY_NARPOut.txt file produced. Not recommended in this version.",
        200: "Q* modelled with L↓ modelled using cloud cover fraction supplied in meteorological forcing file [Loridan et al., 2011]. Zenith angle accounted for in albedo calculation. SSss_YYYY_NARPOut.txt file produced. Not recommended in this version.",
        300: "Q* modelled with L↓ modelled using air temperature and relative humidity supplied in meteorological forcing file [Loridan et al., 2011]. Zenith angle accounted for in albedo calculation. SSss_YYYY_NARPOut.txt file produced. Not recommended in this version.",
        1001: "Q* modelled with SPARTACUS-Surface (SS) but with L↓ modelled as in 1. Experimental in this version.",
        1002: "Q* modelled with SPARTACUS-Surface (SS) but with L↓ modelled as in 2. Experimental in this version.",
        1003: "Q* modelled with SPARTACUS-Surface (SS) but with L↓ modelled as in 3. Experimental in this version."
    },
    'roughlenheatmethod': {
        1: "Uses value of 0.1*z0m.",
        2: "Calculated according to Kawai et al. [2009].",
        3: "Calculated according to Voogt and Grimmond [2000].",
        4: "Calculated according to Kanda et al. [2007].",
        5: "Adaptively using z0m based on pervious coverage: if fully pervious, use method 1; otherwise, use method 2. Recommended in this version."
    },
    'roughlenmommethod': {
    1: "Values specified in SUEWS_SiteSelect.txt are used. Tip: Note that UMEP provides tools to calculate these. See Kent et al. [2017] for recommendations on methods. Kent et al. [2017] have developed a method to include vegetation which is also available within UMEP.",
    2: "z0m and zd are calculated using ‘rule of thumb’ [Grimmond and Oke, 1999] using mean building and tree height specified in SUEWS_SiteSelect.txt. z0m and zd are adjusted with time to account for seasonal variation in porosity of deciduous trees.",
    3: "z0m and zd are calculated based on the Macdonald et al. [1998] method using mean building and tree heights, plan area fraction and frontal areal index specified in SUEWS_SiteSelect.txt. z0m and zd are adjusted with time to account for seasonal variation in porosity of deciduous trees."
    }
}


# def create_subplots(var, grids, s, e):
#     a_ssohm = df_output_merge_a_ssohm.SUEWS
#     a_ssehc = df_output_merge_a_ssehc.SUEWS
#     b_ssohm = df_output_merge_b_ssohm.SUEWS
#     b_ssehc = df_output_merge_b_ssehc.SUEWS
#     c_ssohm = df_output_merge_c_ssohm.SUEWS
#     c_ssehc = df_output_merge_c_ssehc.SUEWS

#     fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    
#     # First column (SSOHM)
#     axs[0, 0].plot(merge_grids_to_df(a_ssohm, grids, s, e, var))
#     axs[0, 0].set_title('SSOHM - A')
    
#     axs[1, 0].plot(merge_grids_to_df(b_ssohm, grids, s, e, var))
#     axs[1, 0].set_title('SSOHM - B')
    
#     axs[2, 0].plot(merge_grids_to_df(c_ssohm, [1], s, e, var))
#     axs[2, 0].set_title('SSOHM - C')
    
#     # Second column (SSEHC)
#     axs[0, 1].plot(merge_grids_to_df(a_ssehc, grids, s, e, var))
#     axs[0, 1].set_title('SSEHC - A')
    
#     axs[1, 1].plot(merge_grids_to_df(b_ssehc, grids, s, e, var))
#     axs[1, 1].set_title('SSEHC - B')
    
#     axs[2, 1].plot(merge_grids_to_df(c_ssehc, [1], s, e, var))
#     axs[2, 1].set_title('SSEHC - C')
    
#     for ax in axs.flat:
#         ax.label_outer()
    
#     plt.tight_layout()
#     plt.show()


# def create_subplots_with_secondary_axis(var, grids, s, e, secondary_var):
#     a_ssohm = df_output_merge_a_ssohm.SUEWS
#     a_ssehc = df_output_merge_a_ssehc.SUEWS
#     b_ssohm = df_output_merge_b_ssohm.SUEWS
#     b_ssehc = df_output_merge_b_ssehc.SUEWS
#     c_ssohm = df_output_merge_c_ssohm.SUEWS
#     c_ssehc = df_output_merge_c_ssehc.SUEWS

#     secondary_data = df_forcing.loc[s:e, secondary_var]

#     fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    
#     # First column (SSOHM)
#     ax1 = axs[0, 0]
#     ax1.plot(merge_grids_to_df(a_ssohm, grids, s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSOHM - A')
    
#     ax1 = axs[1, 0]
#     ax1.plot(merge_grids_to_df(b_ssohm, grids, s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSOHM - B')
    
#     ax1 = axs[2, 0]
#     ax1.plot(merge_grids_to_df(c_ssohm, [1], s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSOHM - C')
    
#     # Second column (SSEHC)
#     ax1 = axs[0, 1]
#     ax1.plot(merge_grids_to_df(a_ssehc, grids, s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSEHC - A')
    
#     ax1 = axs[1, 1]
#     ax1.plot(merge_grids_to_df(b_ssehc, grids, s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSEHC - B')
    
#     ax1 = axs[2, 1]
#     ax1.plot(merge_grids_to_df(c_ssehc, [1], s, e, var), label=var)
#     ax2 = ax1.twinx()
#     ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
#     ax1.set_title('SSEHC - C')
    
#     for ax in axs.flat:
#         ax.label_outer()
    
#     plt.tight_layout()
#     plt.show()

def print_test_cases(spartacus_test_dict, runcontrol_dict):
    # Generate markdown table
    markdown_output = "| CASE                | a_SSOHM | a_SSEHC |\n"
    markdown_output += "|---------------------|---------|---------|\n"

    methods = ['stabilitymethod', 'roughlenheatmethod', 'roughlenmommethod', 'storageheatmethod', 'netradiationmethod']

    for method in methods:
        row = f"| {method.capitalize()} |"
        for test_case, settings in spartacus_test_dict.items():
            value = settings[method]
            description = runcontrol_dict[method][value]
            row += f" ({value}) \"{description}\" |"
        markdown_output += row + "\n"
    
    return markdown_output