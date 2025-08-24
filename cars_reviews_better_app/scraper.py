from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.chrome.options import Options
from django.core.management.base import BaseCommand
from cars_reviews_better_app.models import NoticiaDiferente
from django.conf import settings
import json
from django.db import IntegrityError



def obtener_noticias_scraping_otro():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página (para la primera sección de noticias)
    articulos = soup.find_all('article', class_='hero-poster poster-article')
    
    # Lista para almacenar las noticias de la primera sección
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título y el enlace de cada noticia
        titulo = articulo.find('h2', class_='poster-title')
        if titulo:
            enlace = titulo.find('a')['href']
            if enlace and not enlace.startswith('http'):
                enlace = url + enlace  # Asegura que el enlace sea completo
            noticias_info.append({
                'titulo': titulo.text.strip(),
                'link': enlace
            })
    
    # Encuentra todos los artículos en la página (para la segunda sección de noticias)
    articles = soup.find_all('article', class_='recent-abstract abstract-article')
    
    # Recorre cada artículo de la segunda sección para extraer la información
    for article in articles:
        # Título
        title_tag = article.find('h2', class_='abstract-title')
        title = title_tag.get_text(strip=True) if title_tag else "No title"
        
        # Enlace del artículo
        link = title_tag.find('a')['href'] if title_tag else "No link"
        
        # Asegura que el enlace sea completo
        if link and not link.startswith('http'):
            link = url + link
        
        # Categoría
        category_tag = article.find('a', class_='abstract-taxonomy')
        category = category_tag.get_text(strip=True) if category_tag else "No category"
        
        # Resumen
        summary_tag = article.find('div', class_='abstract-excerpt')
        summary = summary_tag.get_text(strip=True) if summary_tag else "No summary"
        
        # Comentarios
        comments_tag = article.find('span', class_='abstract-comment-count')
        comments = comments_tag.get_text(strip=True) if comments_tag else "No comments"
        
        # Fecha de publicación
        date_tag = article.find('time', class_='abstract-date')
        date = date_tag.get_text(strip=True) if date_tag else "No date"
        
        # Imprime los resultados de la segunda sección
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Category: {category}")
        print(f"Summary: {summary}")
        print(f"Comments: {comments}")
        print(f"Date: {date}")
        print("-" * 80)
        
        # Almacena la noticia en la lista
        noticias_info.append({
            'titulo': title,
            'link': link,
            'categoria': category,
            'resumen': summary,
            'comentarios': comments,
            'fecha': date
        })
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    return noticias_info


def obtener_noticias_scraping_2():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página (para la primera sección de noticias)
    articulos = soup.find_all('article', class_='hero-poster poster-article')
    
    # Lista para almacenar las noticias de la primera sección
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título y el enlace de cada noticia
        titulo = articulo.find('h2', class_='poster-title')
        if titulo:
            enlace = titulo.find('a')['href']
            if enlace and not enlace.startswith('http'):
                enlace = url + enlace  # Asegura que el enlace sea completo
            noticias_info.append({
                'titulo': titulo.text.strip(),
                'link': enlace,
                'img_url': 'https://img.remediosdigitales.com/3999ac/prop3-1/150_150.png'
            })
    
    # Encuentra todos los artículos en la página (para la segunda sección de noticias)
    articles = soup.find_all('article', class_='recent-abstract abstract-article')
    
    # Recorre cada artículo de la segunda sección para extraer la información
    for article in articles:
        # Título
        title_tag = article.find('h2', class_='abstract-title')
        title = title_tag.get_text(strip=True) if title_tag else "No title"
        
        # Enlace del artículo
        link = title_tag.find('a')['href'] if title_tag else "No link"
        
        # Asegura que el enlace sea completo
        if link and not link.startswith('http'):
            link = url + link
        
        # Extraer la imagen
        img_tag = articulo.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'https://img.remediosdigitales.com/3999ac/prop3-1/150_150.png'
        
        noticias_info.append({
            'titulo': title,
            'link': link,
            'img_url': img_url
        })

        # # Categoría
        # category_tag = article.find('a', class_='abstract-taxonomy')
        # category = category_tag.get_text(strip=True) if category_tag else "No category"
        
        # # Resumen
        # summary_tag = article.find('div', class_='abstract-excerpt')
        # summary = summary_tag.get_text(strip=True) if summary_tag else "No summary"
        
        # # Comentarios
        # comments_tag = article.find('span', class_='abstract-comment-count')
        # comments = comments_tag.get_text(strip=True) if comments_tag else "No comments"
        
        # # Fecha de publicación
        # date_tag = article.find('time', class_='abstract-date')
        # date = date_tag.get_text(strip=True) if date_tag else "No date"
        
        # # Imprime los resultados de la segunda sección
        # print(f"Title: {title}")
        # print(f"Link: {link}")
        # print(f"Category: {category}")
        # print(f"Summary: {summary}")
        # print(f"Comments: {comments}")
        # print(f"Date: {date}")
        # print("-" * 80)
        
        # # Almacena la noticia en la lista
        # noticias_info.append({
        #     'titulo': title,
        #     'link': link,
        #     'categoria': category,
        #     'resumen': summary,
        #     'comentarios': comments,
        #     'fecha': date
        # })
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    return noticias_info

