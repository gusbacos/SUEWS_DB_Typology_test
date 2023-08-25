#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
import datetime

# def night(ax, df_, s, e, s_alpha=False):
#     idx =0
#     f_date = (date(int(s[0:4]),int(s[5:7]),int(s[7:10])))
#     l_date = (date(int(e[0:4]),int(e[5:7]),int(e[7:10])))
#     delta = (l_date - f_date)+ datetime.timedelta(days=2)
#     for i in range(delta.days):    
#         time = datetime.date(int(s[0:4]),int(s[5:7]),int(s[7:10])) + datetime.timedelta(days=idx)
#         time2 = time -datetime.timedelta(days=1)
#         a=str(time)[:10]
#         r=df_.loc[a:a]
#         up=r[r['Kdown']>0].index.tolist()
        
#         b=str(time2)[:10]
#         d=df_.loc[b:b]
#         down=d[d['Kdown']>0].index.tolist()

#         if s_alpha:
#             ax.axvspan(down[-1],up[0],alpha=s_alpha,color='grey')
#         else:
#             ax.axvspan(down[-1],up[0],alpha=0.07,color='grey')
        
#         idx=idx+1

def night(ax, df_in, s, e, s_alpha=False):
    idx =0
    f_date = (date(int(s[0:4]),int(s[5:7]),int(s[7:10])))
    l_date = (date(int(e[0:4]),int(e[5:7]),int(e[7:10])))
    delta = (l_date - f_date)+ datetime.timedelta(days=2)
    
    try:    
        df_in.loc['Kdown']
        var = 'Kdown'
    except:
        var = 'kdown'

    for i in range(delta.days):    
        time_plus = datetime.date(int(s[0:4]),int(s[5:7]),int(s[7:10])) + datetime.timedelta(days=idx)
        time_now = time_plus -datetime.timedelta(days=1)
        day_plus=str(time_plus)[:10]
        forc_plus=df_in.loc[day_plus]
        up=forc_plus[forc_plus[var]>0].index.tolist()
        
        day_now=str(time_now)[:10]
        forc_now=df_in.loc[day_now]
        down=forc_now[forc_now[var]>0].index.tolist()

        if s_alpha:
            try:
                ax.axvspan(down[-1],up[0],alpha=s_alpha,color='grey')
            except:
                ax.axvspan(down[-1], df_in.iloc[-1].name.strftime('%Y-%m-%d %H:%m'), alpha=s_alpha,color='grey')
                
        else:
            try:
                ax.axvspan(down[0],up[-1],alpha=0.07,color='grey')
            except:
                ax.axvspan(down[-1], df_in.iloc[-1].name.strftime('%Y-%m-%d %H:%m'),alpha= 0.07 ,color='grey')
        
        idx=idx+1
    


# Old Unused
def night_2(i):
    
    i.axvspan(pd.Timestamp('2012 7 18 20:30'),pd.Timestamp('2012 7 19 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 19 20:30'),pd.Timestamp('2012 7 20 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 20 20:30'),pd.Timestamp('2012 7 21 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 21 20:30'),pd.Timestamp('2012 7 22 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 22 20:30'),pd.Timestamp('2012 7 23 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 23 20:30'),pd.Timestamp('2012 7 24 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 24 20:30'),pd.Timestamp('2012 7 25 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 25 20:30'),pd.Timestamp('2012 7 26 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 26 20:30'),pd.Timestamp('2012 7 27 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 27 20:30'),pd.Timestamp('2012 7 28 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 28 20:30'),pd.Timestamp('2012 7 29 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 29 20:30'),pd.Timestamp('2012 7 30 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 30 20:30'),pd.Timestamp('2012 7 31 03:30'),alpha=0.07,color='grey')
    i.axvspan(pd.Timestamp('2012 7 31 20:30'),pd.Timestamp('2012 8 01 03:30'),alpha=0.07,color='grey')