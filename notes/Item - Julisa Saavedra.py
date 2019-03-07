class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False  # Because the engine is off
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward.")

    def move_backward(self):
        self.fuel -= 1
        print("You move backward")

    def turn_left(self):
        self.fuel -= 1
        print("You turn left.")

    def turn_right(self):
        self.fuel -= 1
        print("You turn right.")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off.")


class Ferrari(Car):
    def __init__(self):
        super(Ferrari,self).__init__("Ferrari", "Gas", "Slim")


class Lamborghini(Car):
    def __init__(self):
        super(Lamborghini, self).__init__("Lamborghini", "Gas", "Slim")


class Mustang(Car):
    def __init__(self):
        super(Mustang, self).__init__("Mustang", "Gas", "Slim")


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__("Corvette", "Gas", "Slim")


class Bugatti(Car):
    def __init__(self):
        super(Bugatti, self).__init__("Bugatti", "Gas", "Slim")


class KeylessCar(Car):
    def __init__(self, name, engine_type, body_type):
        super(KeylessCar, self).__init__(name, engine_type, body_type)

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the car starts.")


julissa_car = Ferrari()
julissa_car.start_engine()
julissa_car.move_forward()
julissa_car.move_backward()
julissa_car.turn_right()
print()

matthew_car = KeylessCar("Matthew's ride", "Diesel", "Toaster")
matthew_car.start_engine()
matthew_car.move_forward()
matthew_car.move_backward()
matthew_car.turn_off()