# this is one way to make a class, every instance of this class would have the values that are set in the constructor method, we can't pass the values since we have not provided any argument space in the constructor method
class Car:
    def __init__(self):
        self.price = 0
        self.model_id = 0
        self.name = ""

    def show_name(self):
        print("Name of the car is: ", self.name)
        
    def show_price(self):
        print("Price of the car is: ", self.price)


# this is another way of making a class in python, here in the constructor method we have passed the arguments that we can set to the data members(variables used) in the class
class CarFull:
    def __init__(self, name, price, model_id): 
        self.name = name
        self.price = price
        self.model_id = model_id

    def show_name(self):
        print("the name of the car is: ", self.name)

    def show_price(self):
        print("the price of the car is:", self.price)

    def show_model_id(self):
        print("the model id of the car is:", self.model_id)
        
#an instance of the class where we cannot pass anything to the constructor
car1 = Car() 
car1.show_name()
car1.show_price()

# a constructor method initializes an instances and sets values to the data mambers of that class, a class in itself does not take any space, it is only an object(instance) is created the memory is assigned to that particular object(instance)

#an instance of the class where we can pass arguments to the constructor
car2 = CarFull("XUV700", 2400000, "ax7 automatic")
car2.show_model_id()
car2.show_name()
car2.show_price()
