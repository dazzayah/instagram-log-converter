try:
    import json
    from Utils import ReplaceChar 
except Exception as err:
    print("Ha faltado un modulo ", err)

try:
    MAINPATH = r"JSON_Content\AilitaRivero\message_1.json"
    with open(MAINPATH, encoding='latin1') as fh:
        data = json.load(fh)
except:
    print("No existe el fichero json que se ha intentado leer.")

OverAllMessages = reversed(data["messages"]) #We reverse the json file because it is read upside down 

CumulativeResponse = ""
for message in OverAllMessages:
    if message.get('content') != None:
        CumulativeResponse = CumulativeResponse + f"{ReplaceChar(message.get('sender_name'))}: {ReplaceChar(message.get('content').encode("latin1").decode("utf-8"))}" + "\n"
    else:
        CumulativeResponse =  CumulativeResponse + f"{ReplaceChar(message.get('sender_name'))}: " + '~Multimedia~' + "\n"

SavePath = r"Output.txt"
try:
    with open(SavePath , "w" , encoding="utf-8") as f:
        f.write(CumulativeResponse)
except Exception as err:
    print(f"Ha surgido un error crítico al intentar escribir en el fichero de texto.{err}")