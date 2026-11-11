class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.celsius:.1f} C = {self.fahrenheit:.1f} F"

    def __lt__(self, other):
        return self.celsius < other.celsius


if __name__ == "__main__":
    temps = [Temperature(21.5), Temperature(-3.0), Temperature(15.0)]
    
    print("Исходные температуры:")
    for t in temps:
        print(t)
        
    print("\nПо возрастанию:")
    for t in sorted(temps):
        print(t)
        
    print("\nСамый тёплый:")
    print(max(temps))