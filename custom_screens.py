import enum

from enums import Seccion, AuthLevel, Screen


available = [
    {"title": "Inicio", "tabBarItem": "Inicio",
        "seccion": Seccion.DESTACADOS, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Realities", "tabBarItem": "Inicio",
        "seccion": Seccion.REALITIES, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Novelas", "tabBarItem": "Inicio",
        "seccion": Seccion.NOVELAS, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Programas", "tabBarItem": "Inicio",
        "seccion": Seccion.PROGRAMAS, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Cine", "tabBarItem": "Inicio",
        "seccion": Seccion.CINE, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "A mas +", "tabBarItem": "Inicio",
        "seccion": Seccion.AMAS, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Series", "tabBarItem": "Inicio",
        "seccion": Seccion.SERIES, "screenType": Screen.VIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "KidSiete", "tabBarItem": "Inicio",
        "seccion": Seccion.KIDSIETE, "screenType": Screen.WEBVIEW, "authLevel": AuthLevel.PUBLIC},
    {"title": "Es mucho mas", "tabBarItem": "Inicio",
        "seccion": Seccion.ESMUCHOMAS, "screenType": Screen.WEBVIEW, "authLevel": AuthLevel.PUBLIC}
]


def getCustomScreens():
    #available = []

    # for i in range(10):
    #    available.append({"title": f"Title {i}", "tabBarItem": "Inicio", "provider": "destacados", "screentype"})
    return available
