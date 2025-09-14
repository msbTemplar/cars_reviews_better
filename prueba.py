import requests

agencias = [
    {"nombre": "Bayt Al Fajr Travel", "pais": "España", "web": "https://alfajrtravel.com"},
        {"nombre": "UmraSpain", "pais": "España", "web": "https://umraspain.com"},
        {"nombre": "Rawahel Travel Spain", "pais": "España", "web": "https://rawahelspain.com"},
        {"nombre": "HajjSpain", "pais": "España", "web": "https://hajjspain.com/en"},
        {"nombre": "Almisk Travel", "pais": "España/Europa", "web": "https://umrah-desde.com"},
        #{"nombre": "RIHAB TRAVEL", "pais": "España", "web": "https://www.cylex.es/madrid/rihab-travel-s-l---hajj-y-umrah-desde-espa%C3%B1a---madrid--barcelona--m%C3%A1laga--13541763.html"},
        {"nombre": "Meca Travel S.L.U", "pais": "España", "web": "https://mecatravel.info"},
        {"nombre": "Rifada Travel", "pais": "Marruecos/España", "web": "https://rifadatravel.com"},
        {"nombre": "HajjMaroc", "pais": "Marruecos", "web": "https://hajjmaroc.com/es"},
        {"nombre": "Nour Viajes y Eventos", "pais": "España/Marruecos", "web": "https://nourviajesyeventos.com"},
        # ✅ Nuevas agencias añadidas
        {"nombre": "Umra Y Hajj S.L", "pais": "Ceuta (España)", "web": "https://empresite.eleconomista.es/UMRA-HAJJ.html"},
        #{"nombre": "Rihab Travel Melilla Umrah & Hajj", "pais": "Melilla (España)", "web": "https://laromerosa.es/rihab-travel-melilla-umrah-hajj/"},
        {"nombre": "Alburak Travel", "pais": "España", "web": "https://alburaktravel.com"},
        {"nombre": "Turismo Marruecos", "pais": "España/Marruecos", "web": "https://viajesmarruecos.com/nosotros/"},
        {"nombre": "Bint Batuta Travel", "pais": "España", "web": "https://bintbatutatravel.com"},
        # ✅ Nuevas agencias de Hajj y Umrah añadidas
        {"nombre": "Bizana Viajes", "pais": "España", "web": "https://bizanaviajes.es"},
        {"nombre": "Adyafa Travel", "pais": "España", "web": "https://adyafatravel.com"},
        {"nombre": "Mansiki Travel", "pais": "Marruecos", "web": "https://manasiki.ma/es/"},
        # ✅ Nuevas agencias encontradas
        {"nombre": "Malik Travel", "pais": "España", "web": "https://www.maliktravel.net"},
        {"nombre": "Agora Travel", "pais": "España", "web": "https://agoratravel.net"},
        {"nombre": "Go Mon Tours", "pais": "España", "web": "https://gomontours.com"},
        #{"nombre": "Oubadi Travel", "pais": "Marruecos", "web": "https://oubaditravel.com"},
        # ✅ Agencias recién añadidas
        {"nombre": "Haima Experience", "pais": "Marruecos", "web": "https://www.haimaexperience.com"},
        {"nombre": "Xaluca Tours", "pais": "Marruecos", "web": "https://xalucatours.com"},
        {"nombre": "Abdou Voyages", "pais": "Marruecos", "web": "https://manasiki.ma"},
        {"nombre": "Oubadi Travel", "pais": "Marruecos", "web": "https://oubaditravel.com"},
        #{"nombre": "Dallah Viajes", "pais": "España", "web": "https://www.dallahviajes.com"},
        # ✅ Nuevas agencias añadidas
        #{"nombre": "Hajjea", "pais": "España", "web": "https://hajjea.es"},
        #{"nombre": "Viajes A Mecca", "pais": "España", "web": "https://viajesamecca.com"},
        #{"nombre": "Umra Europa", "pais": "España/Europa", "web": "https://umraeuropa.es"},
        {"nombre": "Al-Andalus Viajes", "pais": "España", "web": "https://alandalustours.es"},
        {"nombre": "Viajes RIHAB TRAVEL", "pais": "España", "web": "https://umrah.es/es"},
        {"nombre": "Bakkah Travel", "pais": "España", "web": "https://bakkahtravel.com"},
        {"nombre": "Masar Travel", "pais": "Marruecos", "web": "https://mastravel.es"},
        {"nombre": "Haj.ma", "pais": "Marruecos", "web": "https://hajj.ma"},
]

for agencia in agencias:
    try:
        response = requests.get(agencia["web"], timeout=10)
        if response.status_code == 200:
            print(f"✅ {agencia['nombre']} ({agencia['web']}) --> OK")
        else:
            print(f"⚠️ {agencia['nombre']} ({agencia['web']}) --> {response.status_code}")
    except Exception as e:
        print(f"❌ {agencia['nombre']} ({agencia['web']}) --> ERROR: {e}")