def obtener_noticias_scraping_directo():
    noticias_guardadas = 0
    noticias_omitidas = 0
    url = "https://www.motorpasion.com"
    
    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para Motorpasion...")
            payload = {'api_key': scraperapi_key, 'url': url}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a Motorpasion...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)
        
        response.raise_for_status()

        # Guardar el HTML en archivo
        with open("pagina_guardada_motorpasion.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_motorpasion.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos
        articulos = soup.find_all('article', class_='recent-abstract abstract-article')

        for articulo in articulos:
            # Título
            title_tag = articulo.find('h2', class_='abstract-title')
            titulo = title_tag.get_text(strip=True) if title_tag else "No title"

            # Enlace
            link_tag = title_tag.find('a') if title_tag else None
            link = link_tag['href'] if link_tag else "No link"
            if link and not link.startswith('http'):
                link = url + link

            # Imagen
            picture_tag = articulo.find('picture')
            img_url = None

            if picture_tag:
                source_tag = picture_tag.find('source', media="(min-width: 767px)")
                if source_tag and 'srcset' in source_tag.attrs:
                    img_url = source_tag['srcset']

            if not img_url:
                img_tag = articulo.find('img')
                img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else \
                    'https://img.remediosdigitales.com/3999ac/prop3-1/150_150.png'

            # Guardar en la base de datos
            _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=link,
                img_url=img_url
            )
            if created:
                noticias_guardadas += 1
            else:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")
        
        
        

def obtener_noticias_scraping_directo_sinkey():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article', class_='recent-abstract abstract-article')

    # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0

    for articulo in articulos:
        # Título
        title_tag = articulo.find('h2', class_='abstract-title')
        titulo = title_tag.get_text(strip=True) if title_tag else "No title"
        
        # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     noticias_omitidas += 1
        #     continue

        # Enlace del artículo
        link_tag = title_tag.find('a') if title_tag else None
        link = link_tag['href'] if link_tag else "No link"

        # Asegura que el enlace sea completo
        if link and not link.startswith('http'):
            link = url + link
        
        # Imagen: intenta obtener la mejor calidad disponible en <source> o <img>
        picture_tag = articulo.find('picture')
        img_url = None

        if picture_tag:
            source_tag = picture_tag.find('source', media="(min-width: 767px)")
            if source_tag and 'srcset' in source_tag.attrs:
                img_url = source_tag['srcset']

        if not img_url:
            img_tag = articulo.find('img')
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'https://img.remediosdigitales.com/3999ac/prop3-1/150_150.png'

        # Guardar en la base de datos usando `get_or_create`
        titulo_truncado = titulo[:20] if len(titulo) > 20 else titulo
        titulo_truncado = titulo
        _, created = NoticiaDiferente.objects.get_or_create(
            titulo=titulo_truncado,
            link=link,
            img_url=img_url
        )

        if created:
            noticias_guardadas += 1
    
    driver.quit()
    print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")



def obtener_noticias_scraping():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario

    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article', class_='recent-abstract abstract-article')
    
    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Título
        title_tag = articulo.find('h2', class_='abstract-title')
        titulo = title_tag.get_text(strip=True) if title_tag else "No title"

         # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     continue  # Salta a la siguiente iteración
        
        # Enlace del artículo
        link_tag = title_tag.find('a') if title_tag else None
        link = link_tag['href'] if link_tag else "No link"
        
        # Asegura que el enlace sea completo
        if link and not link.startswith('http'):
            link = url + link
        
        # Imagen: intenta obtener la mejor calidad disponible en <source> o <img>
        picture_tag = articulo.find('picture')
        img_url = None
        
        if picture_tag:
            source_tag = picture_tag.find('source', media="(min-width: 767px)")
            if source_tag and 'srcset' in source_tag.attrs:
                img_url = source_tag['srcset']
        
        if not img_url:
            img_tag = articulo.find('img')
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'https://img.remediosdigitales.com/3999ac/prop3-1/150_150.png'
        
        # Almacena la información en la lista
        noticias_info.append({
            'titulo': titulo,
            'link': link,
            'img_url': img_url
        })
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    return noticias_info



def obtener_noticias_imdb():
    url = "https://www.imdb.com/chart/moviemeter/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find('table',  {'class': 'chart full-width'})

    rows = table.find_all('tr')

    movies = []

    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])



def obtener_noticias_scraping_carscoop():
    url = "https://www.carscoops.com"
    noticias_guardadas = 0
    noticias_omitidas = 0

    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para Carscoops...")
            payload = {'api_key': scraperapi_key, 'url': url}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a Carscoops...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        # Guardar el HTML en un archivo para debug
        with open("pagina_guardada_carscoops.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_carscoops.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos
        articulos = soup.find_all('div', class_='card-wrapper')

        for articulo in articulos:
            # Extraer título
            titulo_tag = articulo.find('h2', class_='title')
            titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

            # Enlace
            enlace_tag = articulo.find('a')
            enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
            if enlace and not enlace.startswith('http'):
                enlace = url + enlace

            # Imagen
            img_tag = articulo.find('img')
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else \
                'https://www.carscoops.com/wp-content/uploads/2022/12/Carscoops-Logo-White.jpg'

            # Guardar en DB
            _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )
            if created:
                noticias_guardadas += 1
            else:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")


            

