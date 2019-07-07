class Car(object):

    def __init__(self, name="General", model="GM", num_of_doors=None, car_type=None, num_of_wheels=None, speed=0):
        self.name = name
        self.model = model
        self.num_of_doors = num_of_doors
        self.car_type = car_type
        self.num_of_wheels = num_of_wheels
        self.speed = speed
        
        if (self.name == "Porshe" or self.name == "Koenigsegg"):
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if (self.num_of_wheels == 4):
            self.car_type = "saloon"
        else:
            self.car_type = "trailer"
            
            
    def is_saloon(self):
        if(self.num_of_wheels == 4):
            return "saloon"
        else:
            return "trailer"

    def drive(self, current_speed):
        self.speed = current_speed
        return self.speed
