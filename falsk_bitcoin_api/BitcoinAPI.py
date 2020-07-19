import requests
class Bitcoin:
   
    API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    def __init__(self):
        pass
        #self.Currency = Currency
    @classmethod
    def read_api(cls):      
        resonse = requests.get(Bitcoin.API_URL)
        return resonse

    @classmethod
    def parse_responce(cls):
        json_responce = Bitcoin.read_api()
        respose_list = []
        if json_responce.status_code == 200:
            r_json = json_responce.json()
        return r_json