def obtener_noticias_scraping_carscoop_sinkey():
    url = "https://www.carscoops.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_carscoops.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_carscoops.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(f"soup: {soup}")

    # Encuentra todos los artículos en la página (para la primera sección de noticias)
    articulos = soup.find_all('div', class_='card-wrapper')

     # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0
    
    # Lista para almacenar las noticias de la primera sección
    noticias_info = []
    
    # for articulo in articulos:
    #     # Extraer el título y el enlace de cada noticia
    #     titulo = articulo.find('h2', class_='title')
    #     print(f"Title: {titulo}")
        
    #     if titulo:
    #         enlace = articulo.find('a')['href']
    #         if enlace and not enlace.startswith('http'):
    #             #enlace = url + enlace  # Asegura que el enlace sea completo
    #             enlace = enlace  # Asegura que el enlace sea completo
    #             print(f"Link: {enlace}")
    #         # Extraer la imagen
    #         img_url = articulo.find('img')['src']
    #         #img_url = img_tag['src'] if img_tag else None
    #         noticias_info.append({
    #             'titulo': titulo.text.strip(),
    #             'link': enlace,
    #             'img_url': img_url
    #         })
    
    for articulo in articulos:
        # Extraer el título
        titulo_tag = articulo.find('h2', class_='title')
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

         # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     continue  # Salta a la siguiente iteración
        
        # Extraer el enlace
        enlace_tag = articulo.find('a')
        enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
        
        # Extraer la imagen
        img_tag = articulo.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'https://www.carscoops.com/wp-content/uploads/2022/12/Carscoops-Logo-White.jpg'
        
        # noticias_info.append({
        #     'titulo': titulo,
        #     'link': enlace,
        #     'img_url': img_url
        # })

        _, created = NoticiaDiferente.objects.get_or_create(
            titulo=titulo,
            link=enlace,
            img_url=img_url
        )

        if created:
            noticias_guardadas += 1

    driver.quit()
    print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")


    # Encuentra todos los artículos en la página (para la segunda sección de noticias)
    # articles = soup.find_all('article', class_='recent-abstract abstract-article')
    
    # # Recorre cada artículo de la segunda sección para extraer la información
    # for article in articles:
    #     # Título
    #     title_tag = article.find('h2', class_='abstract-title')
    #     title = title_tag.get_text(strip=True) if title_tag else "No title"
        
    #     # Enlace del artículo
    #     link = title_tag.find('a')['href'] if title_tag else "No link"
        
    #     # Asegura que el enlace sea completo
    #     if link and not link.startswith('http'):
    #         link = url + link
        
    #     # Categoría
    #     category_tag = article.find('a', class_='abstract-taxonomy')
    #     category = category_tag.get_text(strip=True) if category_tag else "No category"
        
    #     # Resumen
    #     summary_tag = article.find('div', class_='abstract-excerpt')
    #     summary = summary_tag.get_text(strip=True) if summary_tag else "No summary"
        
    #     # Comentarios
    #     comments_tag = article.find('span', class_='abstract-comment-count')
    #     comments = comments_tag.get_text(strip=True) if comments_tag else "No comments"
        
    #     # Fecha de publicación
    #     date_tag = article.find('time', class_='abstract-date')
    #     date = date_tag.get_text(strip=True) if date_tag else "No date"
        
    #     # Imprime los resultados de la segunda sección
    #     print(f"Title: {title}")
    #     print(f"Link: {link}")
    #     print(f"Category: {category}")
    #     print(f"Summary: {summary}")
    #     print(f"Comments: {comments}")
    #     print(f"Date: {date}")
    #     print("-" * 80)
        
    #     # Almacena la noticia en la lista
    #     noticias_info.append({
    #         'titulo': title,
    #         'link': link,
    #         'categoria': category,
    #         'resumen': summary,
    #         'comentarios': comments,
    #         'fecha': date
    #     })
    
    # driver.quit()
    
    # # Imprimir las noticias procesadas
    # print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    #return noticias_info


