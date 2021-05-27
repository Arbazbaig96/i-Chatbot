import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"

def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key = config["user_key"]


    def get_categories(self):
        """
        Takes no input.
        Returns a dictionary of IDs and their respective category names.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "categories", headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        self.is_key_invalid(a)
        self.is_rate_exceeded(a)

        categories = {}
        for category in a['categories']:
            categories.update({category['categories']['id'] : category['categories']['name']})

        return categories

