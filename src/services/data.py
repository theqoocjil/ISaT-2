from repositories.person import PersonrRep


class DataService():

    def __init__(self):
        self._person_rep = PersonrRep()

    def add_friends(self):
        return True