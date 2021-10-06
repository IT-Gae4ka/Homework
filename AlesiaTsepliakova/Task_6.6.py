# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. Implement singleton logic inside your custom class using a method to initialize class instance.
#Синглтон - это класс, который позволяет создать только один экземпляр самого себя и предоставляет доступ к этому созданному экземпляру. Реализуйте одноэлементную логику внутри своего настраиваемого класса, используя метод для инициализации экземпляра класса.


# Example:

# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True

class Sun:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sun, cls).__new__(cls)
            
    def inst():
        return Sun()

      
p = Sun.inst()
f = Sun.inst()
print(p is f)