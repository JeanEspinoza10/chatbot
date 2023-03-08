
# Identificar el mensaje del usuario #
import re

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
                "body": "Hola, buenas tardes. Puede brindarnos los siguientes datos: \n 1) Nombres \n 2)apellidos \n 3)Correo"
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
    # Buscando el nombre
    patron_nombre = r"1\) (.*)\n"
    nombre = re.search(patron_nombre, text).group(1)
    # Buscar los apellidos
    patron_apellidos = r"2\) (.*)\n"
    apellidos = re.search(patron_apellidos, text).group(1)

    # Buscar el correo
    patron_correo = r"3\) (.*)"
    correo = re.search(patron_correo, text).group(1)
    # Grabar en la base de datos
    print(text)
    respuesta = "Gracias, por la informacion. Desea saber la lista de Menus"
    data = TextFormatMessage(respuesta, number)

