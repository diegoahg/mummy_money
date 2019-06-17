from tinydb import TinyDB, Query
import numpy as np
import math

class Inversors:

    def __init__(self):
        self.__db = TinyDB('inversors.json')
        self.__innocence = 0
        self.__experience = 0
        self.__charisma = 0
        self.id = 0
        self.money = 0
        self.weeks = 0
        self.selected = False
    
    def insert(self): 
        self.__innocence = np.random.uniform(0,1)
        self.__experience = np.random.uniform(0,1)
        self.__charisma = np.random.uniform(0,1)
        self.id = self.__db.insert({'innocence': self.__innocence, 'experience': self.__experience, 'charisma': self.__charisma, 'money': 0, 'weeks':0, 'selected':False})

    def save_money(self, money):
        self.__db.update({'money': money}, doc_ids=[self.id])
        self.money = money
    
    def get(self, id):
        result = self.__db.get(doc_id = id)
        self.id = id
        self.money = result.get('money')
        self.selected =  result.get('selected')
        self.weeks =  result.get('weeks')

    def probability_find_member(self, members):
        return self.__experience*self.__charisma*(1 - math.log(members,10))

    def probability_candidate_accept(self):
        return self.__innocence*(1-self.__experience)

    def max_weeks(self):
        return math.floor((1-self.__innocence)*self.__experience*self.__charisma*10)

    def add_week(self):
        week = self.weeks + 1
        self.__db.update({'weeks': week}, doc_ids=[self.id])
    
    def count(self):
        return len(self.__db.all())

    def select(self):
        Inversor = Query()
        select = self.__db.search(Inversor.selected == False)
        if len(select) > 0:
            # Update to selected
            select = select[0]
            self.__db.update({'selected': True}, doc_ids=[select.doc_id])
            self.id = select.doc_id
            self.selected = True
            self.money = select.get('money')
        else:
            self.id = 0

        return self 