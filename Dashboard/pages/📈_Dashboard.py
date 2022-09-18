#Dashboard
# import sys
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
# sys.path.append('/my/local/directory') #local
from Data_relations import *

st.set_page_config(layout='wide')
with open("https://github.com/Aurora-MR/COVID19_USA/raw/main/Covid_data/Frontend/style.css") as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)
st.write('<h1 style="text-align:center">COVID-19</h1>', unsafe_allow_html=True)

col1_1, col1_2 = st.columns([2, 5])
col2_1, col2_2, col2_3 = st.columns([1, 1, 5])
col3_1, col3_2, col3_3 = st.columns([1, 1, 5])
col4_1, col4_2, col4_3, col4_4, col4_5, col4_6, col4_7 = st.columns(7)
col1_1.write('##### Periodo de estudio')

#Fecha1
with col2_1:
    fechai = st.date_input('Fecha inicial', value=df_covid19['date'].min(), 
                                            min_value=df_covid19['date'].min(), 
                                            max_value=df_covid19['date'].max())
#Fecha2
with col2_2:
    fechaf = st.date_input('Fecha final', value=df_covid19['date'].max(), 
                                            min_value=df_covid19['date'].min(), 
                                            max_value=df_covid19['date'].max())

fecha1 = str(fechai)
fecha2 = str(fechaf)
#---------------------------------------------------------------------------
#Porcentaje COVID-19 positivos en cuidados intensivos por estado
col1_2.write('<h5 style="text-align:center">Ocupación hospitalaria en el área de cuidados intensivos</h5>', unsafe_allow_html=True)
df_covid19_icu_covid = df_covid19_icu_covid[(df_covid19_icu_covid['date'] >= fecha1) & (df_covid19_icu_covid['date'] <= fecha2)]
df_covid19_icu_covid = df_covid19_icu_covid.groupby(['name_state', 'state']).agg(np.sum)
df_covid19_icu_covid['percent_icu_beds_covid_adult'] = df_covid19_icu_covid.apply(lambda r: r['staffed_icu_adult_patients_confirmed_covid']/r['total_staffed_adult_icu_beds'], axis=1)
df_covid19_icu_covid['percent_icu_beds_covid_pediatric'] = df_covid19_icu_covid.apply(lambda r: r['staffed_icu_pediatric_patients_confirmed_covid']/r['total_staffed_pediatric_icu_beds'], axis=1)

#Adultos
df_covid19_icu_covid_a = df_covid19_icu_covid.loc[:, ['total_staffed_adult_icu_beds',
                                                      'staffed_icu_adult_patients_confirmed_covid',
                                                      'percent_icu_beds_covid_adult'
                                                      ]]
df_covid19_icu_covid_a = df_covid19_icu_covid_a.sort_values('percent_icu_beds_covid_adult', ascending=False)
df_covid19_icu_covid_a.reset_index(inplace=True)
df_covid19_icu_covid_a.fillna(0, inplace=True)
#Plot

def text(fr1, values):
    '''
    Regresa formato del texto que se mostrará en gráfico de pastel
    '''
    txt = np.round(fr1*100/np.sum(values),0)
    return "{:.2f}%".format(fr1)

def figure(vf, vt, i, color):
    '''
    Regresa gráfico de pastel
    '''
    fig, ax = plt.subplots()
    val = [vf[i], vt[i]-vf[i]]
    wedges, texts, autotexts = ax.pie(val, colors=[color, '#68797F'], autopct=lambda fr1: text(fr1, val), textprops=dict(color="w"))
    plt.setp(autotexts, size=20, weight="bold")
    ax.legend(['Ocupación'], loc="upper right", fontsize=18)
    fig.set_facecolor('#DFDFDF')
    ax.set_title(str(df_covid19_icu_covid_a['name_state'].iloc[i]), fontsize=23)
    return fig
#-------------------------------------------------------

pie_ta  = df_covid19_icu_covid_a['total_staffed_adult_icu_beds'].values
pie_ra  = df_covid19_icu_covid_a['staffed_icu_adult_patients_confirmed_covid'].values

try:
    for i in range(5):
        str1 = 'figpa'+str(i+1)
        globals()[str1] = figure(pie_ra, pie_ta, i, '#000064')
