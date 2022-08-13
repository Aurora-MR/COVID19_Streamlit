#Page2
import requests
import pandas as pd
import datetime as dt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
st.markdown('# COVID-19')
col1, col2 = st.columns(2)
col3, col4, col5, col6, col7, col8, col9, col10= st.columns(8)
col11, col12 = st.columns(2)

#Obtención de datos
df_covid19 = pd.read_csv('https://healthdata.gov/api/views/g62h-syeh/rows.csv')
states = pd.read_csv('https://raw.githubusercontent.com/Aurora-MR/COVID19_Streamlit/main/states.csv')
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

#Fecha1
col1.write('Fecha')
with col3:
    st.write('Fecha inicial:')
    year = np.arange(2020, df_covid19['date'].max().year+1)
    year1 = st.selectbox('Año1', year)
    if year1 < df_covid19['date'].max().year:
        month = np.arange(1,13).tolist()
        month1 = st.selectbox('Mes1', month) 
        for n in range(7):
            o = 2*n+1
            e = 2*n
            if month1 == o:
                if o < 9:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,31).tolist()
            elif month1 == e:
                if e > 2 and e < 8:
                   day = np.arange(1,31).tolist()
                elif e >= 8:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,29).tolist()  
        day1 = st.selectbox('Día1', day)
    else: 
        month = np.arange(1,df_covid19['date'].max().month+1).tolist()
        month1 = st.selectbox('Mes1', month) 
        for n in range(7):
            o = 2*n+1
            e = 2*n
            if month1 == df_covid19['date'].max().month:
                day = np.arange(1, df_covid19['date'].max().day+1).tolist()
            elif month1 == o:
                if o < 9:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,31).tolist()
            elif month1 == e:
                if e > 2 and e < 8:
                   day = np.arange(1,31).tolist()
                elif e >= 8:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,29).tolist()  
        day1 = st.selectbox('Día1', day)
    #Fecha 1
    if month1 not in (10,11,12):
        if day1 in range(1,10):
            fecha1 = str(year1) + '-0' + str(month1) + '-0' + str(day1)
        else:
            fecha1 = str(year1) + '-0' + str(month1) + '-' + str(day1)
    else:
        if day1 in range(1,10):
            fecha1 = str(year1) + '-' + str(month1) + '-0' + str(day1)
        else:
            fecha1 = str(year1) + '-' + str(month1) + '-' + str(day1)
#Fecha2
with col4:
    st.write('Fecha final:')
    year = np.arange(2020, df_covid19['date'].max().year+1)
    year2 = st.selectbox('Año2', year)
    if year2 < df_covid19['date'].max().year:
        month = np.arange(1,13).tolist()
        month2 = st.selectbox('Mes2', month) 
        for n in range(7):
            o = 2*n+1
            e = 2*n
            if month2 == o:
                if o < 9:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,31).tolist()
            elif month2 == e:
                if e > 2 and e < 8:
                   day = np.arange(1,31).tolist()
                elif e >= 8:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,29).tolist()  
        day2 = st.selectbox('Día2', day)
    else: 
        month = np.arange(1,df_covid19['date'].max().month+1).tolist()
        month2 = st.selectbox('Mes2', month) 
        for n in range(7):
            o = 2*n+1
            e = 2*n
            if month2 == df_covid19['date'].max().month:
                day = np.arange(1, df_covid19['date'].max().day+1).tolist()
            elif month2 == o:
                if o < 9:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,31).tolist()
            elif month2 == e:
                if e > 2 and e < 8:
                   day = np.arange(1,31).tolist()
                elif e >= 8:
                   day = np.arange(1,32).tolist()
                else:
                   day = np.arange(1,29).tolist()  
        day2 = st.selectbox('Día2', day)
    #Fecha 2
    if month2 not in (10,11,12):
        if day2 in range(1,10):
            fecha2 = str(year2) + '-0' + str(month2) + '-0' + str(day2)
        else:
            fecha2 = str(year2) + '-0' + str(month2) + '-' + str(day2)
    else:
        if day2 in range(1,10):
            fecha2 = str(year2) + '-' + str(month2) + '-0' + str(day2)
        else:
            fecha2 = str(year2) + '-' + str(month2) + '-' + str(day2)
