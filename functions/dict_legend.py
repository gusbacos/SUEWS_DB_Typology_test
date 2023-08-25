#!/usr/bin/env python
# coding: utf-8

# a dict for better display variable names
dict_var_disp = {
    
    'Kdown': r'$K_{\downarrow}$',
    'Kup': r'$K_{\uparrow}$',
    'Ldown': r'$L_{\downarrow}$',
    'Lup': r'$L_{\uparrow}$',
    
    'QN': '$Q^*$',
    'QS': r'$\Delta Q_S$',
    'QE': '$Q_E$',
    'QH': '$Q_H$',
    'QF': '$Q_F$',
    'RH2':'RH',
    'T2': '$T_2$',
    'Q2': '$Q_2$',
    'UStar':'$U^*$',
    'SMD':'SMD',
    'U10': 'U10',
    #_w
    'QN_w': '$Q^*$_w',
    'QS_w':  r'$\Delta Q_S$_w',
    'QE_w': '$Q_E$_w',
    'QH_w': '$Q_H$_w',
    'QF_w': '$Q_F$_w',
    'RH2_w':'RH_w',
    'T2_w': '$T_2$_w',
    'Q2_w': '$Q_2$_w',
    'UStar_w':'$U^*$_w',
    'SMD_w':'SMD_w',
    #_wu
    'QN_wu': '$Q^*$_wu',
    'QS_wu':  r'$\Delta Q_S$_wu',
    'QE_wu': '$Q_E$_wu',
    'QH_wu': '$Q_H$_wu',
    'QF_wu': '$Q_F$_wu',
    'RH2_wu':'RH_wu',
    'T2_wu': '$T_2$_wu',
    'Q2_wu': '$Q_2$_wu',
    'UStar_wu':'$U^*$_wu',
    'SMD_wu':'SMD_wu',
    #_delta_w
    'QN_w_d': '$\\Delta Q^*$_w',
    'QS_w_d': '$\Delta Q_S$_w',
    'QE_w_d': '$\Delta Q_E$_w',
    'QH_w_d': '$\Delta Q_H$_w',
    'QF_w_d': '$\Delta Q_F$_w',
    'RH2_w_d':'$\\Delta RH$_w',
    'T2_w_d': '$\\Delta T_2$_w',
    'Q2_w_d': '$\\Delta Q_2$_w',
    'UStar_w_d':'$\\Delta U^*$_w',
    'U10_w_d':'$\\Delta U10$_w',
    'SMD_w_d':'$\\Delta SMD$_w',        
    'RA_w_d':'$\\Delta RA$_w',

    #_delta_wu
    'QN_wu_d': '$\\Delta Q^*$_wu',
    'QS_wu_d': '$\Delta Q_S$_wu',
    'QE_wu_d': '$\Delta Q_E$_wu',
    'QH_wu_d': '$\Delta Q_H$_wu',
    'QF_wu_d': '$\Delta Q_F$_wu',
    'RH2_wu_d':'$\\Delta RH$_wu',
    'T2_wu_d': '$\\Delta T_2$_wu',
    'Q2_wu_d': '$\\Delta Q_2$_wu',
    'UStar_wu_d':'$\\Delta U^*$_wu',
    'U10_wu_d':'$\\Delta U10$_wu',
    'SMD_wu_d':'$\\Delta SMD$_wu',
    'RA_wu_d':'$\\Delta RA$_wu',

}

