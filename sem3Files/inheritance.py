class a:
    def night():
        print("moon")
class b(a):
    def morning():
        print("sunrise")
obj=b()
print("Single Inheritance")
b.night()
b.morning()
class c(b):
    def evening():
        print("sunset")
obj1=c()
print("Multilevel Inheritance")
c.night()
c.morning()
c.evening()