#---------------------------------------------------------------------------

# Estados con mayor ocupación hospitalaria por COVID 
#Total
df_covid19_occup_between = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
occup = df_covid19_occup_between['inpatient_beds_used_covid'].sum()
#General
df_covid19_occup = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
#Agrupación
#General
df_covid19_occup = df_covid19_occup.loc[:, ['date', 'year', 'name_state',  'lat', 'lon',
                                            'inpatient_beds_used_covid',
                                            'staffed_icu_pediatric_patients_confirmed_covid',
                                            'total_adult_patients_hospitalized_confirmed_covid',
                                            'total_pediatric_patients_hospitalized_confirmed_covid'
                                            ]
                                       ]
top_state_occup = df_covid19_occup.groupby(['name_state', 'lat', 'lon']).agg(np.sum)
top_state_occup = top_state_occup.loc[:, ['inpatient_beds_used_covid']]
top_state_occup.sort_values('inpatient_beds_used_covid', inplace=True, ascending=False)
top_state_occup.reset_index(inplace=True)
top_state_occup = top_state_occup[['name_state', 'inpatient_beds_used_covid']]
top_state_occup = top_state_occup.rename(columns={'name_state':'Estado', 'inpatient_beds_used_covid':'Ocupación hospitalaria'})
top_state_occup = top_state_occup.iloc[:5, :]
top_state_occup['Porcentaje'] = top_state_occup.apply(lambda r: round((r['Ocupación hospitalaria']*100)/occup, 0), axis=1)
#-----------------------------------------------------------

# Ocupación hospitalaria por COVID-19 en el área de cuidados intensivos
#Mayor ocupación por estado
df_covid19_icu = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
df_covid19_icu = df_covid19_icu.loc[:, ['date', 'name_state', 
                                        'staffed_adult_icu_bed_occupancy',
                                        'staffed_pediatric_icu_bed_occupancy']]
df_covid19_icu = df_covid19_icu.groupby('name_state').agg(np.sum)
#Adultos
df_covid19_icu_a = df_covid19_icu.sort_values('staffed_adult_icu_bed_occupancy', ascending=False)
df_covid19_icu_a.reset_index(inplace=True)
df_covid19_icu_a = df_covid19_icu_a.loc[:5,['name_state', 'staffed_adult_icu_bed_occupancy']]
df_covid19_icu_a = df_covid19_icu_a.rename(columns={'name_state':'Estado', 'staffed_adult_icu_bed_occupancy':'Ocupación hospitalaria'})
#Área pediátrica
df_covid19_icu_p = df_covid19_icu.sort_values('staffed_pediatric_icu_bed_occupancy', ascending=False)
df_covid19_icu_p.reset_index(inplace=True)
df_covid19_icu_p = df_covid19_icu_p.loc[:5,['name_state', 'staffed_pediatric_icu_bed_occupancy']]
df_covid19_icu_p = df_covid19_icu_p.rename(columns={'name_state':'Estado', 'staffed_pediatric_icu_bed_occupancy':'Ocupación hospitalaria'})
#-----------------------------------------------------------

#Porcentaje COVID-19 positivos en cuidados intensivos por estado
df_covid19_icu_covid = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
df_covid19_icu_covid = df_covid19_icu_covid.loc[:, ['date', 'name_state', 'state',
                                                    'total_staffed_adult_icu_beds',
                                                    'staffed_icu_adult_patients_confirmed_covid',
                                                    'total_staffed_pediatric_icu_beds',
                                                    'staffed_icu_pediatric_patients_confirmed_covid']]
df_covid19_icu_covid = df_covid19_icu_covid.groupby(['name_state', 'state']).agg(np.sum)
df_covid19_icu_covid['percent_icu_beds_covid_adult'] = df_covid19_icu_covid.apply(lambda r: r['staffed_icu_adult_patients_confirmed_covid']/r['total_staffed_adult_icu_beds'], axis=1)
df_covid19_icu_covid['percent_icu_beds_covid_pediatric'] = df_covid19_icu_covid.apply(lambda r: r['staffed_icu_pediatric_patients_confirmed_covid']/r['total_staffed_pediatric_icu_beds'], axis=1)