def obtener_noticias_scraping_insideevs():
    url = "https://insideevs.com/"
    noticias_guardadas = 0
    noticias_omitidas = 0

    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para InsideEVs...")
            payload = {'api_key': scraperapi_key, 'url': url}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a InsideEVs...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        # Guardar el HTML en archivo para debug
        with open("pagina_guardada_insideevs.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_insideevs.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos
        articulos = soup.find_all('article')

        for articulo in articulos:
            # Extraer título
            titulo_tag = articulo.find('h2')
            titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

            # Extraer enlace
            enlace_tag = articulo.find('a')
            enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None

            if enlace and enlace.startswith('/'):
                enlace = url + enlace.lstrip('/')

            # Extraer imagen
            img_tag = articulo.find('img')
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else \
                'https://cdn.motor1.com/images/static/insideevs/largetile.png'

            # Guardar en DB
            _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

            if created:
                noticias_guardadas += 1
            else:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")




def obtener_noticias_scraping_insideevs_sinkey():
    url = "https://insideevs.com/"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_insideevs.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_insideevs.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article')
    
     # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0

    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título
        titulo_tag = articulo.find('h2')
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

         # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     continue  # Salta a la siguiente iteración
        
        # Extraer el enlace
        enlace_tag = articulo.find('a')
        enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
        
        # Extraer la imagen
        img_tag = articulo.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'https://cdn.motor1.com/images/static/insideevs/largetile.png'
        
        # Verifica que el enlace es relativo y lo convierte a absoluto
        if enlace and enlace.startswith('/'):
            enlace = url + enlace.lstrip('/')
        
    #     noticias_info.append({
    #         'titulo': titulo,
    #         'link': enlace,
    #         'img_url': img_url
    #     }) 
    
    # driver.quit()
    
    # # Imprimir las noticias procesadas
    # print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    # return noticias_info

        _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

        if created:
            noticias_guardadas += 1

    driver.quit()
    print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")




def obtener_noticias_scraping_carmagazine_co_uk():
    url = "https://www.carmagazine.co.uk/car-news/"
    noticias_guardadas = 0
    noticias_omitidas = 0

    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para CarMagazine...")
            payload = {'api_key': scraperapi_key, 'url': url}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a CarMagazine...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        # Guardar HTML en archivo para depuración
        with open("pagina_guardada_carmagazine_co_uk.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_carmagazine_co_uk.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos
        articulos = soup.find_all('article', class_='panel')

        for articulo in articulos:
            # Extraer título
            titulo_tag = articulo.find('h3', class_='title')
            titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

            # Extraer enlace
            enlace_tag = titulo_tag.find('a') if titulo_tag else None
            enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None

            if enlace and enlace.startswith('/'):
                # Si empieza con /car-news/, eliminamos esa parte duplicada
                if enlace[1:].startswith('car-news/'):
                    enlace = url + enlace[1:].replace('car-news/', '', 1)
                else:
                    enlace = url + enlace.lstrip('/')

            # Extraer imagen
            img_url = 'https://car-images.bauersecure.com/wp-images/5079/480x270/jan25_01.jpg?quality=50'
            img_tag = articulo.find('a', class_='th')
            if img_tag:
                img = img_tag.find('img')
                if img:
                    if 'data-src' in img.attrs:
                        img_url = img['data-src']
                    elif 'src' in img.attrs:
                        img_url = img['src']

            # Guardar en DB
            _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

            if created:
                noticias_guardadas += 1
            else:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")




def obtener_noticias_scraping_carmagazine_co_uk_sinkey():
    url = "https://www.carmagazine.co.uk/car-news/"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_carmagazine_co_uk.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_carmagazine_co_uk.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article', class_='panel')

    # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0
    
    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título
        titulo_tag = articulo.find('h3', class_='title')
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"

         # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     continue  # Salta a la siguiente iteración
        
        # Extraer el enlace
        enlace_tag = titulo_tag.find('a') if titulo_tag else None
        enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
        
        # Extraer la imagen
        # Encuentra el <a> que contiene el <img>
        img_tag = articulo.find('a', class_='th')

        # Verifica si se encontró el <a> y si tiene un <img> dentro
        if img_tag:
            img = img_tag.find('img')
            if img and 'data-src' in img.attrs:
                img_url = img['data-src']
            else:
                img_url = 'https://car-images.bauersecure.com/wp-images/5079/480x270/jan25_01.jpg?quality=50'
        else:
            img_url = 'https://car-images.bauersecure.com/wp-images/5079/480x270/jan25_01.jpg?quality=50'

        print(f"El enlace de la imagen de Carmagazine es : {img_url} .")


        # Verifica que el enlace es relativo y lo convierte a absoluto
        # if enlace and enlace.startswith('/'):
        #     enlace = url + enlace.lstrip('/')
        #     print(f"El enlace de Carmagazine es : {enlace} .")

        if enlace and enlace.startswith('/'):
            # Verifica si el enlace ya tiene 'car-news' después del primer '/'
            if enlace[1:].startswith('car-news/'):
                # Si ya tiene 'car-news' al inicio, eliminamos el primer 'car-news/'
                enlace = url + enlace[1:].replace('car-news/', '', 1)
            else:
                # Si no tiene 'car-news' al inicio, simplemente agregamos la URL base
                enlace = url + enlace.lstrip('/')

            print(f"El enlace de Carmagazine es : {enlace} .")

    
        
    #     noticias_info.append({
    #         'titulo': titulo,
    #         'link': enlace,
    #         'img_url': img_url
    #     }) 
    
    # driver.quit()
    
    # # Imprimir las noticias procesadas
    # print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    # return noticias_info

        _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )
        
        if created:
            noticias_guardadas += 1
    
    driver.quit()
    print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")


def obtener_noticias_scraping_autocar_co_uk():
    url = "https://www.autocar.co.uk/"
    noticias_guardadas = 0
    noticias_omitidas = 0
    
    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para Autocar...")
            payload = {'api_key': scraperapi_key, 'url': url, 'render': 'true'}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a Autocar...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        # Guardar HTML en archivo para depuración
        with open("pagina_guardada_autocar_co_uk.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_autocar_co_uk.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos en Autocar
        articulos = soup.find_all('div', class_='views-row')

        for row in articulos:
            # Extraer enlace
            enlace = None
            a_tag = row.find('a', href=True)
            if a_tag:
                enlace = a_tag['href']
                if enlace.startswith("/"):
                    enlace = f"https://www.autocar.co.uk{enlace}"

            # Valor predeterminado para título
            titulo = "Título no disponible"

            # Caso 1: <h2 class="block-title">
            h2 = row.find('h2', class_='block-title')
            if h2:
                a_tag = h2.find('a')
                if a_tag and a_tag.get_text(strip=True):
                    titulo = a_tag.get_text(strip=True)

            # Caso 2: <div class="title">
            elif row.find('div', class_='title'):
                div_title = row.find('div', class_='title')
                a_tag = div_title.find('a')
                if a_tag and a_tag.get_text(strip=True):
                    titulo = a_tag.get_text(strip=True)

            # Caso 3: <a class="cover-link">
            else:
                cover_link = row.find('a', class_='cover-link')
                if cover_link and cover_link.get_text(strip=True):
                    titulo = cover_link.get_text(strip=True)

            # Extraer imagen
            img_url = 'https://www.autocar.co.uk/sites/autocar.co.uk/files/autocar_logo_150.jpg'
            img_tag = row.find('img', src=True)
            if img_tag:
                img_url = img_tag['src']

            # Guardar en DB
            _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

            if created:
                noticias_guardadas += 1
            else:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")





def obtener_noticias_scraping_autocar_co_uk_sinkey():
    
    # URL de la página de noticias de Autocar
    url = "https://www.autocar.co.uk/"

    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Abre la página
    driver.get(url)

    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario

    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_autocar_co_uk.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_autocar_co_uk.html'")

    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0

    # Encuentra todos los artículos de noticias
    #noticias = []
    articulos = soup.find_all('div', class_='views-row')
    for row in soup.find_all('div', class_='views-row'):
        # Extraer el enlace
        enlace = row.find('a', href=True)
        if enlace:
            enlace = enlace['href']
            # Si el enlace es relativo, lo convierte en absoluto
            if enlace.startswith("/"):
                enlace = f"https://www.autocar.co.uk{enlace}"

        # Valor predeterminado para el título
        titulo = "Título no disponible"

        # Caso 1: Buscar en <h2 class="block-title">
        h2 = row.find('h2', class_='block-title')
        if h2:
            a_tag = h2.find('a')  # Busca la etiqueta <a> dentro del <h2>
            if a_tag and a_tag.get_text(strip=True):  # Asegúrate de que exista texto
                titulo = a_tag.get_text(strip=True)
                 # Validación: Si el título es mayor a 100 caracteres, omitir el registro
                # if len(titulo) > 100:
                #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
                #     continue  # Salta a la siguiente iteración

        # Caso 2: Si no se encuentra en <h2>, buscar en <div class="title">
        elif row.find('div', class_='title'):
            div_title = row.find('div', class_='title')
            a_tag = div_title.find('a')  # Busca la etiqueta <a> dentro del <div>
            if a_tag and a_tag.get_text(strip=True):  # Asegúrate de que exista texto
                titulo = a_tag.get_text(strip=True)
                 # Validación: Si el título es mayor a 100 caracteres, omitir el registro
                # if len(titulo) > 100:
                #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
                #     continue  # Salta a la siguiente iteración

        # Caso 3: Buscar en <a class="cover-link"> (nuevo caso)
        else:
            cover_link = row.find('a', class_='cover-link')
            if cover_link and cover_link.get_text(strip=True):  # Asegúrate de que exista texto
                titulo = cover_link.get_text(strip=True)
                 # Validación: Si el título es mayor a 100 caracteres, omitir el registro
                # if len(titulo) > 100:
                #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
                #     continue  # Salta a la siguiente iteración



        # Extraer la categoría
        categoria = row.find('div', class_='category')
        if categoria:
            categoria = categoria.get_text(strip=True)

        # Extraer la fecha
        fecha = row.find('div', class_='pub-date')
        if fecha:
            fecha = fecha.get_text(strip=True)

        # Extraer la URL de la imagen
        # img_tag = row.find('img', src=True)
        # img_url = img_tag['src'] if img_tag else 'https://www.autocar.co.uk/sites/autocar.co.uk/files/autocar_logo_150.jpg'

        # Extraer la URL de la imagen
        img_tag = row.find('img', src=True)  # Busca una etiqueta <img> con el atributo src
        if img_tag:
            img_url = img_tag['src']  # Obtén la URL de la imagen encontrada
        else:
            # No hay imagen en este artículo, asignar una imagen predeterminada
            img_url = 'https://www.autocar.co.uk/sites/autocar.co.uk/files/autocar_logo_150.jpg'


    #     # Almacena la noticia en un diccionario
    #     noticia = {
    #         'titulo': titulo,
    #         'link': enlace,
    #         'img_url': img_url
    #     }
    #     noticias.append(noticia)

    #     print(f"Título: {titulo}, Enlace: {enlace}")

    # # Cierra el navegador
    # driver.quit()

    # # Devuelve la lista de noticias
    # return noticias

        _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

        if created:
            noticias_guardadas += 1

    driver.quit()
    print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")


# Ejemplo de uso
# noticias = obtener_noticias_scraping_autocar_co_uk()
# for noticia in noticias:
#     print(noticia)


def obtener_noticias_scraping_autonews0():
    
    # URL de la página de noticias de Autocar
    url = "https://www.autonews.com/"

    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Abre la página
    driver.get(url)

    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario

    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_autonews.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_autonews.html'")

    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Lista para almacenar noticias
    noticias = []

    # Itera sobre todos los bloques relevantes en la página
    for row in soup.find_all('div', class_='views-row'):
        # Extraer el título y el enlace
        enlace_tag = row.find('a', href=True)
        if enlace_tag:
            titulo = enlace_tag.get_text(strip=True)
            enlace = enlace_tag['href']
            # Si el enlace es relativo, conviértelo en absoluto
            if enlace.startswith("/"):
                enlace = f"https://www.autonews.com{enlace}"
        else:
            titulo = "Título no disponible"
            enlace = None

        # Extraer la URL de la imagen
        img_tag = row.find('img', src=True)
        if img_tag:
            img_url = img_tag['src']
        else:
            # Imagen predeterminada si no hay imagen en el artículo
            img_url = 'https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87'

        # Almacenar los datos en un diccionario
        noticia = {
            'titulo': titulo,
            'link': enlace,
            'img_url': img_url
        }
        noticias.append(noticia)

    # Cierra el navegador
    driver.quit()

    # Devuelve la lista de noticias
    return noticias




def obtener_noticias_scraping_autonews():
    url = "https://www.autonews.com/"
    noticias_guardadas = 0
    noticias_omitidas = 0
    
    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)

    try:
        if scraperapi_key:
            print("Usando ScraperAPI para Autonews...")
            payload = {'api_key': scraperapi_key, 'url': url, 'render': 'true'}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a Autonews...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        # Guardar HTML en archivo para depuración
        with open("pagina_guardada_autonews.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_autonews.html'")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Encuentra artículos en Autonews
        articulos = soup.find_all('a', {'data-testid': 'header-story-title'})

        for bloque in articulos:
            # Extraer título
            titulo = bloque.get_text(strip=True).replace("Title", "", 1)

            # Extraer enlace
            enlace = bloque['href']
            if enlace.startswith("/"):
                enlace = f"https://www.autonews.com{enlace}"

            # Buscar imagen relacionada
            img_url = "https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87"
            imagen_div = bloque.find_next('div', class_='u-w-full md:u-pt-0 u-order-1 md:u-order-2')
            img_tag = imagen_div.find('img', src=True) if imagen_div else None

            if not img_tag:
                contenedor_relacionado = bloque.find_next('div', class_='u-shrink-0')
                if contenedor_relacionado:
                    img_tag = contenedor_relacionado.find('img', src=True)

            if not img_tag:
                img_tag = bloque.find('img', src=True)

            if img_tag:
                img_url = img_tag['src']

            # Guardar en DB
            try:
                _, created = NoticiaDiferente.objects.get_or_create(
                    titulo=titulo,
                    link=enlace,
                    img_url=img_url
                )
                if created:
                    noticias_guardadas += 1
                else:
                    noticias_omitidas += 1
            except IntegrityError:
                noticias_omitidas += 1

        print(f"Noticias procesadas: {len(articulos)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el scraping: {e}")
        
        
        


def obtener_noticias_scraping_autonews_sinkey():
    
    # URL de la página de noticias de Autocar
    url = "https://www.autonews.com/"

    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Abre la página
    driver.get(url)

    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)

    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_autonews.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_autonews.html'")

    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Contador para estadísticas
    noticias_guardadas = 0
    noticias_omitidas = 0

    # Lista para almacenar noticias
    noticias = []

    # Encuentra los bloques de noticias
    bloques = soup.find_all('a', {'data-testid': 'header-story-title'})
    for bloque in bloques:
        # Extraer el título
        titulo = bloque.get_text(strip=True)
        titulo = titulo.replace("Title", "", 1)  # Reemplaza solo la primera ocurrencia de "Title"
         # Validación: Si el título es mayor a 100 caracteres, omitir el registro
        # if len(titulo) > 100:
        #     print(f"Noticia omitida: Título demasiado largo -> {titulo}")
        #     continue  # Salta a la siguiente iteración

        # Extraer el enlace
        enlace = bloque['href']
        if enlace.startswith("/"):
            enlace = f"https://www.autonews.com{enlace}"

        # # Buscar el contenedor de la imagen relacionado
        # imagen_div = bloque.find_next('div', class_='u-w-full md:u-pt-0 u-order-1 md:u-order-2')
        # img_tag = imagen_div.find('img', src=True) if imagen_div else None
        # img_url = img_tag['src'] if img_tag else 'https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87'

        # # Intentar encontrar la imagen relacionada
        # img_tag = None

        # # Caso 1: La imagen está en un contenedor relacionado
        # contenedor_relacionado = bloque.find_next('div', class_='u-shrink-0')
        # if contenedor_relacionado:
        #     img_tag = contenedor_relacionado.find('img', src=True)

        # # Caso 2: La imagen está dentro del enlace actual
        # if not img_tag:
        #     img_tag = bloque.find('img', src=True)

        # # Obtener la URL de la imagen, si existe
        # img_url = img_tag['src'] if img_tag else 'https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87'


        # # Buscar el contenedor de la imagen relacionado
        # imagen_div = bloque.find_next('div', class_='u-w-full md:u-pt-0 u-order-1 md:u-order-2')
        # img_tag = imagen_div.find('img', src=True) if imagen_div else None

        # # Si no encuentra la imagen en el primer contenedor, intenta con otro contenedor relacionado
        # if not img_tag:
        #     contenedor_relacionado = bloque.find_next('div', class_='u-shrink-0')
        #     if contenedor_relacionado:
        #         img_tag = contenedor_relacionado.find('img', src=True)

        # # Si tampoco encuentra la imagen en un contenedor relacionado, busca dentro del enlace actual
        # if not img_tag:
        #     img_tag = bloque.find('img', src=True)

        # # Obtener la URL de la imagen, si existe, o usar un valor predeterminado
        # img_url = img_tag['src'] if img_tag else 'https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87'


        # Buscar el contenedor de la imagen relacionado dentro del artículo
        imagen_div = bloque.find_next('div', class_='u-w-full md:u-pt-0 u-order-1 md:u-order-2')
        img_tag = imagen_div.find('img', src=True) if imagen_div else None

        # Si no encuentra la imagen en el primer contenedor, intenta con otro contenedor relacionado
        if not img_tag:
            contenedor_relacionado = bloque.find_next('div', class_='u-shrink-0')
            if contenedor_relacionado:
                img_tag = contenedor_relacionado.find('img', src=True)

        # Si tampoco encuentra la imagen en un contenedor relacionado, busca dentro del enlace actual
        if not img_tag:
            img_tag = bloque.find('img', src=True)

        # # Verificar si el contenedor pertenece al artículo actual para evitar duplicados
        # if img_tag:
        #     # Buscar el contenedor padre más cercano del bloque actual
        #     contenedor_padre = img_tag.find_parent('div', class_='u-flex')
        #     if contenedor_padre and contenedor_padre != bloque:
        #         img_tag = None  # Descartar la imagen si pertenece a otro artículo

        # Obtener la URL de la imagen o usar un valor predeterminado
        img_url = img_tag['src'] if img_tag else 'https://www.autonews.com/pf/resources/images/logos/default/default.svg?d=87'



    #     # Agregar la noticia a la lista
    #     noticia = {
    #         'titulo': titulo,
    #         'link': enlace,
    #         'img_url': img_url
    #     }
    #     noticias.append(noticia)

    # # Cierra el navegador
    # driver.quit()

    # # Devuelve la lista de noticias
    # return noticias

        _, created = NoticiaDiferente.objects.get_or_create(
                titulo=titulo,
                link=enlace,
                img_url=img_url
            )

        if created:
            noticias_guardadas += 1

    driver.quit()
    print(f"Noticias procesadas: {len(bloques)} | Guardadas: {noticias_guardadas} | Omitidas: {noticias_omitidas}")