except ValueError:
    for i in range(5):
        str1 = 'figpa'+str(i+1)
        globals()[str1] = ''

#Pyplot
    # figpa1 = px.pie(values=[pie_ta[0], pie_ra[0]], 
    # title=str(df_covid19_icu_covid_a['name_state'].iloc[0]),width=100, height=100,
    # color_discrete_sequence=['#68797F', '#000064'])
    # figpa1.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpa2 = px.pie(values=[pie_ta[1], pie_ra[1]], 
    # title=str(df_covid19_icu_covid_a['name_state'].iloc[1]), width=100, height=100,
    # color_discrete_sequence=['#68797F', '#000064'])
    # figpa2.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpa3 = px.pie(values=[pie_ta[2], pie_ra[2]], 
    # title=str(df_covid19_icu_covid_a['name_state'].iloc[2]), width=100, height=100,
    # color_discrete_sequence=['#68797F', '#000064'])
    # figpa3.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpa4 = px.pie(values=[pie_ta[3], pie_ra[3]], 
    # title=str(df_covid19_icu_covid_a['name_state'].iloc[3]), width=100, height=100,
    # color_discrete_sequence=['#68797F', '#000064'])
    # figpa4.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpa5 = px.pie(values=[pie_ta[4], pie_ra[4]], 
    # title=str(df_covid19_icu_covid_a['name_state'].iloc[4]), width=100, height=100,
    # color_discrete_sequence=['#68797F', '#000064'])
    # figpa5.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

#layout
col3_3.write('Adultos')
col4_3.write(figpa1)
col4_4.write(figpa2)
col4_5.write(figpa3)
col4_6.write(figpa4)
col4_7.write(figpa5)

# #Área pediátrica
df_covid19_icu_covid_p = df_covid19_icu_covid.loc[:,['total_staffed_pediatric_icu_beds',
                                                     'staffed_icu_pediatric_patients_confirmed_covid',
                                                     'percent_icu_beds_covid_pediatric',
                                                     ]]
df_covid19_icu_covid_p = df_covid19_icu_covid_p.sort_values('percent_icu_beds_covid_pediatric', ascending=False)
df_covid19_icu_covid_p.reset_index(inplace=True)
df_covid19_icu_covid_p.fillna(0, inplace=True)

pie_tp  = df_covid19_icu_covid_p['total_staffed_pediatric_icu_beds'].values
pie_rp  = df_covid19_icu_covid_p['staffed_icu_pediatric_patients_confirmed_covid'].values

try:
    for i in range(5):
        str1 = 'figpp'+str(i+1)
        globals()[str1] = figure(pie_rp, pie_tp, i, '#00759D')
except ValueError:
    for i in range(5):
        str1 = 'figpp'+str(i+1)
        globals()[str1] = ''

#Pyplot
    # figpp1 = px.pie(values=[pie_tp[0], pie_rp[0]], 
    #           title=str(df_covid19_icu_covid_p['name_state'].iloc[0]), width=100, height=100,
    #           color_discrete_sequence=['#68797F', '#000064'])
    # figpp1.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpp2 = px.pie(values=[pie_tp[1], pie_rp[1]], 
    #           title=str(df_covid19_icu_covid_p['name_state'].iloc[1]), width=100, height=100,
    #           color_discrete_sequence=['#68797F', '#000064'])
    # figpp2.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpp3 = px.pie(values=[pie_tp[2], pie_rp[2]], 
    #           title=str(df_covid19_icu_covid_p['name_state'].iloc[2]), width=100, height=100,
    #           color_discrete_sequence=['#68797F', '#000064'])
    # figpp3.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpp4 = px.pie(values=[pie_tp[3], pie_rp[3]], 
    #           title=str(df_covid19_icu_covid_p['name_state'].iloc[3]), width=100, height=100,
    #           color_discrete_sequence=['#68797F', '#000064'])
    # figpp4.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))
    # figpp5 = px.pie(values=[pie_tp[4], pie_rp[4]], 
    #           title=str(df_covid19_icu_covid_p['name_state'].iloc[4]), width=100, height=100,
    #           color_discrete_sequence=['#68797F', '#000064'])
    # figpp5.update_layout(hoverlabel=dict(bgcolor='#68797F', font_size=16))