df_covid19_icu_covid_a = df_covid19_icu_covid.loc[:, ['total_staffed_adult_icu_beds',
                                                      'staffed_icu_adult_patients_confirmed_covid',
                                                      'percent_icu_beds_covid_adult'
                                                      ]]
df_covid19_icu_covid_a = df_covid19_icu_covid_a.sort_values('percent_icu_beds_covid_adult', ascending=False)
df_covid19_icu_covid_a.reset_index(inplace=True)
df_covid19_icu_covid_a.fillna(0, inplace=True)

df_covid19_icu_covid_p = df_covid19_icu_covid.loc[:,['total_staffed_pediatric_icu_beds',
                                                     'staffed_icu_pediatric_patients_confirmed_covid',
                                                     'percent_icu_beds_covid_pediatric',
                                                     ]]
df_covid19_icu_covid_p = df_covid19_icu_covid_p.sort_values('percent_icu_beds_covid_pediatric', ascending=False)
df_covid19_icu_covid_p.reset_index(inplace=True)
df_covid19_icu_covid_p.fillna(0, inplace=True)
col2.write('Ocupación hospitalaria en el área de cuidados intensivos')
col5.write('')
col5.write('Adultos')
col5.write('')
col5.write('')
col5.write('')
col5.write('')
col5.write('')
col5.write('')
col5.write('Área pediátrica')

#Plot
#Adultos
pie_ta  = df_covid19_icu_covid_a['total_staffed_adult_icu_beds'].values
pie_ra  = df_covid19_icu_covid_a['staffed_icu_adult_patients_confirmed_covid'].values

