import requests
import pandas as pd
import datetime as dt
import numpy as np

#Obtención de datos
df_covid19 = pd.read_csv('https://healthdata.gov/api/views/g62h-syeh/rows.csv')
states = pd.read_csv('/home/aury/Henry/COVID19_Streamlit_copy/COVID19_Timeseries/COVID_data/states.csv')
#Merge
df_covid19 = pd.merge(df_covid19, states, on='state', how='left')

#Corrección valores faltantes
df_covid19.dropna(axis=1, inplace=True, thresh=df_covid19.shape[0]*0.2)
df_covid19.fillna(0, inplace=True)

#Corrección tipo de dato
#Date
df_covid19['date'] = pd.to_datetime(df_covid19['date'], infer_datetime_format=True)

#Reindexación
df_covid19 = df_covid19.sort_values('date')
df_covid19.reset_index(inplace=True, drop=True)

#Calendario
df_covid19['year'] = df_covid19['date'].dt.year
df_covid19['month']=df_covid19['date'].dt.month
df_covid19['day']=df_covid19['date'].dt.day
#-----------------------------------------------------------

#Estados con mayor ocupación hospitalaria por COVID 
#General
df_covid19_occup = df_covid19.loc[:, ['date', 'year', 'name_state',  'lat', 'lon',
                                    'inpatient_beds_used_covid',
                                    'staffed_icu_pediatric_patients_confirmed_covid',
                                    'total_adult_patients_hospitalized_confirmed_covid',
                                    'total_pediatric_patients_hospitalized_confirmed_covid'
                                    ]
                                ]
#-----------------------------------------------------------

#Porcentaje COVID-19 positivos en cuidados intensivos por estado
df_covid19_icu_covid = df_covid19.loc[:, ['date', 'name_state', 'state',
                                        'total_staffed_adult_icu_beds',
                                        'staffed_icu_adult_patients_confirmed_covid',
                                        'total_staffed_pediatric_icu_beds',
                                        'staffed_icu_pediatric_patients_confirmed_covid']]
#------------------------------------------------------------

#Muertes por estado ocasionadas por COVID-19 y relación con falta de personal
df_covid19_rel_deaths_year = df_covid19.loc[:, ['date', 'name_state', 'lat', 'lon', 
                                                'deaths_covid', 'critical_staffing_shortage_today_yes', 
                                                'critical_staffing_shortage_today_no']]
#------------------------------------------------------------

# Hospitalizados con covid confirmado durante la pademia(pacientes adultos y pediátricos)
df_covid19_confirmed = df_covid19.loc[:, ['date', 'year', 'month', 'day', 
                                          'total_adult_patients_hospitalized_confirmed_covid', 
                                          'total_pediatric_patients_hospitalized_confirmed_covid',
                                          'deaths_covid']]
#------------------------------------------------------------

#Total de hospitalizados por estado en pandemia
df_covid19_confirmed_state = df_covid19.loc[:, ['date', 'name_state', 'lat', 'lon', 'total_adult_patients_hospitalized_confirmed_covid', 'total_pediatric_patients_hospitalized_confirmed_covid']]
