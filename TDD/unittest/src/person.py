import requests


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.data_received = False

    def get_all_data(self):
        response = requests.get('http://jsonplaceholder.typicode.com/users/1')

        if response.ok:
            self.data_received = True
            return 'Connected!'

        self.data_received = False
        return 'Error 404'
