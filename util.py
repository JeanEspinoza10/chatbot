
# Identificar el mensaje del usuario #

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
                "body": "Hola, buenas tardes. Desea recibir el menu de hoy:"
                }
        }
    return data

def TextFormatMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "Por favor, brindarme su cuenta de red: "
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
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Tienes estos platos para el dia de hoy"
            },
            "footer": {
                "text": "Seleciona una opcion"
            },
            "action": {
                "button": "Mirar las opciones",
                "sections": [
                    {
                        "title": "Categoria de productos",
                        "rows": [
                            {
                                "id": "001",
                                "title": "Traer datos de la base de datos",
                                "description": "Traer datos de la base de datos"
                            },
                            {
                                "id": "002",
                                "title": "<SECTION_1_ROW_2_TITLE>",
                                "description": "<SECTION_1_ROW_2_DESC>"
                            }
                        ]
                    },
                    {
                        "title": "Categoria de productos",
                        "rows": [
                            {
                                "id": "003",
                                "title": "<SECTION_2_ROW_1_TITLE>",
                                "description": "<SECTION_2_ROW_1_DESC>"
                            },
                            {
                                "id": "<LIST_SECTION_2_ROW_2_ID>",
                                "title": "<SECTION_2_ROW_2_TITLE>",
                                "description": "<SECTION_2_ROW_2_DESC>"
                            }
                        ]
                    }
                ]
            }
        }
    }

    
    return data