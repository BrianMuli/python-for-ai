#creating classe
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print("Bark!!!Bark!!")    

dog1=Dog("jetty","german")
dog1.bark()
dog1.name