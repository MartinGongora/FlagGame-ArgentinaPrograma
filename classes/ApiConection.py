from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import requests
import json
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget, IconLeftWidget
from kivy.storage.jsonstore import JsonStore


class ApiConection():
    source = StringProperty()
    #store = JsonStore('data.json')      # Ejemplo del JsonStore como DB no relacional

    def search_product(self):
        print("Init search")
        try:
            api_url = f"https://restcountries.com/v3.1/all"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            else:
                print("Error al obtener resultados de la API.")
                return []
        except Exception as e:
            print(f"Error: {str(e)}")