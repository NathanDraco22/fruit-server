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
        "calories" : 80,
        "description" : "it is a green fruit"
    },
    {
        "name" : "Pinapple",
        "color" : "Yellow",
        "flavor" : "sweet",
        "calories" : 110,
        "description" : "it is a really sweet fruit"
    },
    {
        "name" : "Watermelon",
        "color" : "Red",
        "flavor" : "sweet",
        "calories" : 100,
        "description" : "it is a fresh fruit"
    },
    

]

class DBSimulate(DBServices):

    def create(self, obj: dict) -> dict:
        fake_data.append(obj)
        return obj

    def fetch_all(self) -> list[dict]:
        return fake_data
        
    def fetch_by_id(self, id:int) -> dict:
        return fake_data[id]
    
    def delete(self, id:int) -> bool:
        try:
            del(fake_data[id])
            return True
        except:
            return False