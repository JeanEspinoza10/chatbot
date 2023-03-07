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

def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "Por favor, brindarme su cuenta de red: "
                }
        }
    return data

    