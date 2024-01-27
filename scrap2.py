from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
import smtplib
import time
import requests
from bs4 import BeautifulSoup

# from dotenv import load_dotenv

# # Cargar variables de entorno desde el archivo .env
# load_dotenv()
#codigo para hacer scraping a la pagina de secop 1 holaa

url = 'https://www.contratos.gov.co/consultas/resultadosConsulta.do?&action=validate_captcha&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&ctl00$ContentPlaceHolder1$hidRedir=&cuantia=0&departamento={valor1}&desdeFomulario=true&entidad=&estado=&fechaFinal=&fechaInicial={valor3}&findEntidad=&g-recaptcha-response=03AFcWeA6UqRYHARxiXlGlKUNO6hNeMFtadzC_8z1DacId8yWAZ6-GM23vp4HI5veWNqasb_VeDlNiIyUhOqpIcuE-5rW3Qx7BOJuFYhefDCMuJmLdO9i7Gp6iBrlIaJ0U9fiktRHS_zdSnNjRNtO3J9V-YW_dssALWOnYAo_LVpnK8XY9mZ01g9ty9U48G6098SxAWJuRRI2igxcIvvNM4OD2AeaenCCkj9cntUYlUy_HFoiGAOoP4hetWWYZdDR-ByArH6_IhGs9s4ex8nPmINBhd1cE4hM1F3rz_e41DHXS63GnwXK2VlSLDhWJrmuojlCZdQ2EGzetg_fxUDehDdXVZwJI8leh4BPf37_GFxPkDwIM7XKYAUWKpRz0dh8LpjcITTp7_5nX4jdsP7aJd14IM5_gssXgZ3840f9qksWdMwXkFxItKUAxF6rZd-SnwtiDotB1ozTPQaWbyvbW6ynN7pFv2N_QStV72BAv96B7TVmgirRWl17CQPux2mpYOvckQNulJgxvjOY8V1weIi53i7xn1tBySWb4x5WtqVl__TEqk-oCL1qPj2FhdbwwnrXAV-Plyqafnm29D18KYVtkqHevw5gcvw&municipio=0&numeroProceso=&objeto={valor2}&paginaObjetivo=1&registrosXPagina=50&tipoProceso='




#Parametros necesarios para hacer la busqueda

params = {
    'departamento': 15000,
    'objeto': 25000000,
    'fechaInicial': '01/01/2024'
}

#procesos
procesos = []

url = url.format(valor1 = params['departamento'], valor2 = params['objeto'], valor3 = params['fechaInicial'])
# Realiza la solicitud

# user_agent_list = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/101.0.0.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/95.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.0.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
# ]


# headers = {
#     'User-Agent': random.choice(user_agent_list),
# }

time.sleep(3)
response = requests.get(url)

print(response)

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla que contiene la información de los procesos
tabla_procesos = soup.find('table', {'border': '0', 'cellpadding': '0', 'cellspacing': '0'})

if tabla_procesos:

    for fila in tabla_procesos.find_all('tr')[1:]:

        # Extraer datos de cada celda en la fila
        datos_celda = fila.find_all('td')

        procesos_encontrados = {
            'numeros_proceso': datos_celda[1].text.strip(),
            'tipos_proceso': datos_celda[2].text.strip(),
            'estados': datos_celda[3].text.strip(),
            'entidades': datos_celda[4].text.strip(),
            'objetos': datos_celda[5].text.strip(),
            'departamentos_municipios': datos_celda[6].text.strip(),
            'cuantias': datos_celda[7].text.strip(),
            'fechas': datos_celda[8].text.strip()            
        }
        procesos.append(procesos_encontrados)





# Configuración de la información del correo
sender_email = os.environ.get('SMTP_USERNAME')
receiver_email = "nicovalbuena2011@gmail.com"
subject = "Informe de Procesos"
body = "Adjunto encontrarás el informe de procesos."

# Configuración del servidor de correo
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.environ.get('SMTP_USERNAME')  # Accede a la variable de entorno
smtp_password = os.environ.get('SMTP_PASSWORD')  # Accede a la variable de entorno

# Crear el cuerpo del correo con la información en formato de tabla
table_body = """
<table border="1" style="border-collapse: collapse;">
    <tr>
        <th>Número de Proceso</th>
        <th>Tipo de Proceso</th>
        <th>Estado</th>
        <th>Entidad</th>
        <th>Objeto</th>
        <th>Departamento/Municipio</th>
        <th>Cuantía</th>
        <th>Fecha</th>
    </tr>
"""

for proceso in procesos:
    table_body += f"""
    <tr>
        <td>{proceso['numeros_proceso']}</td>
        <td>{proceso['tipos_proceso']}</td>
        <td>{proceso['estados']}</td>
        <td>{proceso['entidades']}</td>
        <td>{proceso['objetos']}</td>
        <td>{proceso['departamentos_municipios']}</td>
        <td>{proceso['cuantias']}</td>
        <td>{proceso['fechas']}</td>
    </tr>
    """

table_body += "</table>"

# Configuración del mensaje de correo
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Adjuntar el cuerpo del correo en formato HTML
message.attach(MIMEText(body + table_body, "html"))

# Conectar al servidor de correo y enviar el mensaje
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")