figpa1 = px.pie(values=[pie_ta[0], pie_ra[0]], 
          title=str(df_covid19_icu_covid_a['name_state'].iloc[0]),width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpa1.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
col6.plotly_chart(figpa1, use_container_width=True)

figpa2 = px.pie(values=[pie_ta[1], pie_ra[1]], 
          title=str(df_covid19_icu_covid_a['name_state'].iloc[1]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpa2.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
col7.plotly_chart(figpa2, use_container_width=True)


figpa3 = px.pie(values=[pie_ta[2], pie_ra[2]], 
          title=str(df_covid19_icu_covid_a['name_state'].iloc[2]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpa3.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

col8.plotly_chart(figpa3, use_container_width=True)

figpa4 = px.pie(values=[pie_ta[3], pie_ra[3]], 
          title=str(df_covid19_icu_covid_a['name_state'].iloc[3]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpa4.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

col9.plotly_chart(figpa4, use_container_width=True)

figpa5 = px.pie(values=[pie_ta[4], pie_ra[4]], 
          title=str(df_covid19_icu_covid_a['name_state'].iloc[4]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpa5.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
col10.plotly_chart(figpa5, use_container_width=True)

#Área pediátrica
pie_tp  = df_covid19_icu_covid_p['total_staffed_pediatric_icu_beds'].values
pie_rp  = df_covid19_icu_covid_p['staffed_icu_pediatric_patients_confirmed_covid'].values

figpp1 = px.pie(values=[pie_tp[0], pie_rp[0]], 
          title=str(df_covid19_icu_covid_p['name_state'].iloc[0]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])

figpp1.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
col6.plotly_chart(figpp1, use_container_width=True)


figpp2 = px.pie(values=[pie_tp[1], pie_rp[1]], 
          title=str(df_covid19_icu_covid_p['name_state'].iloc[1]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpp2.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

col7.plotly_chart(figpp2, use_container_width=True)

figpp3 = px.pie(values=[pie_tp[2], pie_rp[2]], 
          title=str(df_covid19_icu_covid_p['name_state'].iloc[2]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpp3.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

col8.plotly_chart(figpp3, use_container_width=True)

figpp4 = px.pie(values=[pie_tp[3], pie_rp[3]], 
          title=str(df_covid19_icu_covid_p['name_state'].iloc[3]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpp4.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

col9.plotly_chart(figpp4, use_container_width=True)

figpp5 = px.pie(values=[pie_tp[4], pie_rp[4]], 
          title=str(df_covid19_icu_covid_p['name_state'].iloc[4]), width=100, height=100,
          color_discrete_sequence=['#68797F', '#000064'])
figpp5.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
col10.plotly_chart(figpp5, use_container_width=True)
#-----------------------------------------------------------

#Muertes por estado ocasionadas por COVID-19 y relación con falta de personal
df_covid19_rel_deaths_year = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
df_covid19_rel_deaths_year = df_covid19_rel_deaths_year.loc[:, ['date', 'name_state', 'lat', 'lon', 
                                                                'deaths_covid', 'critical_staffing_shortage_today_yes', 
                                                                'critical_staffing_shortage_today_no']]
df_covid19_rel_deaths_year = df_covid19_rel_deaths_year.groupby(['name_state', 'lat', 'lon']).agg(np.sum)
df_covid19_rel_deaths_year.sort_values('deaths_covid', ascending=False, inplace=True)
df_covid19_rel_deaths_year.reset_index(inplace=True)

#Correlación
corr = df_covid19_rel_deaths_year.drop(['lat', 'lon'], axis=1)
corr = corr.corr()
correl = corr.iloc[0,1]
correl = round(correl, 2)


#Plot
fig1 = go.Figure()

fig1.add_trace(go.Scattergeo(
        lon = df_covid19_rel_deaths_year['lon'],
        lat = df_covid19_rel_deaths_year['lat'],
        customdata = df_covid19_rel_deaths_year[['name_state', 'deaths_covid']],
        marker = dict(
            color = '#000000', 
            size = df_covid19_rel_deaths_year['deaths_covid']/25,
            sizemode = 'area'),
        hovertemplate = '<i>Estado</i>: %{customdata[0]}' + '<br>Decesos</b>: %{customdata[1]}<br>', 
        name = 'Decesos por COVID-19')
        )

fig1.add_trace(go.Scattergeo(
        lon = df_covid19_rel_deaths_year['lon'],
        lat = df_covid19_rel_deaths_year['lat'],
        customdata = df_covid19_rel_deaths_year[['name_state', 'critical_staffing_shortage_today_yes']],
        marker = dict(
            color = '#000064', 
            size = df_covid19_rel_deaths_year['critical_staffing_shortage_today_yes']/25,
            sizemode = 'area'),
        hovertemplate = '<i>Estado</i>: %{customdata[0]}'+
                        '<br>Cantidad de hospitales con escasez de personal</b>: %{customdata[1]}<br>', 
        name = 'Cantidad de hospitales con escasez de personal')
        )


fig1.update_layout(title=f'Cantidad de decesos por COVID-19 vs falta de personal medico entre {fecha1} y {fecha2}', 
                    geo = dict( landcolor='#68797F', scope = 'usa'),
                    hoverlabel=dict(bgcolor='#68797F', font_size=16))
#------------------------------------------------------------

# Hospitalizados con covid confirmado durante la pademia(pacientes adultos y pediátricos)
df_covid19_confirmed = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
df_covid19_confirmed = df_covid19_confirmed.loc[:, ['date', 'year', 'month', 'day', 
                                                    'total_adult_patients_hospitalized_confirmed_covid', 
                                                    'total_pediatric_patients_hospitalized_confirmed_covid',
                                                    'deaths_covid']]
df_covid19_confirmed = df_covid19_confirmed.groupby(['year', 'month', 'day']).agg(np.sum)
df_covid19_confirmed.reset_index(inplace=True)
df_covid19_confirmed['date'] =df_covid19_confirmed.apply(lambda r: dt.date(int(r['year']), int(r['month']), int(r['day'])), axis=1)
df_covid19_confirmed.sort_values('date', inplace=True)

#Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_covid19_confirmed['date'], 
                         y=df_covid19_confirmed['total_adult_patients_hospitalized_confirmed_covid'], 
                         name='Pacientes adultos', mode='lines', line=dict(color='#000064')))

fig.add_trace(go.Scatter(x=df_covid19_confirmed['date'], 
                         y=df_covid19_confirmed['total_pediatric_patients_hospitalized_confirmed_covid'], 
                         name='Pacientes pediátricos', mode='lines', line=dict(color='#00759D')))

fig.update_layout(title=f'Hospitalizadas por COVID-19 entre {fecha1} y {fecha2}',
xaxis=dict(title='Fecha', gridcolor='rgba(0,0,0,0)', griddash='dash', ticks='outside',
tickcolor='#68797F'),
yaxis=dict(title='Cantidad de hospitalizados', gridcolor='#68797F', griddash='dash', ticks='outside',
tickcolor='#68797F'),
plot_bgcolor='rgba(0,0,0,0)')
#-----------------------------------------------------------

#Cantidad de decesos pandemia
#Plot
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=df_covid19_confirmed['date'], 
                         y=df_covid19_confirmed['deaths_covid'], 
                         name='Pacientes adultos', mode='lines', line=dict(color='#000000')))

fig6.update_layout(title=f'Decesos por COVID-19 entre {fecha1} y {fecha2}',
xaxis=dict(title='Fecha', gridcolor='rgba(0,0,0,0)', griddash='dash', ticks='outside',
tickcolor='#68797F'),
yaxis=dict(title='Cantidad de decesos', gridcolor='#68797F', griddash='dash', ticks='outside',
tickcolor='#68797F'),
plot_bgcolor='rgba(0,0,0,0)')
#-----------------------------------------------------------

#Total de hospitalizados por estado en pandemia
df_covid19_confirmed_state = df_covid19[(df_covid19['date'] >= fecha1) & (df_covid19['date'] <= fecha2)]
df_covid19_confirmed_state = df_covid19_confirmed_state.loc[:, ['date', 'name_state', 'lat', 'lon', 'total_adult_patients_hospitalized_confirmed_covid', 'total_pediatric_patients_hospitalized_confirmed_covid']]
df_covid19_confirmed_state = df_covid19_confirmed_state.groupby(['name_state', 'lat', 'lon']).agg(np.sum)
df_covid19_confirmed_state.reset_index(inplace=True)
#Plot
fig5 = go.Figure()

fig5.add_trace(go.Scattergeo(
        lon = df_covid19_confirmed_state['lon'],
        lat = df_covid19_confirmed_state['lat'],
        customdata = df_covid19_confirmed_state[['name_state', 'total_adult_patients_hospitalized_confirmed_covid']],
        marker = dict(
            color = '#000064', 
            size = df_covid19_confirmed_state['total_adult_patients_hospitalized_confirmed_covid']/3000,
            sizemode = 'area'),
        hovertemplate = '<i>Estado</i>: %{customdata[0]}' + '<br>Hospitalizados</b>: %{customdata[1]}<br>', 
        name = 'Pacientes adultos hospitalizados por COVID-19')
        )

fig5.add_trace(go.Scattergeo(
        lon = df_covid19_confirmed_state['lon'],
        lat = df_covid19_confirmed_state['lat'],
        customdata = df_covid19_confirmed_state[['name_state', 'total_pediatric_patients_hospitalized_confirmed_covid']],
        marker = dict(
            color = '#00759D', 
            size = df_covid19_confirmed_state['total_pediatric_patients_hospitalized_confirmed_covid']/3000,
            sizemode = 'area'),
        hovertemplate = '<i>Estado</i>: %{customdata[0]}'+
                        '<br>Hospitalizados</b>: %{customdata[1]}<br>', 
        name = 'Pacientes pediátricos hospitalizados por COVID-19')
        )


fig5.update_layout(title=f'Cantidad de hospitalizados por estado entre {fecha1} y {fecha2}', 
                    geo = dict( landcolor='#68797F', scope = 'usa'),
                    hoverlabel=dict(bgcolor='#68797F', font_size=16))

col11.write('Ocupación hospitalaria por COVID-19')
col11.write('## Total')
col11.write(occup)
col11.dataframe(top_state_occup)
col12.plotly_chart(fig, use_container_width=True)
with st.container():
    st.plotly_chart(fig5, use_container_width=True)
col13, col14 = st.columns(2)
col13.plotly_chart(fig1, use_container_width=True)
col14.plotly_chart(fig6, use_container_width=True)
col13.write('Correlación entre la cantidad de decesos por COVID-19 y falta de personal medico:')
col13.write(correl)
