class ParkingLot:
    def __init__(self, size, spot_length=12, spot_width=8):
        self.size = size
        self.spot_length = spot_length
        self.spot_width = spot_width
        self.spots = self.calculate_spots()
        self.parked_cars = [None] * self.spots

    def calculate_spots(self):
        spot_area = self.spot_length * self.spot_width
        return self.size // spot_area

    def park_car(self, car, spot_number):
        if 0 <= spot_number < self.spots and not self.parked_cars[spot_number]:
            self.parked_cars[spot_number] = car
            return True
        return False

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot_number):
        success = parking_lot.park_car(self, spot_number)
        if success:
            return f"Car with license plate {self.license_plate} parked successfully in spot {spot_number + 1}"
        else:
            return f"Car with license plate {self.license_plate} could not park in spot {spot_number + 1}"

def main(cars, parking_lot):
    for car in cars:
        spot_parked = False
        attempts = 0
        while not spot_parked and attempts < parking_lot.spots:
            spot_number = random.randint(0, parking_lot.spots - 1)
            if parking_lot.parked_cars[spot_number] is None:
                print(car.park(parking_lot, spot_number))
                spot_parked = True
            attempts += 1


import random
parking_lot = ParkingLot(2000)
cars = [Car(f"{random.randint(100000, 9999999)}") for _ in range(25)]
main(cars, parking_lot)