dict_var_disp_TS = {
    
    'Kdown': r'$K_{\downarrow}$',
    'Kup': r'$K_{\uparrow}$',
    'Ldown': r'$L_{\downarrow}$',
    'Lup': r'$L_{\uparrow}$',
    
    'QN': '$Q^*$_fKC_sKC',
    'QS': r'$\Delta Q_S$_fKC_sKC',
    'QE': '$Q_E$_fKC_sKC',
    'QH': '$Q_H$_fKC_sKC',
    'QF': '$Q_F$_fKC_sKC',
    'RH2':'RH_fKC_sKC',
    'T2': '$T_2$_fKC_sKC',
    'Q2': '$Q_2$_fKC_sKC',
    'UStar':'$U^*$_fKC_sKC',
    'SMD':'SMD_fKC_sKC',
    'U10': 'U10_fKC_sKC',
    'Ts': 'Ts_fKC_sKC',

    #_w
    'QN_w': '$Q^*$_fWS_sWS',
    'QS_w':  r'$\Delta Q_S$_fWS_sWS',
    'QE_w': '$Q_E$_fWS_sWS',
    'QH_w': '$Q_H$_fWS_sWS',
    'QF_w': '$Q_F$_fWS_sWS',
    'RH2_w':'RH_fWS_sWS',
    'T2_w': '$T_2$_fWS_sWS',
    'Q2_w': '$Q_2$_fWS_sWS',
    'UStar_w':'$U^*$_fWS_sWS',
    'SMD_w':'SMD_fWS_sWS',
    'Ts_w': 'Ts_fWS_sWS',
    #_wu
    'QN_wu': '$Q^*$_fWS_sKC',
    'QS_wu':  r'$\Delta Q_S$_fWS_sKC',
    'QE_wu': '$Q_E$_fWS_sKC',
    'QH_wu': '$Q_H$_fWS_sKC',
    'QF_wu': '$Q_F$_fWS_sKC',
    'RH2_wu':'RH_fWS_sKC',
    'T2_wu': '$T_2$_fWS_sKC',
    'Q2_wu': '$Q_2$_fWS_sKC',
    'UStar_wu':'$U^*$_fWS_sKC',
    'SMD_wu':'SMD_fWS_sKC',
    'Ts_wu': 'Ts_fWS_sKC',
    
    #_delta_w
    'QN_w_d': '$\\Delta Q^*$_fWS_sWS',
    'QS_w_d': '$\Delta Q_S$_fWS_sWS',
    'QE_w_d': '$\Delta Q_E$_fWS_sWS',
    'QH_w_d': '$\Delta Q_H$_fWS_sWS',
    'QF_w_d': '$\Delta Q_F$_fWS_sWS',
    'RH2_w_d':'$\\Delta RH$_fWS_sWS',
    'T2_w_d': '$\\Delta T_2$_fWS_sWS',
    'Q2_w_d': '$\\Delta Q_2$_fWS_sWS',
    'UStar_w_d':'$\\Delta U^*$_fWS_sWS',
    'U10_w_d':'$\\Delta U10$_fWS_sWS',
    'SMD_w_d':'$\\Delta SMD$_fWS_sWS',        
    'RA_w_d':'$\\Delta RA$_fWS_sWS',
    'Ts_w_d': '$\\Delta Ts$_fWS_sWS',


    #_delta_wu
    'QN_wu_d': '$\\Delta Q^*$_fWS_sKC',
    'QS_wu_d': '$\Delta Q_S$_fWS_sKC',
    'QE_wu_d': '$\Delta Q_E$_fWS_sKC',
    'QH_wu_d': '$\Delta Q_H$_fWS_sKC',
    'QF_wu_d': '$\Delta Q_F$_fWS_sKC',
    'RH2_wu_d':'$\\Delta RH$_fWS_sKC',
    'T2_wu_d': '$\\Delta T_2$_fWS_sKC',
    'Q2_wu_d': '$\\Delta Q_2$_fWS_sKC',
    'UStar_wu_d':'$\\Delta U^*$_fWS_sKC',
    'U10_wu_d':'$\\Delta U10$_fWS_sKC',
    'SMD_wu_d':'$\\Delta SMD$_fWS_sKC',
    'RA_wu_d':'$\\Delta RA$_fWS_sKC',
    'Ts_ws_d': '$\\Delta Ts$_fWS_sKC',

}

list_var_plot = [
    'QN',
    'QS',
    'QE',
    'QH',
    'QF',
    'RH2',
    'T2'
]
dict_var_ylabel = {
    'QN': 'Flux ($ \mathrm{W \ m^{-2}}$)',
    'QS': 'Flux ($ \mathrm{W \ m^{-2}}$)',
    'QE': 'Flux ($ \mathrm{W \ m^{-2}}$)',
    'QH': 'Flux ($ \mathrm{W \ m^{-2}}$)',
    'QF': 'Flux ($ \mathrm{W \ m^{-2}}$)',
    'RH2': 'Relative Humidity (%)',
    'T2': 'Air Temperature\n2 magl ($^{\\circ}}$C)',
    'Q2': 'Specific Humidity (g/$ \mathrm{kg^{-1}}$',
    'UStar':' ',
    'RA' : ' ',
    'SMD':'Soil Moisture Deficit (%)',
    'U10': 'Wind Speed (m $\mathrm{s^{-1}}$)',
    'Ts' : 'Surface Temperature ($^{\\circ}}$C)',

}

dict_var_title = {
    'QN': 'Net All-Wave Radiation',
    'QS': 'Storage Heat Flux',
    'QE': 'Latent Heat Flux',
    'QH': 'Sensible Heat Flux',
    'QF': 'Antrophogenic Heat Flux',
    'RH2': 'Relative Humidity',
    'T2': 'Air Temperature 2m agl',
    'Q2': 'Specific Humidity',
    'UStar':'Friction Velocity',
    'SMD':'Soil Moisture Deficit',        
    'U10': 'Wind Speed',
    'RA' : 'Aerodynamic Restistance',
    'Ts' : 'Surface Temperature',
}

list_var_forcing = [
    'kdown',
    'Tair',
    'RH',
    'pres',
    'U',
    'rain',
]
dict_var_label = {
    'kdown': 'Incoming Solar\n Radiation ($ \mathrm{W \ m^{-2}}$)',
    'Tair': 'Air Temperature ($^{\circ}}$C)',
    'RH': r'Relative Humidity (%)',
    'pres': 'Air Pressure (hPa)',
    'rain': 'Rainfall (mm)',
    'U': 'Wind Speed (m $\mathrm{s^{-1}}$)'
}