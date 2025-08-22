from django.core.management.base import BaseCommand
from cars_reviews_better_app.models import Noticia, NoticiaDiferente  # Asegúrate de importar el modelo
from cars_reviews_better_app.scraper import obtener_noticias_scraping, obtener_noticias_scraping_carscoop, obtener_noticias_scraping_insideevs
from cars_reviews_better_app.scraper import obtener_noticias_scraping_carmagazine_co_uk, obtener_noticias_scraping_autocar_co_uk
from cars_reviews_better_app.scraper import obtener_noticias_scraping_autonews , obtener_noticias_scraping_directo  # Importa tu función de scraping

# cars_reviews_app/management/commands/populate_noticias.py

class Command(BaseCommand):
    help = 'Obtiene noticias desde Motorpasion y las guarda en la base de datos'

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando scraping de Motorpasion...")
        
        # Llama a la función para realizar el scraping y guardar en la BD
        obtener_noticias_scraping_directo()
        obtener_noticias_scraping_carscoop()
        obtener_noticias_scraping_insideevs()
        obtener_noticias_scraping_carmagazine_co_uk()
        obtener_noticias_scraping_autocar_co_uk()
        obtener_noticias_scraping_autonews()


        
        self.stdout.write(self.style.SUCCESS('Proceso completado: Noticias guardadas correctamente.'))


