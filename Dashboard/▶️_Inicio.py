#Page1
from urllib.request import urlopen
import streamlit as st 
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
r = urlopen('https://github.com/Aurora-MR/COVID19_USA/raw/main/Covid_data/Frontend/stylei.css')
r = r.read().decode('utf-8')
st.markdown(f'<style>{r.read()}</style>', unsafe_allow_html=True)
st.markdown('<div align="right"><a href="https://aurora-mr-covid19-usa-dashboard-inicio-h7fwid.streamlitapp.com/Dashboard"><img src="https://github.com/Aurora-MR/COVID19_USA/raw/main/src/dashboardb.png"></a></div>', unsafe_allow_html=True)
st.markdown('# COVID-19(USA)')
st.markdown('## Introducción')
st.write(
		"""
		El 20 de enero de 2020, fue confirmado el primer caso conocido de COVID-19 en Estados Unidos. Un virus que en un par de meses posiciono a Estados Unidos como el país con más casos de COVID-19 en el mundo; 
		superando incluso al país donde se origino. Y que un mes más tarde, en abril del 2020 lo convertiría en el país con más muertes en el mundo.
		Los datos presentados proporcionan información histórica referente a la ocupación, escases de personal, hospitalizaciones y muertes generadas por el COVID-19 en Estados unidos. Los mismos se encontrarán mayormente expresados en forma gráfica y tabular, dando énfasis al desarrollo por estado.
		""")
st.markdown('## Objetivo')
st.markdown('Brindar información que sugiera en base a los datos recolectados, como organizar los recursos hospitalarios para prevenir que lo ocurrido durante la pandemia COVID-19 suceda de vuelta.')
st.markdown('## Consideraciones')
st.markdown(
		"""
        - Este trabajo esta realizado y actualizado según los datos proporcionados por el gobierno de Estados unidos desde la página <a href="https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh">healthdata.gov</a>.    
        - Todos los datos se encuentran expresados de forma acumulativa durante el periodo especificado.
 		""", unsafe_allow_html=True)
