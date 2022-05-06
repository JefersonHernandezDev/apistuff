from operator import truediv
from typing import Optional

from fastapi import FastAPI
from screens import screens
from destacados import destacados
from custom_screens import getCustomScreens
from seciones import destacados_data
from content import content

app = FastAPI()


@app.get("/")
def read_root():
    return {"adunitid": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo", "adunitidios": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo", "busqueda": [{"url": "https://servicios.site/tva/AztecaEnVivo2019/busqueda.php?buscar={[PARAMETROBUSCAR]}", "screenname": "pantalla_busqueda"}], "datos": [{"adunitid": "inicio-seccion", "adunitidios": "inicio-seccion", "firebase_seccion": "Inicio", "tituloselcolor": "#f8f809", "titulo": "Inicio", "firebase_screen": "inicio-Destacados", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/destacados", "firebasescreen": "inicio-Destacados"}, {"adunitid": "realities-seccion", "adunitidios": "realities-seccion", "firebase_seccion": "Realities", "tituloselcolor": "#f8f809", "titulo": "Realities", "firebase_screen": "inicio-realities", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/realities", "firebasescreen": "inicio-realities"}, {"adunitid": "novelas-seccion", "adunitidios": "novelas-seccion", "firebase_seccion": "Novelas", "tituloselcolor": "#f8f809", "titulo": "Novelas", "firebase_screen": "inicio-novelas", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/novelas", "firebasescreen": "inicio-novelas"}, {"adunitid": "programas-seccion", "adunitidios": "programas-seccion", "firebase_seccion": "Programas", "tituloselcolor": "#f8f809", "titulo": "Programas", "firebase_screen": "inicio-programas", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/programas", "firebasescreen": "inicio-programas"}, {"adunitid": "cine-seccion", "adunitidios": "cine-seccion", "firebase_seccion": "Cine", "tituloselcolor": "#f8f809", "titulo": "Cine", "firebase_screen": "cine-seccion", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/cine", "firebasescreen": "cine-seccion"}, {"adunitid": "a-mas-seccion", "adunitidios": "a-mas-seccion", "firebase_seccion": "a más +", "tituloselcolor": "#f8f809", "titulo": "a más +", "firebase_screen": "inicio-a+7.2", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/envivo2020/amastv", "firebasescreen": "inicio-a+7.2"}, {"adunitid": "series-seccion", "adunitidios": "series-seccion", "firebase_seccion": "Series", "tituloselcolor": "#f8f809", "titulo": "Series", "firebase_screen": "inicio-series", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/series", "firebasescreen": "inicio-series"}, {"adunitid": "kidsiete-seccion", "adunitidios": "kidsiete-seccion", "firebase_seccion": "KidSiete", "tituloselcolor": "#f8f809", "titulo": "KidSiete", "firebase_screen": "inicio-kidsiete", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/kidsiete", "firebasescreen": "inicio-kidsiete"}, {"adunitid": "es-mucho-mas-seccion", "adunitidios": "es-mucho-mas-seccion", "firebase_seccion": "Es mucho más", "tituloselcolor": "#f8f809", "titulo": "Es mucho más", "firebase_screen": "es-mucho-mas-seccion", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/deportes-esmuchomas", "firebasescreen": "es-mucho-mas-seccion"}, {"adunitid": "interactua-seccion", "adunitidios": "interactua-seccion", "firebase_seccion": "Interactúa", "tituloselcolor": "#f8f809", "titulo": "Interactúa", "firebase_screen": "interactua-seccion", "firebase_tipo": "Inicio", "titulounselcolor": "#ffffff", "tipo": "Inicio", "contenido": "https://www.tvazteca.com/envivo2020/seccion/interactua", "firebasescreen": "interactua-seccion"}], "envivo": {"liveswitch": {"videoinicial": "http://mdstrm.com/video/deprecado.mp4", "tipo": "En vivo", "firebasescreen": "En vivo", "vast": "https://pubads.g.doubleclick.net/gampad/live/ads?iu=/29782907/Apps-Azteca/App-Envivo-2020/EnVivo&description_url=&url=&env=vp&impl=s&tfcd=0&npa=0&gdfp_req=1&output=vast&sz=640x480&unviewed_position_start=1&ad_rule=1&correlator=", "cartas": [{"programa": "", "firebase_video": "", "icono": "https://tvazteca.brightspotcdn.com/dims4/default/4d24aac/2147483647/strip/true/crop/512x341+0+85/resize/300x200!/quality/90/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F87%2Fa7%2F41466180494a863ef1f4aca5d7f0%2Fazteca-uno-cuadrado-2.png", "url": "https://www.tvazteca.com/envivo2020/epg/aztecauno", "id": "1038", "firebase_seccion": "", "vast": "https://pubads.g.doubleclick.net/gampad/live/ads?iu=/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Azteca-Uno&description_url=&url=&env=vp&impl=s&tfcd=0&npa=0&gdfp_req=1&output=vast&sz=640x480&unviewed_position_start=1&ad_rule=1&correlator=", "firebase_screen": "En vivo-AztecaUNO-Programacion", "firebase_tipo": "En vivo", "firebase_canal": "AztecaUNO", "firebase_videoaviso": "En vivo", "firebase_programa": "", "firebasescreen": "En vivo-AztecaUNO-Programacion"}, {"programa": "", "firebase_video": "", "icono": "https://tvazteca.brightspotcdn.com/dims4/default/3f214b3/2147483647/strip/true/crop/1620x1080+150+0/resize/300x200!/quality/90/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F5d%2Fac%2F3199ed5e4f8cbc52ea2f4a29acce%2Flogo7blanco1.png", "url": "https://www.tvazteca.com/envivo2020/epg/a7", "adunitid": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Azteca-7", "firebase_seccion": "", "id": "1037", "adunitidios": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Azteca-7", "vast": "https://pubads.g.doubleclick.net/gampad/live/ads?iu=/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Azteca-7&description_url=&url=&env=vp&impl=s&tfcd=0&npa=0&gdfp_req=1&output=vast&sz=640x480&unviewed_position_start=1&ad_rule=1&correlator=", "firebase_screen": "En vivo-Azteca7-Programacion", "firebase_canal": "Azteca7", "firebase_tipo": "En vivo", "firebase_videoaviso": "En vivo", "firebase_programa": "", "firebasescreen": "En vivo-Azteca7-Programacion"}, {"programa": "", "firebase_video": "", "icono": "https://tvazteca.brightspotcdn.com/dims4/default/52d3eed/2147483647/strip/true/crop/512x341+0+85/resize/300x200!/quality/90/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F7e%2Ff8%2F26a32c8943a999981121de5f9771%2Flogoamas-app-vivo.png", "url": "https://www.tvazteca.com/envivo2020/epg/amas", "adunitid": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Amas-TV", "firebase_seccion": "", "id": "1040", "adunitidios": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Amas-TV", "vast": "https://pubads.g.doubleclick.net/gampad/live/ads?iu=/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/Amas-TV&description_url=&url=&env=vp&impl=s&tfcd=0&npa=0&gdfp_req=1&output=vast&sz=640x480&unviewed_position_start=1&ad_rule=1&correlator=", "firebase_screen": "En vivo-amás+-Programacion", "firebase_canal": "amás+", "firebase_tipo": "En vivo", "firebase_videoaviso": "En vivo", "firebase_programa": "", "firebasescreen": "En vivo-amás+-Programacion"}, {"programa": "", "firebase_video": "", "icono": "https://tvazteca.brightspotcdn.com/dims4/default/1448897/2147483647/strip/true/crop/512x341+0+85/resize/300x200!/quality/90/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F58%2F74%2F8f13538947b7a5e8a0c8989612e1%2Fadn-40-512x512-color-02.png", "url": "https://tv-azteca-brightspot.s3-us-west-1.amazonaws.com/program_schedule/ADN40FeedEPG.json", "adunitid": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/ADN-40", "firebase_seccion": "", "id": "1039", "adunitidios": "/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/ADN-40", "vast": "https://pubads.g.doubleclick.net/gampad/live/ads?iu=/29782907/Apps-Azteca/App-Envivo-2020/EnVivo/ADN-40&description_url=&url=&env=vp&impl=s&tfcd=0&npa=0&gdfp_req=1&output=vast&sz=640x480&unviewed_position_start=1&ad_rule=1&correlator=", "firebase_screen": "En vivo-ADN40-Programacion", "firebase_canal": "ADN40", "firebase_tipo": "En vivo", "firebase_videoaviso": "En vivo", "firebase_programa": "", "firebasescreen": "En vivo-ADN40-Programacion"}], "EPG": "https://www.tvazteca.com/envivo2020/epg/all"}, "EPG": {"firebase_screen": "En vivo", "firebasescreen": "En vivo", "screenname": "En vivo", "firebase_tipo": "En vivo"}}}


@app.get("/screens")
def read_item():
    return {
        "screens": getCustomScreens()
    }


@app.get("/seccion/{name}")
def read_item(name: str):
    if name == "programas":
        # destacados = {"uno": {"el": "el"}, "dos": {}}
        datos = destacados["datos"]
        for element in datos:
            #temp = datos[element]
            element["isFavoryte"] = True
            element["isFavoryte"] = True
            element["isFavoryte"] = True
            #datos[element] = temp
        return {"datos": datos}
    elif name == "destacados":
        return destacados_data.data
    # elif name == "section_to_navigate_envivo":
    #    return {}
    else:
        return {}


@app.get("/content/{name}")
def read_item(name: str):
    if name == "section_to_navigate_envivo":
        return content.enVivoCarrouselItems
    elif name == "section_to_navigate_logos_programas":
        return content.logosProgrmas
    elif name == "es_mucho_mas":
        return content.progrmasRecomendados
    elif name == "programas_recomendados":
        return content.progrmasRecomendados
    elif name == "realities":
        return content.progrmasRecomendados
    elif name == "programas":
        return content.progrmasRecomendados
    elif name == "novelas":
        return content.progrmasRecomendados
    elif name == "a_mas":
        return content.progrmasRecomendados
    elif name == "series":
        return content.progrmasRecomendados
    elif name == "cine":
        return content.progrmasRecomendados
    elif name == "kit_siete":
        return content.progrmasRecomendados
    return content.data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
