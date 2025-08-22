from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from datetime import datetime
import locale
from django.core.mail import send_mail
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
import json
from .forms import CommentForm,NewsletterForm,ContactMessageForm,CommentMotorpasionForm, CommentCarscoopsForm, CommentAutonewsForm, CommentAutocarForm, CommentCarmagazineForm, CommentInsideevsForm,CommentBuscarNoticiasForm, CommentIMDBForm
from .models import Comment,Noticia, NoticiaDiferente,CommentMotorpasion,CommentCarscoops, CommentInsideevs, CommentAutocar, CommentAutonews, CommentCarmagazine,CommentBuscarNoticias, CommentIMDB, FeaturedNews
from django.http import JsonResponse
import time
from django.db.models import Q
from django.contrib import messages
from django.core.management import call_command
from django.conf import settings


# Create your views here.


def featured_slider(request):
    featured = FeaturedNews.objects.order_by("-date")[:10]  # últimas 10 noticias
    return render(request, "cars_reviews_better_app/todos_mis_proyectos.html", {"featured": featured})

def todos_mis_proyectos(request):
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    context = {'fecha_hora_actual': fecha_hora_actual}
    return render(request, 'cars_reviews_better_app/todos_mis_proyectos.html', context)

def populate_noticias(request):
    try:
        call_command('populate_noticias')  # Nombre de tu comando
        return JsonResponse({'message': 'El scraping se completó correctamente.'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def buscar_noticias(request):
    query = request.GET.get('q', '')  # Captura el término de búsqueda
    if not query:  # Si el texto de búsqueda está vacío
        return redirect('home')  # Cambia 'home' al nombre de tu URL para la página de inicio

    resultados = []
    if query:
        resultados = NoticiaDiferente.objects.filter(
            Q(titulo__icontains=query) | Q(link__icontains=query)
        )
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentBuscarNoticiasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('buscar_noticias')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentBuscarNoticiasForm()
    
    comments = CommentBuscarNoticias.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'query': query, 'resultados': resultados}
    
    return render(request, 'cars_reviews_better_app/buscar_noticias.html', context)

def set_cookie_consent(request):
    response = JsonResponse({'status': 'ok'})
    response.set_cookie('cookie_consent', 'true', max_age=365*24*60*60)  # 1 año
    return response

def privacy_policy(request):
    return render(request, 'cars_reviews_better_app/privacy_policy.html')


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Guarda el email en la base de datos
            subscription = form.save(commit=False)
            email = subscription.email
            form.save()
            # Envía un correo de confirmación
            send_mail(
                'Subscription Confirmed',
                'Thank you for subscribing to our newsletter! with your email: ' + email,
                email,  # Email del remitente
                [email,'msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com', 'msb.caixa@gmail.com'],
            )
            
            # Muestra un mensaje de éxito
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')  # Redirige para evitar el reenvío de formularios

        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, 'Please provide a valid email.')

    else:
        form = NewsletterForm()  # Cargar un formulario vacío en caso de GET

    return render(request, 'cars_reviews_better_app/home.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Guardar el registro en la base de datos
            form.save()

            # Obtener los datos del formulario
            message_name = form.cleaned_data['name']
            message_email = form.cleaned_data['email']
            message_subject = form.cleaned_data['subject']
            message_message = form.cleaned_data['message']
            
            """
            # Enviar el correo electrónico
            send_mail(
                'Message from ' + message_name,  # Asunto
                message_message,  # Mensaje
                message_email,  # Correo electrónico del remitente
                ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],  # Correos de destino
            )
            """
            email_content = f"""
            You have received a new contact message from {message_name}:

            Name: {message_name}
            Email: {message_email}
            Subject: {message_subject}
            Message: {message_message}
            """
            
            # Enviar el correo electrónico
            send_mail(
                f'Message from {message_name}',  # Asunto
                email_content,  # Cuerpo del correo con todos los detalles
                message_email,  # Correo electrónico del remitente
                [message_email,'msb.caixa@gmail.com','msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],  # Correos de destino
            )

            return render(request, 'cars_reviews_better_app/contact.html', {'message_name': message_name})
    else:
        form = ContactMessageForm()

    return render(request, 'cars_reviews_better_app/contact.html', {'form': form})

def lista_noticias(request):
    #noticias = Noticia.objects.order_by('-fecha_creacion')
    noticias_diferentes = NoticiaDiferente.objects.order_by('-fecha_creacion')
    
    name = request.user.username
    # set pagination
    
    p = Paginator(noticias_diferentes, 8)
    page = request.GET.get('page')
    todas_noticias_diferentes = p.get_page(page)
    nums = "a" * todas_noticias_diferentes.paginator.num_pages
    nums = range(1, todas_noticias_diferentes.paginator.num_pages + 1)  # Rango dinámico para las páginas

            
    print("hola : " + str(todas_noticias_diferentes.paginator.num_pages))

    return render(request, 'cars_reviews_better_app/listar_noticias.html', {'noticias_diferentes': noticias_diferentes,  'todas_noticias_diferentes' : todas_noticias_diferentes})


def cars_reviews_admin_view(request):
    context = {'form': ''}
    return render(request, 'cars_reviews_better_app/cars_reviews_admin.html',context )

def motorpasion_view(request):
    # noticias = obtener_noticias_scraping()
    # #Guarda las noticias de Motorpasion en la base de datos
    # for noticia in noticias:
    #     print(f"Guardando noticia de Motorpasion: {noticia['titulo']}")  # Imprime para depurar
    #     NoticiaDiferente.objects.get_or_create(
    #             titulo=noticia['titulo'],
    #             link=noticia['link'],
    #             img_url=noticia['img_url']
    #         )
    noticias = NoticiaDiferente.objects.filter(link__icontains='motorpasion').order_by('-fecha_creacion')
    print(f"Noticias encontradas: {noticias.count()}")  # Debe imprimir 18
    for noticia in noticias:
        print(f"Título: {noticia.titulo}")
        print(f"Link: {noticia.link}")
        print(f"Imagen: {noticia.img_url}")
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentMotorpasionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('motorpasion')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentMotorpasionForm()
    
    comments = CommentMotorpasion.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}

    return render(request, 'cars_reviews_better_app/motorpasion.html', context)

def carscoops_view(request):
    #noticias = obtener_noticias_scraping_carscoop()
    noticias = NoticiaDiferente.objects.filter(link__icontains='carscoops').order_by('-fecha_creacion')
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentCarscoopsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carscoops')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentCarscoopsForm()
    
    comments = CommentCarscoops.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}
    return render(request, 'cars_reviews_better_app/carscoops.html', context)