def obtener_noticias_scraping_carmagazine_co_uk1():
    url = "https://www.carmagazine.co.uk/car-news/"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_carmagazine_co_uk.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_carmagazine_co_uk.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article')
    
    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título
        titulo_tag = articulo.find('h2')
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"
        
        # Extraer el enlace
        enlace_tag = articulo.find('a')
        enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
        
        # Extraer la imagen
        img_tag = articulo.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
        
        # Verifica que el enlace es relativo y lo convierte a absoluto
        if enlace and enlace.startswith('/'):
            enlace = url + enlace.lstrip('/')
        
        noticias_info.append({
            'titulo': titulo,
            'link': enlace,
            'img_url': img_url
        }) 
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    return noticias_info





def obtener_noticias_scraping_insideevs_0():
    url = "https://insideevs.com/"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_insideevs.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada_insideevs.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encuentra todos los artículos en la página (basado en el nuevo HTML)
    articulos = soup.find_all('article', class_='md:grid-bottom-first')
    
    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título
        titulo_tag = articulo.find('h2')
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"
        
        # Extraer el enlace
        enlace_tag = articulo.find('a')
        enlace = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else None
        
        # Extraer la imagen
        img_tag = articulo.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
        
        # Verifica que el enlace es relativo y lo convierte a absoluto
        if enlace and enlace.startswith('/'):
            enlace = url + enlace.lstrip('/')
        
        noticias_info.append({
            'titulo': titulo,
            'link': enlace,
            'img_url': img_url
        }) 
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {len(noticias_info)} noticias.")
    
    return noticias_info


