class Car:

    POWER_PER_CYLINDER = 30  

    def __init__(self, brand: str, cylinders: int):
        self.brand = brand
        self.cylinders = cylinders

    def power(self) -> float:
        return self.cylinders * self.POWER_PER_CYLINDER

    def __str__(self):
        return (
            f"Машина '{self.brand}', "
            f"циліндрів: {self.cylinders}, "
            f"потужність: {self.power()} к.с."
        )


class Truck(Car):

    def __init__(self, brand: str, cylinders: int, payload_tons: float):
        super().__init__(brand, cylinders)
        self.payload_tons = payload_tons 

    def power(self) -> float:
        return super().power() * 1.25

    def __str__(self):
        return (
            f"Вантажівка '{self.brand}', "
            f"циліндрів: {self.cylinders}, "
            f"вантажність: {self.payload_tons} т, "
            f"потужність: {self.power()} к.с."
        )
if __name__ == "__main__":
    car = Car("Toyota Camry", 4)
    truck = Truck("MAN TGX", 6, 20.0)

    print(car)  
    print(truck) 

    print()
    base = Car(truck.brand, truck.cylinders)
    print(f"  Машина:    {base.power()} к.с.")
    print(f"  Вантажівка: {truck.power()} к.с.")
    print(f"  Різниця:   +{truck.power() - base.power():.1f} к.с. (25%)")