def insideevs_view(request):
    #noticias = obtener_noticias_scraping_insideevs()
    noticias = NoticiaDiferente.objects.filter(link__icontains='insideevs').order_by('-fecha_creacion')
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentInsideevsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('insideevs')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentInsideevsForm()
    
    comments = CommentInsideevs.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}
    return render(request, 'cars_reviews_better_app/insideevs.html', context)

def carmagazine_view(request):
    #noticias = obtener_noticias_scraping_carmagazine_co_uk()
    noticias = NoticiaDiferente.objects.filter(link__icontains='carmagazine').order_by('-fecha_creacion')
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentCarmagazineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carmagazine')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentCarmagazineForm()
    
    comments = CommentCarmagazine.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}
    return render(request, 'cars_reviews_better_app/carmagazine.html', context)

def autocar_view(request):
    #noticias = obtener_noticias_scraping_autocar_co_uk()
    noticias = NoticiaDiferente.objects.filter(link__icontains='autocar').order_by('-fecha_creacion')
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentAutocarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autocar')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentAutocarForm()
    
    comments = CommentAutocar.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}
    return render(request, 'cars_reviews_better_app/autocar.html', context)

def autonews_view(request):
    #noticias = obtener_noticias_scraping_autonews()
    noticias = NoticiaDiferente.objects.filter(link__icontains='autonews').order_by('-fecha_creacion')
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentAutonewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autonews')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentAutonewsForm()
    
    comments = CommentAutonews.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'noticias': noticias}
    return render(request, 'cars_reviews_better_app/autonews.html', context)

def single_view(request):
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('single_view')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentForm()
    
    comments = Comment.objects.order_by('-created_at')  
    context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form}
    return render(request, 'cars_reviews_better_app/single.html',context )

def category_view(request):
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {'fecha_hora_actual': fecha_hora_actual}
    return render(request, 'cars_reviews_better_app/category.html',context )

def custom_logout_view(request):
    logout(request)
    return redirect('home') 






