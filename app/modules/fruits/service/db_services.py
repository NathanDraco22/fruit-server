from .abstract.abstract_db import DBServices

fake_data = [
    {
        "name" : "Banana",
        "color" : "yellow",
        "flavor" : "sweet",
        "calories" : 60,
        "description" : "it is a nice fruit"
    },
    {
        "name" : "Apple",
        "color" : "Green",
        "flavor" : "sweet",
        "calories" : 60,
        "description" : "it is a green fruit"
    },

]

class DBSimulate(DBServices):
    def fetch_all(self) -> list[dict]:
        return fake_data
        
    def fetch_by_id(self, id:int) -> dict:
        return fake_data[id]