import requests
from bs4 import BeautifulSoup

def buscar(nombre):
    url = f"https://www.tumangaonline.com/api/v1/mangas/search?title={nombre}"
    response = requests.get(url)
    data = response.json()

    if data and "mangas" in data and data["mangas"]:
        primerManga = data["mangas"][0]
        enlacePrimerManga = f"https://www.tumangaonline.com{primer_manga['url']}"

        return enlacePrimerManga

    else:

        return None

def descargar(enlace):
    response = request.get(enlace)
    contenido = response.text

    soup = BeautifulSoup(contenido, 'html.parser')
    texto = soup.get_text()

    return texto

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del manga: ")
    enlace = buscar(nombre)

    if enlace:
        print(f"Enlace del manga {enlace}")

        contenido = descargar(enlace)
        print(contenido)

    else:

        print(f"No se encontró el manga '{nombre}'.")
