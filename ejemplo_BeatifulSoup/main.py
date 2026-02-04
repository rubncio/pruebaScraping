if __name__=="__main__":
    from bs4 import BeautifulSoup

html_content = """tu_html_aqui""" # Aquí va el string que pegaste

soup = BeautifulSoup(html_content, 'html.parser')

# 1. Localizamos la tabla
tabla = soup.find('table', class_='wikitable')

# 2. Creamos la lista para guardar los nombres
nombres_versiones = []

# 3. Iteramos por las filas (saltándonos la primera que son los encabezados)
for fila in tabla.find_all('tr')[1:]:
    celdas = fila.find_all('td')
    if celdas:
        # Extraemos el texto de la primera celda
        # .get_text(strip=True) limpia espacios y saltos de línea
        version = celdas[0].get_text(strip=True)
        nombres_versiones.append(version)

# Resultado
print(nombres_versiones)