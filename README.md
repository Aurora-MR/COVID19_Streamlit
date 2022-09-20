![COVID19](https://i.ibb.co/3yVwWJN/banner-covid.png)

# COVID-19(USA)

### Descripción
Se disponibiliza presentación sobre el desarrollo de la pandemia ocasionada por COVID19 en Estados unidos. En la misma se pueden visualizar los datos relacionados a la ocupación hospitalaria general y en cuidados intensivos por estado, mostrando un top de los estados más relevantes. Así mismo es posible observar la cantidad de decesos ocacionados por dicha pandemia y su relación con la falta de personal. 
El periodo de observaciones es seleccionado por el usuario.

### Presentación
La visualización de los datos fue implementada mediante la herramienta Streamlit de  python y es accesible desde el siguiente enlace: [Dashboard](https://aurora-mr-covid19-usa-dashboard-inicio-h7fwid.streamlitapp.com/)

### Datos utilizados
Se presentan los datos recuperados de la pagina de [healthdata.gov](https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh), en tiempo real.

### Alteraciones a los datos
- Se conservaron solo instancias correspondientes a decesos; reportes de falta de personal medico; total y ocupación hospitalaria general y en área de cuidados intensivos debido a COVID19.
- Se realizaron agrupaciónes por estado para presentar datos acumulados en el periodo requerido.
- El diccionario de datos esta disponible desde el siguiente link: [Diccionario](https://github.com/Aurora-MR/COVID19_USA/blob/main/Covid_data/diccionario.csv)