def obtener_noticias_scrapingNoFUnciona():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Imprime el HTML para inspección
    # print(soup.prettify())  # Puedes activar esto si necesitas ver el HTML completo
    
    # Encuentra todos los artículos en la página
    articulos = soup.find_all('article', class_='hero-poster poster-article')
    
    # Lista para almacenar las noticias
    noticias_info = []
    
    for articulo in articulos:
        # Extraer el título y el enlace de cada noticia
        titulo = articulo.find('h2', class_='poster-title')
        if titulo:
            enlace = titulo.find('a')['href']
            if enlace and not enlace.startswith('http'):
                enlace = url + enlace  # Asegura que el enlace sea completo
            noticias_info.append({
                'titulo': titulo.text.strip(),
                'link': enlace
            })
    
        # Encuentra todos los artículos de noticias
    articles = soup.find_all('article', class_='recent-abstract abstract-article')

# Recorre cada artículo para extraer la información
    for article in articles:
        # Título
        title_tag = article.find('h2', class_='abstract-title')
        title = title_tag.get_text(strip=True) if title_tag else "No title"
        
        # Enlace del artículo
        link = title_tag.find('a')['href'] if title_tag else "No link"
        
        # Categoría
        category_tag = article.find('a', class_='abstract-taxonomy')
        category = category_tag.get_text(strip=True) if category_tag else "No category"
        
        # Resumen
        summary_tag = article.find('div', class_='abstract-excerpt')
        summary = summary_tag.get_text(strip=True) if summary_tag else "No summary"
        
        # Comentarios
        comments_tag = article.find('span', class_='abstract-comment-count')
        comments = comments_tag.get_text(strip=True) if comments_tag else "No comments"
        
        # Fecha de publicación
        date_tag = article.find('time', class_='abstract-date')
        date = date_tag.get_text(strip=True) if date_tag else "No date"
        
        # Imprime los resultados
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Category: {category}")
        print(f"Summary: {summary}")
        print(f"Comments: {comments}")
        print(f"Date: {date}")
        print("-" * 80)
    
    driver.quit()
    
    # Imprimir las noticias procesadas
    print(f"Noticias procesadas: {noticias_info}")
    
    return noticias_info





