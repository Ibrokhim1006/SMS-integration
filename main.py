import requests



def send_message(username,item,im):
    url = ""
    params = {
                "messages":
                     [
                     {
                      "recipient":f"{username}",
                      "message-id":"fgh5558",
                         "sms":{
                         "originator": "1234",
                         "content": {
                          "text": f"Tasdiqlash kodi {item} bu kodni hechkimga aytmang {im}"
                          }
                          }
                             }
                         ]
                    }
    username = ""
    password = ""
    response = requests.post(url, auth=(username, password), json=params)