
# Identificar el mensaje del usuario #
import re
from grabardatos import Grabardatos
grabar = Grabardatos

def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    if typeMessage == "text":
        text = (message["text"])["body"]
        

    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print("sin mensaje")
    
    return text




def TextMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "to": number,
        "text": {
            "body": "Buenos tardes, usted tiene algun problema con su cuenta de red"
        },
        "type": "text"
}
    
    return data


def TextPresentacion(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "Hola, buenas tardes. Puede brindarnos los siguientes datos: 1) Nombres"
                }
        }
    
    return data



def TextFormatMessage(text, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"{text}"
                }
        }
    return data



def Buttons(number):
    data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "{number}",
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": ""
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "<UNIQUE_BUTTON_ID_1>",
                        "title": "<BUTTON_TITLE_1>"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "<UNIQUE_BUTTON_ID_2>",
                        "title": "<BUTTON_TITLE_2>"
                    }
                }
            ]
        }
    }
}
    return data

def listaMenu(number):
    data =  {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}

    
    return data

def ObteniendoDatosdeusuario(text, number):
    
    if "1" in text:
        nombre = text.replace("1)","")
        usuario = grabar.create(name=nombre)
        valor = "2) apellidos"
    if "2" in text:
        apellidos = text.replace("2)", "")
        valor ="3) correo"
    if "3" in text:
        correo = text.replace("3)", "")
        usuariocorreo = grabar.createcorreo(correo=correo)
        valor = ""
    
    # if usuario is not None and  usuariocorreo is not None:
    #     # Llamar a grabar en base de datos
    #     print(usuario, usuariocorreo)
    #     print("Se grabo correctamente")

    # Grabar en la base de datos
    if valor:
        respuesta = f"Puede brindar {valor} "
        data = TextFormatMessage(respuesta, number)
    else:
        respuesta = "Gracias por la informacion brindada"
        data = TextFormatMessage(respuesta, number)
    return data
