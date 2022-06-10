from flask import Flask, jsonify
import functions


app = Flask(__name__)
func = functions.Functions()


@app.route("/api/all/<word>", methods=['GET'])
def all(word):
    allList = []
    googleList = func.googleSearch(str(word))
    yahooList = func.yahooSearch(str(word))
    bingList = func.bingSearch(str(word))
    askList = func.askSearch(str(word))
    allList.extend(googleList)
    allList.extend(yahooList)
    allList.extend(bingList)
    allList.extend(askList)

    allEngine = ["Google","Yahoo","Bing","AskFM"]

    json_data = {
        "Aranan Kelime" : word,
        "Arama Motoru" : allEngine,
        "Sonuc" : allList
    }
    return jsonify(json_data)

@app.route("/api/google/<word>", methods=['GET'])
def google(word):
    googleList = func.googleSearch(str(word))
    
    json_data = {
        "Aranan Kelime" : word,
        "Arama Motoru" : "Google",
        "Sonuc" : googleList
    }
    return jsonify(json_data)

@app.route("/api/yahoo/<word>", methods=['GET'])
def yahoo(word):
    yahooList = func.yahooSearch(str(word))
    
    json_data = {
        "Aranan Kelime" : word,
        "Arama Motoru" : "Yahoo",
        "Sonuc" : yahooList
    }
    return jsonify(json_data)

@app.route("/api/bing/<word>", methods=['GET'])
def bing(word):
    bingList = func.bingSearch(str(word))
    
    json_data = {
        "Aranan Kelime" : word,
        "Arama Motoru" : "Bing",
        "Sonuc" : bingList
    }
    return jsonify(json_data)

@app.route("/api/ask/<word>", methods=['GET'])
def ask(word):
    askList = func.askSearch(str(word))
    
    json_data = {
        "Aranan Kelime" : word,
        "Arama Motoru" : "Ask",
        "Sonuc" : askList
    }
    return jsonify(json_data)


if __name__ == "__main__":
    app.run(debug=True)
