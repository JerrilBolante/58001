class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def meterstocm(self):
        return self.__distance * 100

    def meterstoin(self):
        return self.__distance * 39.37

    def meterstokm(self):
        return self.__distance / 1000

    def convert_distance(self):
        print(f"{self.__distance} meters is equal to {round(self.meterstocm(), 2)} centimeters.")
        print(f"{self.__distance} meters is equal to {round(self.meterstoin(), 2)} inches.")
        print(f"{self.__distance} meters is equal to {round(self.meterstokm(), 2)} kilometers.")



distance = float(input("Enter the distance in meters: "))
convert = DistanceConversion(distance)
convert.convert_distance()
