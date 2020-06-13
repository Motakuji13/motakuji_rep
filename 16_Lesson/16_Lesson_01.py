class Person:
    name = "Dolboeb"
    age = 30
    
    def set(self, name, age):
        self.name = name
        self.age = age
    

vlad = Person ()
vlad.set ("Влад", 25)
print (vlad.name + " " + str(vlad.age))

Dolboeb = Person ()
Dolboeb.set ("Долбоеб", 56)
print (Dolboeb.name + " " + str(Dolboeb.age))