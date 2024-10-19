from graphviz import Digraph
class Person:
    def __init__(self,name,gender):
        self.name= name 
        self.gender= gender
        self.parents=[]
    def add_parent(self,parent):
        self.parents.append(parent)
john=Person("John","male")
susan=Person("Susan","female")
peter=Person("Peter","male")
lisa=Person("Lisa","female")
michael=Person("Michael","male")
mary=Person("Mary","female")
james=Person("James","male")
anna=Person("Anna","female")

peter.add_parent(john)
peter.add_parent(susan)

lisa.add_parent(john)
lisa.add_parent(susan)

michael.add_parent(peter)
michael.add_parent(mary)

anna.add_parent(james)
anna.add_parent(lisa)

def father(child):
    for parent in child.parents:
        if parent.gender=="male":
            return parent.name
    return None
    
def mother(child):
    for parent in child.parents:
        if parent.gender=="female":
            return parent.name
    return None

def granfather(child):
    for parent in child.parents:
        father_of_parent=father(parent)
        if father_of_parent:
            return father_of_parent
    return None

def grandmother(child):
    for parent in child.parents:
        father_of_parent=father(parent)
        if father_of_parent:
            return father_of_parent
    return None

def siblings(person):
    result=[]
    for parent in person.parents:
        for sibling in parent.parents:
            if sibling!=person and sibling not in result:
                result.append(sibling)
    return result

def brother(person):
    return[sibling.name for sibling in siblings(person)if sibling.gender=="male"]

def sister(person):
    return[sibling.name for sibling in siblings(person)if sibling.gender=="female"]

def uncle(child):
    for parent in child.parents:
        for sibling in siblings(parent):
            if sibling.gender=="male":
                return sibling.name
    return None


def aunt(child):
    for parent in child.parents:
        for sibling in siblings(parent):
            if sibling.gender=="female":
                return sibling.name
    return None

def nephew(uncle_aunt,person):
    return person.gender=="male" and (uncle(person)==uncle_aunt or aunt(person)==uncle_aunt)

def niece(uncle_aunt,person):
    return person.gender=="female" and (uncle(person)==uncle_aunt or aunt(person)==uncle_aunt)

def cousin(person):
    cousins=[]
    for parent in person.parents:
        for sibling in siblings(parent):
            for cousin in sibling.parents:
                cousins.append(cousin.name)
    return cousins

def draw_family_tree():
    tree=Digraph(comment='Family Tree')
    tree.node('J','John')
    tree.node('S','Susan')
    tree.node('P','Peter')
    tree.node('L','Lisa')   
    tree.node('M','Michael')    
    tree.node('Mary','Mary')    
    tree.node('James','James')    
    tree.node('A','Anna')
    tree.edge('J','P',label='father')
    tree.edge('S','P',label='mother')
    tree.edge('J','L',label='father')
    tree.edge('S','L',label='mother')
    tree.edge('P','M',label='father')
    tree.edge('Mary','M',label='Mother')
    tree.edge('James','A',label='father')
    tree.edge('L','A',label='mother')
    tree.render('family_tree',view=True,format='png')

print("Father of Peter:",father(peter))
print("Mother of Peter:",mother(peter))
print("Grandfather of Michael:",granfather(michael))
print("Grandmother of Michael:",grandmother(michael))
print("Brother of Lisa:",brother(lisa))
print("Sister of Peter:",sister(peter))
print("Uncle of Michael:",uncle(michael))
print("Aunt of Anna:",aunt(anna))
print("Cousin of Michael:",cousin(michael))

draw_family_tree()