#layout
col5_1, col5_2, col5_3 = st.columns([1, 1, 5])
col5_3.write('Área pediátrica')
col6_1, col6_2, col6_3, col6_4, col6_5, col6_6, col6_7 = st.columns(7)
col6_3.write(figpp1)
col6_4.write(figpp2)
col6_5.write(figpp3)
col6_6.write(figpp4)
col6_7.write(figpp5)
#-----------------------------------------------------------

st.write('<h5 style="text-align:center">Ocupación hospitalaria por COVID-19</h5>', unsafe_allow_html=True)
col8_1, col8_2 = st.columns([1, 3])
#---------------------------------------------------------------
#Estados con mayor ocupación hospitalaria por COVID
#Periodo
df_covid19_occup = df_covid19_occup[(df_covid19_occup['date'] >= fecha1) & (df_covid19_occup['date'] <= fecha2)]
occup = df_covid19_occup['inpatient_beds_used_covid'].sum()
#Top
top_state_occup = df_covid19_occup.groupby(['name_state', 'lat', 'lon']).agg(np.sum)
top_state_occup = top_state_occup.loc[:, ['inpatient_beds_used_covid']]
top_state_occup.sort_values('inpatient_beds_used_covid', inplace=True, ascending=False)
top_state_occup.reset_index(inplace=True)
top_state_occup = top_state_occup[['name_state', 'inpatient_beds_used_covid']]
top_state_occup = top_state_occup.rename(columns={'name_state':'Estado', 'inpatient_beds_used_covid':'Ocupación hospitalaria'})
top_state_occup = top_state_occup.iloc[:5, :]
# top_state_occup['Porcentaje'] = top_state_occup.apply(lambda r: round((r['Ocupación hospitalaria']*100)/occup, 0), axis=1)
top_state_occup['Ocupación hospitalaria'] = top_state_occup['Ocupación hospitalaria'].map(lambda x: int(x))
top_state_occup.set_index(pd.Index([1,2,3,4,5]), drop=True, inplace=True)
# layout
col8_1.write('              .')
col8_1.write(f'Total: {occup}')

cell = {'selector': 'td', 'props': 'text-align: center; border-color:#000064'}
headers = {'selector': 'th:not(.index_name)', 
           'props': 'background-color: #68797F; text-align: center; color: #ffffff; font-weight: bold; border-color: #000064'}
col8_1.table(top_state_occup.style.set_table_styles([headers, cell]).bar(subset='Ocupación hospitalaria', vmax=occup, color='#68797F'))
#-----------------------------------------------------------------

#Total de hospitalizados por estado en pandemia
df_covid19_confirmed_state = df_covid19_confirmed_state[(df_covid19_confirmed_state['date'] >= fecha1) & (df_covid19_confirmed_state['date'] <= fecha2)]
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
#layout
col8_2.plotly_chart(fig5, use_container_width=True)
#---------------------------------------------------------------

# Hospitalizados con covid confirmado durante la pademia(pacientes adultos y pediátricos)
df_covid19_confirmed = df_covid19_confirmed[(df_covid19_confirmed['date'] >= fecha1) & (df_covid19_confirmed['date'] <= fecha2)]
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
#layout
st.plotly_chart(fig, use_container_width=True)
st.write('<h5 style="text-align:center">Cantidad de decesos por COVID-19 vs falta de personal medico</h5>', unsafe_allow_html=True)
col9_1, col9_2 = st.columns(2)
#-----------------------------------------------------------------

#Muertes por estado ocasionadas por COVID-19 y relación con falta de personal
df_covid19_rel_deaths_year = df_covid19_rel_deaths_year[(df_covid19_rel_deaths_year['date'] >= fecha1) & (df_covid19_rel_deaths_year['date'] <= fecha2)]
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
#layout
col9_1.plotly_chart(fig1, use_container_width=True)
#---------------------------------------------------------------
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
#layout
col9_2.plotly_chart(fig6, use_container_width=True)
col9_1.write(f'Correlación: {correl}')
