from flask import Flask, request
import util
import whatsappservice
import os
app = Flask(__name__)

@app.route("/welcome", methods=["GET"])
def index():
    return "welcome developer"

@app.route("/whatsapp", methods=["GET"])
def VerifyToken():
    try:
        accessToken = os.getenv("ACCES_TOKEN")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "No se valido correctamente", 400
    except: 
        return"Error", 400


@app.route("/whatsapp", methods=["POST"])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = (changes["value"])
        message = (value["messages"])[0]

        messageUser = (message["text"])["body"]
        number = message["from"]
        text = util.GetTextUser(message)
        #GenerateMessage(messageUser, number)
        print(text)

        return "EVENT_RECEIVED"
    except Exception as e:
        print("Error 1", e)
        return "EVENT_RECEIVED"
 
def GenerateMessage(messageUser, number):
    data = None
    if "si" == messageUser or "Si" == messageUser:
        data = util.TextFormatMessage(number)
    else:
        data = util.TextMessage(number)
    whatsappservice.SendMessageWhatsapp(data)
       
    
    

if (__name__=="__main__"):
    app.run()