def obtener_noticias_scraping8():
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    # Abre la página
    driver.get(url)
    
    # Espera unos segundos para asegurarse de que todo el contenido se haya cargado
    time.sleep(5)  # Ajusta el tiempo según sea necesario
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("HTML guardado correctamente en 'pagina_guardada.html'")
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Imprime el HTML para inspección
    print(soup.prettify())
    
    # Encuentra las noticias (ajusta según el HTML actual)
    noticias = soup.find_all('h2', class_='title')
    print(f"Noticias encontradas: {noticias}")
    
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })
    
    driver.quit()
    
    print(f"Noticias procesadas: {noticias_info}")
    return noticias_info





def obtener_noticias_scraping7():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    url = "https://www.motorpasion.com"
    
    # Configura el navegador en modo sin cabeza (headless)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    
    # Obtén el contenido de la página después de cargar JavaScript
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Imprime el HTML para inspección
    print(soup.prettify())
    
    noticias = soup.find_all('h2', class_='title')  # Ajusta según el HTML actual
    print(f"Noticias encontradas: {noticias}")
    
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })
    
    driver.quit()
    
    print(f"Noticias procesadas: {noticias_info}")
    return noticias_info




def obtener_noticias_scraping6():
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://www.motorpasion.com"
    response = requests.get(url)
    
    print(f"Respuesta HTTP: {response.status_code}")
    
    if response.status_code != 200:
        return []  # Si la respuesta no es exitosa, regresa una lista vacía
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Imprime todo el HTML para inspección
    #print(soup.prettify())  # Esto muestra el HTML formateado
    
    # Ajusta el selector si es necesario
    #noticias = soup.find_all('h2', class_='title')  # Ajusta según sea necesario
    noticias = soup.find_all('a', class_='card__title')  # Ajusta el selector según la estructura
    
    print(f"Noticias encontradas: {noticias}")  # Verifica cuántas noticias se encuentran
    
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link  # Asegúrate de que el enlace sea absoluto
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })
    
    print(f"Noticias procesadas: {noticias_info}")  # Verifica qué noticias se están guardando
    return noticias_info





