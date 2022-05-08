# MOCKUP PARA LA SECCION DESTACADOS (VISTA PRINCIPAL EN LA SECCION INICIO DE LA APLICAION)

import enum

from enums import Seccion, AuthLevel, Screen, Action, Component

API = "http://127.0.0.1:8000/"


children = [
    {
        "title": "MasterChef Celebrity",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.BANNER_PRINCIPAL,
        "content": "provider_required_by_action",
        "askForLogin": False
    },
    {
        "title": "En Vivo Ahora",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_LIVE,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "Interactua",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": "json_file_with_data.json",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_CUADRADO,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.ADS_CONTAINER,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS RECOMENDADOS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "REALITIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": "json_file_with_data.json",
        "askForLogin": False
    },
    {
        "title": "NOVELAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "A MAS +",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "SERIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": "json_file_with_data.json",
        "askForLogin": False
    },
    {
        "title": "CINE",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": "section_to_navigate",
        "askForLogin": False
    }
]

enVivoCarrouselItems = [
    {
        "title": "La Academia",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "live",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False,
    },
    {
        "title": "Hasta que la plata nos separe",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "live",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "La loba",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "live",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False},
    {
        "title": "La Resolana",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "interactua",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    }
]

data = {"children": children}

logosProgrmas = [
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "provider_by_action",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E/FFFFFF?text=MasterChef",
        "askForLogin": False,
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "provider_by_action",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E/FFFFFF?text=Venga+La+Alegria",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "provider_by_action",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E/FFFFFF?text=TQF",
        "askForLogin": False},
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": "provider_by_action",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E/FFFFFF?text=Exatlon+Mexico",
        "askForLogin": False
    }
]

progrmasRecomendados = [
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": f"{API}child_data/exatlon",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E",
        "askForLogin": False,
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": f"{API}child_data/el_origen",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": f"{API}child_data/nada_personal",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E",
        "askForLogin": False},
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": f"{API}child_data/mastercheft",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NAVIGATE,
        "componentType": Component.CHILD,
        "content": f"{API}child_data/la_voz",
        "thumbnail": "https://via.placeholder.com/150x150/D7385E",
        "askForLogin": False
    }
]
