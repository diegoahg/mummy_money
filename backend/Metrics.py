from tinydb import TinyDB, Query

class Metrics:

    def __init__(self):
        self.population = 0
        self.mummy_money = 0 
        self.__db = TinyDB('metrics.json')

    def generate(self): 
        self.__db.insert({'population': 0})
        self.__db.insert({'mummy_money': 0})
    
    def add_population(self, population):
        self.__db.update({'population': population}, doc_ids=[1])

    def add_mummy_money(self):
        mummy_money = self.__db.get(doc_id = 2)
        money = int(mummy_money.get('mummy_money')) + 500
        self.__db.update({'mummy_money': money}, doc_ids=[2])
    
    def subtract_mummy_money(self):
        mummy_money = self.__db.get(doc_id = 2)
        money = int(mummy_money.get('mummy_money')) - 100
        self.__db.update({'mummy_money': money}, doc_ids=[2])
    
    def get(self):
        self.population = self.__db.get(doc_id = 1).get('population')
        self.mummy_money = self.__db.get(doc_id = 2).get('mummy_money')

