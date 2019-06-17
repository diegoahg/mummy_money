from tinydb import TinyDB, Query

class Members:

    def __init__(self):
        self.__db = TinyDB('members.json')
        self.id = 0
        self.inversor_id = 0
        self.recruited_by = 0
        self.is_active = True
    
    def insert(self, inversor_id, recruited_by):
        self.inversor_id = inversor_id
        self.id = self.__db.insert({'inversor_id': inversor_id, 'recruited_by': recruited_by, 'is_active': True})
    
    def get(self, id):
        result = self.__db.get(doc_id = id)
        self.id = result.doc_id
        self.inversor_id = result.get("inversor_id")
        self.recruited_by = result.get("recruited_by")
        self.is_active = result.get("is_active")

    def remove(self):
        self.__db.update({'is_active': False}, doc_ids=[self.id])
    
    def getMembersActive(self):
        Member = Query()
        actives = self.__db.search(Member.is_active == True)
        return actives

    def count(self):
        Member = Query()
        actives = self.__db.search(Member.is_active == True)
        return len(actives)
        