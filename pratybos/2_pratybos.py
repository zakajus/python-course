#Sukurkite abstrakčią klasę Box ir apibrėžkite kelis metodus
#darbui su ja:
#add - pridėti bet kokį kiekį elementų į dėžę;
#empty - išimti visus elementus iš dėžės ir grąžinti juos kaip
#sąrašą;
#count - suskaičiuoti, kiek yra elementų dėžėje.
#Sukurkite elementų klasę Item, kuri turėtų požymius name (vardas) ir
#value (vertė). Visi elementai su kuriais dirbsite bus Item klasės
#objektai.
#Sukurkite du klasės Box poklasius, kurie naudotų skirtingus
#konteinerius saugoti elementams: 
#ListBox turi naudoti sąrašą;
#DictBox turi naudoti žodyną.
#Klasės turi sudaryti modulį.
#Naudodami sukurtą modulį parašykite programą, kuri saugotų 9
#elementus ListBox'e ir 7 elementus DictBox'e. Atspausdinkite
#dėžių turinį ir jų vertę.

from abc import ABC, abstractmethod

class Box(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def empty(self):
        pass
    @abstractmethod
    def count(self):
        pass

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'Item - {self.name}:{self.value}'

class ListBox(Box):
    def __init__(self):
        self.box = []
    def add(self, lst):
        self.box.extend(lst)
##    def add(self, *args):
##        self.box.extend(args)
    def empty(self):
        temp = self.box.copy()
        self.box = []
        return temp
    def count(self):
        return len(self.box)

class DictBox(Box):
    def __init__(self):
        self.box = {}
    def add(self, lst):
        for e in lst:
            if e.name in self.box:
                self.box[e.name] = e.value
            else:
                self.box[e.name] += e.value
    def add(self, lst):
        start = self.count()
        for i, e in enumerate(lst, start):
            self.box[i] = e
            #alternatyva
            #self.box.update((i, e))
    def empty(self):
        temp = [Item(name, self.box[name]) for name in self.box]
        #alternatyva
        #temp = self.box.values()
        self.box.clear()
        return temp
    def count(self):
        return len(self.box)
    
if __name__ == "__main__":
    a = Item('aaa', 5)
    print([a,a])
