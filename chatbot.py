import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "76f1feb0-77f0-11ec-816d-9da0fc946d1c4e71352f-8f4c-4808-8cdb-dd24c9e2e6e8"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_questions():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    if answerclass == "Precio":
        print ("El precio de los buzos es 13,80€.")
    elif answerclass == "Tallas":
        print ("Tenemos tallas desde la 48 a la 64. Si no encuentra de su talla, llame a la tienda y nos encargamos de traerlo!.")
    elif answerclass == "Descuentos":
        print ("Los buzos no tienen descuento por cantidad.")

print ("Te gustaria saber algo sobre los buzos que tenemos disponibles?")

while True:
    answer_questions()