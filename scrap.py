import requests
from bs4 import BeautifulSoup
#codigo para hacer scraping a la pagina de secop 1

url = 'https://www.contratos.gov.co/consultas/resultadosConsulta.do?&action=validate_captcha&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&ctl00$ContentPlaceHolder1$hidRedir=&cuantia=0&departamento={valor1}&desdeFomulario=true&entidad=&estado=&fechaFinal=&fechaInicial={valor3}&findEntidad=&g-recaptcha-response=03AFcWeA6UqRYHARxiXlGlKUNO6hNeMFtadzC_8z1DacId8yWAZ6-GM23vp4HI5veWNqasb_VeDlNiIyUhOqpIcuE-5rW3Qx7BOJuFYhefDCMuJmLdO9i7Gp6iBrlIaJ0U9fiktRHS_zdSnNjRNtO3J9V-YW_dssALWOnYAo_LVpnK8XY9mZ01g9ty9U48G6098SxAWJuRRI2igxcIvvNM4OD2AeaenCCkj9cntUYlUy_HFoiGAOoP4hetWWYZdDR-ByArH6_IhGs9s4ex8nPmINBhd1cE4hM1F3rz_e41DHXS63GnwXK2VlSLDhWJrmuojlCZdQ2EGzetg_fxUDehDdXVZwJI8leh4BPf37_GFxPkDwIM7XKYAUWKpRz0dh8LpjcITTp7_5nX4jdsP7aJd14IM5_gssXgZ3840f9qksWdMwXkFxItKUAxF6rZd-SnwtiDotB1ozTPQaWbyvbW6ynN7pFv2N_QStV72BAv96B7TVmgirRWl17CQPux2mpYOvckQNulJgxvjOY8V1weIi53i7xn1tBySWb4x5WtqVl__TEqk-oCL1qPj2FhdbwwnrXAV-Plyqafnm29D18KYVtkqHevw5gcvw&municipio=0&numeroProceso=&objeto={valor2}&paginaObjetivo=1&registrosXPagina=50&tipoProceso='


# Inicializar listas para almacenar los datos
numeros_proceso = []
tipos_proceso = []
estados = []
entidades = []
objetos = []
departamentos_municipios = []
cuantias = []
fechas = []

#Parametros necesarios para hacer la busqueda

params = {
    'departamento': 73000,
    'objeto': 25000000,
    'fechaInicial': '01/01/2024'
}

url = url.format(valor1 = params['departamento'], valor2 = params['objeto'], valor3 = params['fechaInicial'])
# Realiza la solicitud
response = requests.get(url)

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla que contiene la información de los procesos
tabla_procesos = soup.find('table', {'border': '0', 'cellpadding': '0', 'cellspacing': '0'})

for fila in tabla_procesos.find_all('tr')[1:]:

    # Extraer datos de cada celda en la fila
    datos_celda = fila.find_all('td')
    
    # Añadir datos a las listas respectivas
    numeros_proceso.append(datos_celda[1].text.strip())
    tipos_proceso.append(datos_celda[2].text.strip())
    estados.append(datos_celda[3].text.strip())
    entidades.append(datos_celda[4].text.strip())
    objetos.append(datos_celda[5].text.strip())
    departamentos_municipios.append(datos_celda[6].text.strip())
    cuantias.append(datos_celda[7].text.strip())
    fechas.append(datos_celda[8].text.strip())

# Imprimir los resultados
for i in range(len(numeros_proceso)):
    print(f"Número de Proceso: {numeros_proceso[i]}")
    print(f"Tipo de Proceso: {tipos_proceso[i]}")
    print(f"Estado: {estados[i]}")
    print(f"Entidad: {entidades[i]}")
    print(f"Objeto: {objetos[i]}")
    print(f"Departamento y Municipio: {departamentos_municipios[i]}")
    print(f"Cuantía: {cuantias[i]}")
    print(f"Fecha: {fechas[i]}")
    print("\n" + "-"*50 + "\n")




# Imprime el contenido de la respuesta
# print(tabla_procesos)