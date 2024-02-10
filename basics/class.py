class Car:

    def __init__(self):
        self.price = 0
        self.model_id = 0
        self.name = ""

    def show_name(self):
        print("Name of the car is: ", self.name)
        
    def show_price(self):
        print("Price of the car is: ", self.price)


car1 = Car()
car1.show_name()
car1.show_price()
