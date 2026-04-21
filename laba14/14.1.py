import math

class Train:

    def __init__(self, destination: str, distance_km: float):
        self.destination = destination   
        self.distance_km = distance_km  

    def travel_days(self) -> float:
        return math.ceil(self.distance_km / 500)

    def __str__(self):
        return (
            f"Потяг до '{self.destination}', "
            f"відстань: {self.distance_km} км, "
            f"днів у дорозі: {self.travel_days()}"
        )

if __name__ == "__main__":
    train1 = Train("Київ", 550)
    train2 = Train("Львів", 1250)
    train3 = Train("Одеса", 500)

    print(train1)  
    print(train2)  
    print(train3)  