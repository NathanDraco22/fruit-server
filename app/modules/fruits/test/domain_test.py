from unittest import TestCase
from ..domain import FruitRepository, FruitModel
from ..service import DBServices

class DBServicesMock(DBServices):
    mock_value = [
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

    def fetch_all(self) -> list[dict]:
        return self.mock_value
    
    def fetch_by_id(self, id: int) -> dict:
        return self.mock_value[id]
    
    

class DomainTest(TestCase):

    db = DBServicesMock()
    repo:FruitRepository

    def setUp(self) -> None:
        self.repo = FruitRepository(db=self.db)

    def test_get_all_fruits(self):
        result = self.repo.get_all_fruits()
        self.assertEqual(type(result[0]), FruitModel )
        self.assertEqual(len(result), len(self.db.fetch_all()))
    
    def test_get_fruit_by_id(self):
        result = self.repo.get_fruit_by_id(0)
        self.assertEqual(type(result), FruitModel)
        self.assertEqual(result.name, "Banana")





