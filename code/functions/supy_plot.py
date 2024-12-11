# plot supy variables
from .night import night
import matplotlib.pyplot as plt
import pandas as pd
from .dict_legend import *# import dict_var_disp, dict_var_title, dict_var_ylabel

def supy_plot(var, df_merge, s,e, size=False, clr=False):
    var_w =  var + '_w'
    var_wd = var +'_w_d'
    var_wu = var + '_wu'
    var_wud= var + '_wu_d'

    if size:   
        size=size
    else:
        size = 6, 8

    if clr:
        clr=clr
    else:
        clr = ('#ff7f0e','#2ca02c')

    fig, axes = plt.subplots(2, 1, sharex=True)
    a = df_merge.loc[s:e,[var, var_w, var_wu]].rename(columns=dict_var_disp)\
        .plot(ax=axes[0],figsize=(size),title=dict_var_title[var])
    b = df_merge.loc[s:e,[var_wd, var_wud]].rename(columns=dict_var_disp)\
        .plot(ax=axes[1],figsize=(size),title=('Difference ' + dict_var_title[var]),color=clr)
    plt.hlines(0,s,'2012 08',linestyles='--',colors='grey')

    for i in [a,b]:
        night(i,df_merge,s,e)
        i.legend()
        i.set_ylabel(dict_var_ylabel[var])
        i.set_xlabel('')
    fig.tight_layout()

def create_subplots(var, grids, s, e):
    a_ssohm = df_output_merge_a_ssohm.SUEWS
    a_ssehc = df_output_merge_a_ssehc.SUEWS
    b_ssohm = df_output_merge_b_ssohm.SUEWS
    b_ssehc = df_output_merge_b_ssehc.SUEWS
    c_ssohm = df_output_merge_c_ssohm.SUEWS
    c_ssehc = df_output_merge_c_ssehc.SUEWS

    fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    
    # First column (SSOHM)
    axs[0, 0].plot(merge_grids_to_df(a_ssohm, grids, s, e, var))
    axs[0, 0].set_title('SSOHM - A')
    
    axs[1, 0].plot(merge_grids_to_df(b_ssohm, grids, s, e, var))
    axs[1, 0].set_title('SSOHM - B')
    
    axs[2, 0].plot(merge_grids_to_df(c_ssohm, [1], s, e, var))
    axs[2, 0].set_title('SSOHM - C')
    
    # Second column (SSEHC)
    axs[0, 1].plot(merge_grids_to_df(a_ssehc, grids, s, e, var))
    axs[0, 1].set_title('SSEHC - A')
    
    axs[1, 1].plot(merge_grids_to_df(b_ssehc, grids, s, e, var))
    axs[1, 1].set_title('SSEHC - B')
    
    axs[2, 1].plot(merge_grids_to_df(c_ssehc, [1], s, e, var))
    axs[2, 1].set_title('SSEHC - C')
    
    for ax in axs.flat:
        ax.label_outer()
    
    plt.tight_layout()
    plt.show()


def create_subplots_with_secondary_axis(var, grids, s, e, secondary_var):
    a_ssohm = df_output_merge_a_ssohm.SUEWS
    a_ssehc = df_output_merge_a_ssehc.SUEWS
    b_ssohm = df_output_merge_b_ssohm.SUEWS
    b_ssehc = df_output_merge_b_ssehc.SUEWS
    c_ssohm = df_output_merge_c_ssohm.SUEWS
    c_ssehc = df_output_merge_c_ssehc.SUEWS

    secondary_data = df_forcing.loc[s:e, secondary_var]

    fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    
    # First column (SSOHM)
    ax1 = axs[0, 0]
    ax1.plot(merge_grids_to_df(a_ssohm, grids, s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSOHM - A')
    
    ax1 = axs[1, 0]
    ax1.plot(merge_grids_to_df(b_ssohm, grids, s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSOHM - B')
    
    ax1 = axs[2, 0]
    ax1.plot(merge_grids_to_df(c_ssohm, [1], s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSOHM - C')
    
    # Second column (SSEHC)
    ax1 = axs[0, 1]
    ax1.plot(merge_grids_to_df(a_ssehc, grids, s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSEHC - A')
    
    ax1 = axs[1, 1]
    ax1.plot(merge_grids_to_df(b_ssehc, grids, s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSEHC - B')
    
    ax1 = axs[2, 1]
    ax1.plot(merge_grids_to_df(c_ssehc, [1], s, e, var), label=var)
    ax2 = ax1.twinx()
    ax2.plot(secondary_data, color='grey', label=secondary_var, alpha = 0.5)
    ax1.set_title('SSEHC - C')
    
    for ax in axs.flat:
        ax.label_outer()
    
    plt.tight_layout()
    plt.show()

# def print_test_cases(spartacus_test_dict, runcontrol_dict):
#     # Generate markdown table
#     markdown_output = "| CASE                | a_SSOHM | a_SSEHC |\n"
#     markdown_output += "|---------------------|---------|---------|\n"

#     methods = ['stabilitymethod', 'roughlenheatmethod', 'roughlenmommethod', 'storageheatmethod', 'netradiationmethod']

#     for method in methods:
#         row = f"| {method.capitalize()} |"
#         for test_case, settings in spartacus_test_dict.items():
#             value = settings[method]
#             description = runcontrol_dict[method][value]
#             row += f" ({value}) \"{description}\" |"
#         markdown_output += row + "\n"
    
#     return markdown_output
