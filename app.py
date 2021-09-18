from flask import Flask,jsonify,request
from bs4 import BeautifulSoup
import requests
from functools import wraps


keyList = ["BviOCxd3CdFPQu8xMYi2fc","kcbOUZHFL6Ci8eeVpgTms2"]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
app = Flask(__name__)

def key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = request.args.get("key")
        if key in keyList:
            return f(*args, **kwargs)
        else:
            return "Geçersiz Anahtar"

    return decorated_function


def googleSearch(word):
    request= requests.get(f"https://www.google.com.tr/search?q={word}",headers=headers)
    soup= BeautifulSoup(request.content,"html.parser")
    links = soup.select("a")
    array = []

    for item in links:
        text =str(item.get("href"))
        control = 'google' in text or 'search' in text or 'None' in text or '#' in text
        if control ==  False:
            array.append(item.get("href"))   

    return array 



def yahooSearch(word):
    request= requests.get(f"https://search.yahoo.com/search?p={word}",headers=headers)
    soup= BeautifulSoup(request.content,"html.parser")
    links = soup.select("a")
    array = []
    
    for item in links:
        text =str(item.get("href"))
        control = "r.search.yahoo.com" in str(item.get("href"))
        if control == True:
            control2 = 'pstart' in text or 'www.yahoo.com' in text or 'bing' in text or '2fshopping' in text or '2fsports' in text or '2ffinance' in text or '2fchrome' in text or '2fadvertising' in text
            if control2 == False:
                array.append(text.strip())
    
    return array


def bingSearch(word):
    request= requests.get(f"https://www.bing.com/search?q={word}",headers=headers)
    soup= BeautifulSoup(request.content,"html.parser")
    links = soup.select("a")
    array = []
    
    for item in links:
        text =str(item.get("href"))
        control = text in array or 'go' in text or '/search' in text or '/videos' in text or '/images' in text or '/maps' in text or 'javascript' in text or 'FORM' in text or '#' in text or 'None' in text
        if control == False:
            array.append(item.get("href"))

    return array


def askSearch(word):
    request= requests.get(f"https://www.ask.com/web?q={word}&ad=SEO&o=779176&qo=homepageSearchBox",headers=headers)
    soup= BeautifulSoup(request.content,"html.parser")
    links = soup.select("a")
    array = []

    for item in links:
        text =str(item.get("href"))
        control = 'askmediagroup' in text or '/cookies' in text or '/terms' in text or '/privacy' in text or '/about' in text or '/web?q=' in text
        if control == False:
            array.append(text)
    
    return array

@app.route("/api/google/<word>", methods=['GET'])
@key_required
def google(word):
    googleList = googleSearch(word)
    
    return  str(googleList).replace(",","<br>")



@app.route("/api/yahoo/<word>", methods=['GET'])
@key_required
def yahoo(word):
    yahooList = yahooSearch(word)

    return  str(yahooList).replace(",","<br>")

@app.route("/api/bing/<word>", methods=['GET'])
@key_required
def bing(word):
    bingList = bingSearch(word)
    return str(bingList).replace(",","<br>")

@app.route("/api/ask/<word>", methods=['GET'])
@key_required
def ask(word):
    askList = askSearch(word)

    return str(askList).replace(",","<br>")


if __name__ == "__main__":
    app.run(debug=True)
