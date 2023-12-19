from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import requests
import json


class ApiConection():
    source = StringProperty()
    #store = JsonStore('data.json')      # Ejemplo del JsonStore como DB no relacional

    def search_countries(self):
        print("Init search")
        try:
            api_url = f"https://restcountries.com/v3.1/all"
            response = requests.get(api_url)
            print("Aca llame a la api")
            if response.status_code == 200:
                data = json.loads(response.text)
                print("Retorno al hilo principal")
                return data
            else:
                print("Error al obtener resultados de la API.")
                return []
        except Exception as e:
            print(f"Error: {str(e)}")