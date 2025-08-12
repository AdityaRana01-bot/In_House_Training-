#def my_function(fname,lname):
#    print(fname + " " + lname)
#my_function("Aditya", "Rana")

#def my_function(fname,lname):
#    print(fname , lname)
#my_function("Aditya","Coder")

#def my_function(*students):
#    print(students[3],"topper of the class")
#my_function("Tushar","Aditya","Reetak","Jatin")

#def my_function(child1, child2, child3):
#    print(f"The youngest child is  {child3}")
#my_function(child1="abc", child2="xyz", child3="pqr")


#def my_function(**kids):
#    print("the last name of child is",kids["lname"])
#my_function(fname="abc", lname="xyz")

#def my_function(country="India"):
#    print("I am from " + country)
#my_function("USA")
#my_function("Thailand")
#my_function()
#my_function("China")

#class person:
#    def __init__(self,name, age):
#        self.name=name
#        self.age=age
#p1=person("Delta",24)
#print(p1.name)
#print(p1.age)

# def decorator1(func):
#     print("Decorator is called")
#     func()
#     print("Decorator is finished")
#     return decorator1

def greet(name):
    print(f"Hello, {name}!")
greet("Aditya Rana")