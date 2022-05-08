import enum

from enums import Seccion, AuthLevel, Screen, Action, Component

API = "http://127.0.0.1:8000/"

destacadosList = [
    {
        "title": "MasterChef Celebrity",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.BANNER_PRINCIPAL,
        "content": "provider_required_by_action",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "En Vivo Ahora",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_LIVE,
        "content": f"{API}content/section_to_navigate_envivo",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "Interactua",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "content": f"{API}webview/interactua",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_CUADRADO,
        "content":  f"{API}content/section_to_navigate_logos_programas",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS RECOMENDADOS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/programas_recomendados",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "REALITIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/realities",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/programas",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "NOVELAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/novelas",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "A MAS +",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/a_mas",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "SERIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/series",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "CINE",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/cine",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "Continuar Viendo",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_LANDSCAPE_WITH_ACTION,
        "content": "provider_required_by_action",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "KIT SIETE",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/kit_siete",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    },
    {
        "title": "ES MUCHO MAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/es_mucho_mas",
        "thumbnail": "https://via.placeholder.com/300x150/D7385E/FFFFFF?text=Thumbnail",
        "askForLogin": False
    }
]

data = {"components": destacadosList}
