class Car(object):
    def __init__(self,  battery,  distance= 30,  drive= False):
        # These are things that a Car has.
        # All of these should be relevant to our program.
        self.battery = battery
        self.motor = drive
        self.lights = True  # Who turn the cars lights off?
        self.speed = distance
        self.engine_pressure = 4

    def move(self, Mph):
        if self.motor:
            if self.engine_pressure <= 0:
                print("There's no pressure")
            elif self.engine_pressure < Mph:
                print("You not driving any %s", Mph)
                self.engine_pressure = 0
            else:
                print("You drove %s", Mph)
                self.engine_pressure -=  Mph
        else:
            print("You not driving")