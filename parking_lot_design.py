class Car:
    def __init__(self, license, model, color) -> None:
        self.license = license
        self.model = model
        self.color = color
    def __repr__(self) -> str:
        return f"{self.license},{self.model},{self.color}"

class Garage:
    def __init__(self) -> None:
        self.car_added = []
        self.spot = 10
        self.car_infos = {}
        self.bill = 0
        self.ticket = []

    def spots_available(self):
        return self.spot
    
    def add_car_to_garage(self, car):
        self.spot_name = ['A1', 'B1', 'C1']
        if self.spots_available() > 0:
            user_data = str(car).split(',')
            self.spot -= 1
            self.car_added.append(user_data)

my_garage = Garage()
user_car = Car('1H8VU86B', 'Ferrari', 'Red')
my_garage.add_car_to_garage(user_car)