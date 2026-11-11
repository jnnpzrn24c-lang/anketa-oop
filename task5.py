class AgeError(Exception):
    pass


class Person:
    def __init__(self, name, age):
        if age < 0 or age > 120:
            raise AgeError(f"Недопустимый возраст: {age}")
        self.name = name
        self.age = age


if __name__ == "__main__":
    people_data = [
        ("Иван", 25),
        ("Петр", -5),
        ("Анна", 30),
        ("Олег", 150)
    ]

    for name, age in people_data:
        try:
            p = Person(name, age)
            print(f"Создан: {p.name}, возраст {p.age}")
        except AgeError as e:
            print(f"Ошибка для {name}: {e}")