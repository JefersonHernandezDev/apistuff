import enum

from enums import Seccion, AuthLevel, Screen

API = "http://127.0.0.1:8000/"

available = [
    {
        "title": "Inicio",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/destacados",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Realities",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/realities",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Novelas",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/novelas",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Programas",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/programas",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Cine",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/cine",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "A mas +",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/amas",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Series",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/series",
        "screenType": Screen.VIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "KidSiete",
        "tabBarItem": "Inicio",
        "seccion": f"{API}seccion/kidsiete",
        "screenType": Screen.WEBVIEW,
        "authLevel": AuthLevel.PUBLIC
    },
    {
        "title": "Es mucho mas",
        "tabBarItem": "Inicio",
        "seccion":  f"{API}seccion/es_mucho_mas",
        "screenType": Screen.WEBVIEW,
        "authLevel": AuthLevel.PUBLIC
    }
]


def getCustomScreens():
    return available