def home_imdb_web(request):
    movies = []
    error_message = None
    
    scraperapi_key = getattr(settings, 'SCRAPERAPI_KEY', None)
    url = 'https://www.imdb.com/es-es/chart/moviemeter/'
    
    try:
        if scraperapi_key:
            print("Usando ScraperAPI...")
            payload = {'api_key': scraperapi_key, 'url': url}
            response = requests.get('https://api.scraperapi.com/', params=payload)
        else:
            print("No se encontró la clave de ScraperAPI, haciendo petición directa a IMDb...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=headers)
        
        response.raise_for_status()
        
        # --- LÍNEA AÑADIDA PARA VER EL HTML COMPLETO ---
        print("--- INICIO DE CONTENIDO HTML RECIBIDO ---")
        #print(response.text)
        # Guarda el HTML de la página en un archivo
        with open("pagina_guardada_imdb_web.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML guardado correctamente en 'pagina_guardada_imdb_web.html'")
        print("--- FIN DE CONTENIDO HTML RECIBIDO ---")
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        script_tag = soup.find("script", type="application/ld+json")
        
        if script_tag:
            imdb_data = json.loads(script_tag.string)
            
            for item in imdb_data.get("itemListElement", []):
                movie_data = item.get("item", {})
                movies.append({
                    "title": movie_data.get("name", "Sin título"),
                    "url": movie_data.get("url", ""),
                    "description": movie_data.get("description", "Sin descripción"),
                    "image": movie_data.get("image", ""),
                    "rating": movie_data.get("aggregateRating", {}).get("ratingValue", "N/A"),
                    "genre": movie_data.get("genre", "N/A"),
                    "duration": movie_data.get("duration", "N/A"),
                })
        else:
            error_message = "No se encontró la información JSON de películas."
            
    except requests.exceptions.RequestException as e:
        error_message = f"Error de conexión: {e}"
    except json.JSONDecodeError:
        error_message = "Error al analizar los datos JSON de IMDb."
    except Exception as e:
        error_message = f"Ocurrió un error inesperado durante el scraping: {e}"

    if request.method == 'POST':
        form = CommentIMDBForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autonews')
    else:
        form = CommentIMDBForm()
    
    p = Paginator(movies, 3)
    page = request.GET.get('page')
    todas_movies = p.get_page(page)
    nums = "a" * todas_movies.paginator.num_pages
    nums = range(1, todas_movies.paginator.num_pages + 1)  # Rango dinámico para las páginas
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    
    context = {
        'todas_movies': todas_movies,
        'fecha_hora_actual': fecha_hora_actual,
        'comments': CommentIMDB.objects.order_by('-created_at'),
        'form': form,
        'nums': nums,
        'name': request.user.username if request.user.is_authenticated else 'Invitado',
        'error': error_message
    }

    return render(request, "cars_reviews_better_app/noticias.html", context)



def home_imdb_web1(request):
    movies = []
    error_message = None
    
    # Intenta obtener la clave de API desde los settings.py
    # En PythonAnywhere, esta clave se leerá de una variable de entorno.
    # En tu entorno local, puedes tenerla en el settings.py o en un archivo .env.
    scrape_do_key = getattr(settings, 'SCRAPEDO_KEY', None)
    
    if scrape_do_key:
        # Lógica para PythonAnywhere: Usar Scrape.do
        print("Usando Scrape.do...")
        api_url = f"https://api.scrape.do/?url=https://www.imdb.com/es-es/chart/moviemeter/&token={scrape_do_key}"
        request_url = api_url
    else:
        # Lógica para entorno local: Petición directa a IMDb
        print("Usando petición directa a IMDb...")
        request_url = "https://www.imdb.com/es-es/chart/moviemeter/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    
    try:
        response = requests.get(request_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        script_tag = soup.find("script", type="application/ld+json")

        if not script_tag:
            error_message = "No se encontró la información JSON de películas."
        else:
            imdb_data = json.loads(script_tag.string)

            for item in imdb_data.get("itemListElement", []):
                movie = item.get("item", {})
                movies.append({
                    "title": movie.get("name", "Sin título"),
                    "url": movie.get("url", ""),
                    "description": movie.get("description", "Sin descripción"),
                    "image": movie.get("image", ""),
                    "rating": movie.get("aggregateRating", {}).get("ratingValue", "N/A"),
                    "genre": movie.get("genre", "N/A"),
                    "duration": movie.get("duration", "N/A"),
                })
    
    except requests.exceptions.RequestException as e:
        error_message = f"Error de conexión: {e}"
    except json.JSONDecodeError:
        error_message = "Error al analizar los datos de IMDb."
    except Exception as e:
        error_message = f"Ocurrió un error inesperado: {e}"
    
    if request.method == 'POST':
        form = CommentIMDBForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autonews')
    else:
        form = CommentIMDBForm()

    
    
    p = Paginator(movies, 3)
    page = request.GET.get('page')
    todas_movies = p.get_page(page)
    nums = "a" * todas_movies.paginator.num_pages
    nums = range(1, todas_movies.paginator.num_pages + 1)  # Rango dinámico para las páginas
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    
    context = {
        'movies': todas_movies,
        'fecha_hora_actual': fecha_hora_actual,
        'comments': CommentIMDB.objects.order_by('-created_at'),
        'form': form,
        'nums': nums,
        'name': request.user.username if request.user.is_authenticated else 'Invitado',
        'error': error_message
    }

    return render(request, "cars_reviews_better_app/noticias.html", context)

def home_imdb(request):
    url = "https://www.imdb.com/es-es/chart/moviemeter/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.get(url, headers=headers)

    # Verifica si la respuesta fue exitosa
    if response.status_code != 200:
        return render(request, "cars_reviews_better_app/noticias.html", {
            'movies': [],
            'error': f"Error al acceder a IMDb: {response.status_code}."
        })
    
    # Guarda el HTML de la página en un archivo
    with open("pagina_guardada_imdb.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("HTML guardado correctamente en 'pagina_guardada_imdb.html'")

    soup = BeautifulSoup(response.content, "html.parser")

     # Buscar el bloque que contiene el JSON con los datos
    script_tag = soup.find("script", type="application/ld+json")
    if not script_tag:
        return render(request, "cars_reviews_better_app/noticias.html", {
            'movies': [],
            'error': "No se encontró información relevante en IMDb."
        })
    
    # Imprimir el contenido del script para inspección
    print(script_tag.string)

    # Analizar el JSON contenido en el script
    try:
        imdb_data = json.loads(script_tag.string)
    except json.JSONDecodeError:
        return render(request, "cars_reviews_better_app/noticias.html", {
            'movies': [],
            'error': "Error al analizar los datos de IMDb."
        })
    

    # Extraer información relevante
    movies = []
    for item in imdb_data.get("itemListElement", []):
        movie = item.get("item", {})
        title = movie.get("name", "Sin título")
        url = movie.get("url", "")
        description = movie.get("description", "Sin descripción")
        image = movie.get("image", "")
        rating = movie.get("aggregateRating", {}).get("ratingValue", "N/A")
        genre = movie.get("genre", "N/A")
        duration = movie.get("duration", "N/A")
        movie_type = movie.get("@type", "N/A")  # Accede al campo @type

        movies.append({
            "title": title,
            "url": url,
            "description": description,
            "image": image,
            "rating": rating,
            "genre": genre,
            "duration": duration,
            "type": movie_type,  # Añadir @type al diccionario
        })
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p')
    if request.method == 'POST':
        form = CommentIMDBForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autonews')  # Cambia 'comments' por el nombre de tu URL
    else:
        form = CommentIMDBForm()
    
    comments = CommentIMDB.objects.order_by('-created_at')  
    #context = {'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'movies': movies}

    name = request.user.username
    # set pagination
    
    p = Paginator(movies, 3)
    page = request.GET.get('page')
    todas_movies = p.get_page(page)
    nums = "a" * todas_movies.paginator.num_pages
    nums = range(1, todas_movies.paginator.num_pages + 1)  # Rango dinámico para las páginas

            
    print("hola : " + str(todas_movies.paginator.num_pages))
    
    context = {'todas_movies': todas_movies, 'fecha_hora_actual': fecha_hora_actual, 'comments':comments, 'form':form, 'movies': movies, 'nums': nums, 'name':name}

    return render(request, "cars_reviews_better_app/noticias.html", context)

def home(request):
    fecha_actual = datetime.now().strftime('%A, %B %d, %Y')  # Ejemplo: Monday, January 01, 2045
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configura a español
        fecha_actual_es = datetime.now().strftime('%A, %d de %B de %Y') 
    except locale.Error:
        # Si no se puede establecer el locale, usa un formato alternativo
        fecha_actual_es = datetime.now().strftime('%A, %d of %B of %Y')
    
    fecha_hora_actual = datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p') 
    context = {
        'fecha_actual': fecha_actual,
        'fecha_actual_es': fecha_actual_es,
        'fecha_hora_actual': fecha_hora_actual
    }
    return render(request, 'cars_reviews_better_app/home.html', context)