""" class Command_antigua(BaseCommand):
    help = 'Obtiene noticias desde Motorpasion y Carscoops, y las guarda en la base de datos'

    def handle(self, *args, **kwargs):
        # Llamar a la función de scraping de Motorpasion
        noticias_motorpasion = obtener_noticias_scraping()  
        print(f"Noticias obtenidas de Motorpasion: {noticias_motorpasion}")  # Imprime las noticias obtenidas de Motorpasion
        
        # Llamar a la función de scraping de Carscoops
        noticias_carscoop = obtener_noticias_scraping_carscoop()  
        print(f"Noticias obtenidas de Carscoops: {noticias_carscoop}")  # Imprime las noticias obtenidas de Carscoops

         # Llamar a la función de scraping de Carscoops
        noticias_insideves = obtener_noticias_scraping_insideevs()  
        print(f"Noticias obtenidas de Insideves: {noticias_insideves}")  # Imprime las noticias obtenidas de Carscoops

        noticias_carmagazine_co_uk = obtener_noticias_scraping_carmagazine_co_uk()  
        print(f"Noticias obtenidas de Carmagazine_co_uk: {noticias_carmagazine_co_uk}")  # Imprime las noticias obtenidas de Carscoops

        noticias_autocar_co_uk = obtener_noticias_scraping_autocar_co_uk()  
        print(f"Noticias obtenidas de Noticias_autocar_co_uk: {noticias_autocar_co_uk}")  # Imprime las noticias obtenidas de Carscoops

        noticias_autonews = obtener_noticias_scraping_autonews()  
        print(f"Noticias obtenidas de Noticias_autonews: {noticias_autonews}")  # Imprime las noticias obtenidas de Carscoops
        
        # #Guarda las noticias de Motorpasion en la base de datos
        # for noticia in noticias_motorpasion:
        #     print(f"Guardando noticia de Motorpasion: {noticia['titulo']}")  # Imprime para depurar
        #     Noticia.objects.get_or_create(
        #         titulo=noticia['titulo'],
        #         link=noticia['link']
        #     )

        #Guarda las noticias de Motorpasion en la base de datos
        # for noticia in noticias_motorpasion:
        #     print(f"Guardando noticia de Motorpasion: {noticia['titulo']}")  # Imprime para depurar
        #     NoticiaDiferente.objects.get_or_create(
        #         titulo=noticia['titulo'],
        #         link=noticia['link'],
        #         img_url=noticia['img_url']
        #     )
        
        for noticia in noticias_motorpasion:
            print(f"Guardando noticia de Motorpasion: {noticia['titulo']}")  # Para depurar
            
            # Truncar el título si excede los 100 caracteres
            titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
            
            NoticiaDiferente.objects.get_or_create(
                titulo=titulo_truncado,
                link=noticia['link'],
                img_url=noticia['img_url']
            )

        # Guarda las noticias de Carscoops en la base de datos
        for noticia in noticias_carscoop:
            print(f"Guardando noticia de Carscoops: {noticia['titulo']}")  # Imprime para depurar
            titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
            NoticiaDiferente.objects.get_or_create(
                titulo=titulo_truncado, #noticia['titulo'],
                link=noticia['link'],
                img_url=noticia['img_url']
            )

        # Guarda las noticias de Carscoops en la base de datos
        for noticia in noticias_insideves:
            print(f"Guardando noticia de Insideeves: {noticia['titulo']}")  # Imprime para depurar
            titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
            NoticiaDiferente.objects.get_or_create(
                titulo=titulo_truncado, #noticia['titulo'],
                link=noticia['link'],
                img_url=noticia['img_url']
            )
        
        # Guarda las noticias de Carscoops en la base de datos
        for noticia in noticias_carmagazine_co_uk:
            print(f"Guardando noticia de Carmagazine_co_uk: {noticia['titulo']}")  # Imprime para depurar
            titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
            NoticiaDiferente.objects.get_or_create(
                titulo=titulo_truncado, #noticia['titulo'],
                link=noticia['link'],
                img_url=noticia['img_url']
            )

        # Guarda las noticias de Carscoops en la base de datos
        # for noticia in noticias_autocar_co_uk:
        #     print(f"Guardando noticia de Autocar_co_uk: {noticia['titulo']}")  # Imprime para depurar
        #     NoticiaDiferente.objects.get_or_create(
        #         titulo=noticia['titulo'],
        #         link=noticia['link'],
        #         img_url=noticia['img_url']
        #     )

        for noticia in noticias_autocar_co_uk:
            if noticia['titulo'] and noticia['link']:
                print(f"Guardando noticia de Autocar_co_uk: {noticia['titulo']}")  # Imprime para depurar
                titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
                NoticiaDiferente.objects.get_or_create(
                    titulo=titulo_truncado, #noticia['titulo'],
                    link=noticia['link'],
                    img_url=noticia.get('img_url')
                )
            else:
                print(f"Noticia omitida por datos incompletos: {noticia}")
        
        for noticia in noticias_autonews:
            if noticia['titulo'] and noticia['link']:
                print(f"Guardando noticia de Autonews: {noticia['titulo']}")  # Imprime para depurar
                titulo_truncado = noticia['titulo'][:20] if len(noticia['titulo']) > 20 else noticia['titulo']
                NoticiaDiferente.objects.get_or_create(
                    titulo=titulo_truncado, #noticia['titulo'],
                    link=noticia['link'],
                    img_url=noticia.get('img_url')
                )
            else:
                print(f"Noticia omitida por datos incompletos: {noticia}")


        # Mensaje de éxito
        self.stdout.write(self.style.SUCCESS('Noticias de Motorpasion y Carscoops guardadas correctamente y Insideeves.'))


class Commandold(BaseCommand):
    help = 'Obtiene noticias desde Motorpasion y las guarda en la base de datos'

    def handle(self, *args, **kwargs):
        noticias = obtener_noticias_scraping()  # Llama a la función de scraping
        print(f"Noticias obtenidas: {noticias}")  # Imprime las noticias obtenidas

        # Guarda las noticias en la base de datos
        for noticia in noticias:
            print(f"Guardando noticia: {noticia['titulo']}")  # Imprime para depurar
            Noticia.objects.get_or_create(
                titulo=noticia['titulo'],
                link=noticia['link']
            )
        self.stdout.write(self.style.SUCCESS('Noticias guardadas correctamente.')) """




