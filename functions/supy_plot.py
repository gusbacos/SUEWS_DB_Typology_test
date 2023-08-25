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