def obtener_noticias_scraping5():
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://www.motorpasion.com"
    response = requests.get(url)
    
    print(f"Respuesta HTTP: {response.status_code}")
    
    if response.status_code != 200:
        return []  # Si la respuesta no es exitosa, regresa una lista vacía
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Imprime todo el HTML para inspección
    print(soup.prettify())  # Esto muestra el HTML formateado
    
    noticias = soup.find_all('h2', class_='title')  # Ajusta según sea necesario
    print(f"Noticias encontradas: {noticias}")  # Verifica cuántas noticias se encuentran
    
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link  # Asegúrate de que el enlace sea absoluto
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })
    
    print(f"Noticias procesadas: {noticias_info}")  # Verifica qué noticias se están guardando
    return noticias_info


def obtener_noticias_scraping4():
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://www.motorpasion.com"
    response = requests.get(url)
    
    print(f"Respuesta HTTP: {response.status_code}")
    
    if response.status_code != 200:
        return []  # Si la respuesta no es exitosa, regresa una lista vacía
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Imprime todo el HTML para inspección
    print(soup.prettify())  # Esto muestra el HTML formateado
    
    # Después de inspeccionar el HTML, ajusta el código para buscar las noticias correctamente
    noticias = soup.find_all('h2', class_='title')  # Ajusta según sea necesario
    print(f"Noticias encontradas: {noticias}")
    
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link  # Asegúrate de que el enlace sea absoluto
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })
    
    return noticias_info



def obtener_noticias_scraping1():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.motorpasion.com"
    response = requests.get(url)
    
    print(f"Respuesta HTTP: {response.status_code}")  # Imprime el código de estado
    if response.status_code != 200:
        return []  # Si la respuesta no es exitosa, regresa una lista vacía
    
    soup = BeautifulSoup(response.content, 'html.parser')
    noticias = soup.find_all('h2', class_='title')
    print(f"Noticias encontradas: {noticias}")
    
    return [{'titulo': noticia.text.strip(), 'link': noticia.a['href']} for noticia in noticias if noticia.a]

def obtener_noticias_scraping2():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.motorpasion.com"
    response = requests.get(url)
    
    print(f"Respuesta HTTP: {response.status_code}")
    
    if response.status_code != 200:
        return []  # Si la respuesta no es exitosa, regresa una lista vacía
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Verifica si los elementos están dentro de un div, ul o alguna otra estructura
    noticias = soup.find_all('h2', class_='title')  # Cambia esto según lo que encuentres en la página
    print(f"Noticias encontradas: {noticias}")
    
    # Si la página contiene otros elementos de noticias, usa un selector adecuado
    noticias_info = []
    for noticia in noticias:
        link = noticia.a['href'] if noticia.a else None
        if link and not link.startswith('http'):
            link = url + link  # Asegúrate de que el enlace sea absoluto
        noticias_info.append({
            'titulo': noticia.text.strip(),
            'link': link
        })

    return noticias_info

