from flask import Flask, render_template, request
import requests
from BitcoinAPI import Bitcoin



app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    
    bitcoin = Bitcoin.parse_responce()
    print(type(bitcoin))
    #currency = json.loads(str(bitcoin_json))
    # print(type(currency))


    #print(response_list)
    return render_template("homepage.html", tree=bitcoin)

 
if __name__ == '__main__':
    app.run(debug=True)
