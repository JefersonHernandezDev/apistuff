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
        "askForLogin": False
    },
    {
        "title": "En Vivo Ahora",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_LIVE,
        "content": f"{API}content/section_to_navigate_envivo",
        "askForLogin": False
    },
    {
        "title": "Interactua",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_CUADRADO,
        "content": "section_to_navigate_logos_programas",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS RECOMENDADOS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/programas_recomendados",
        "askForLogin": False
    },
    {
        "title": "REALITIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/realities",
        "askForLogin": False
    },
    {
        "title": "PROGRAMAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/programas",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "askForLogin": False
    },
    {
        "title": "NOVELAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/novelas",
        "askForLogin": False
    },
    {
        "title": "A MAS +",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/a_mas",
        "askForLogin": False
    },
    {
        "title": "SERIES",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/series",
        "askForLogin": False
    },
    {
        "title": "",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.OPEN_WEB_VIEW,
        "componentType": Component.ADS_CONTAINER,
        "content": f"{API}webview/interactua",
        "askForLogin": False
    },
    {
        "title": "CINE",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/cine",
        "askForLogin": False
    },
    {
        "title": "Continuar Viendo",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_LANDSCAPE_WITH_ACTION,
        "content": "provider_required_by_action",
        "askForLogin": False
    },
    {
        "title": "KIT SIETE",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/kit_siete",
        "askForLogin": False
    },
    {
        "title": "ES MUCHO MAS",
        "authLevel": AuthLevel.PUBLIC,
        "action": Action.NONE,
        "componentType": Component.CARROUSEL_HORIZONTAL_PORTRAIT,
        "content": f"{API}content/es_mucho_mas",
        "askForLogin": False
    }
]

data = {"components": destacadosList}
