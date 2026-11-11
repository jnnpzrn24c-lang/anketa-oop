class Counter:
    def __init__(self, name):
        self.name = name
        self.value = 0  # Изначально значение равно 0

    def add(self, n=1):
        # Увеличивает значение на n; по умолчанию на единицу
        self.value += n

    def reset(self):
        # Обнуляет значение
        self.value = 0

    def __str__(self):
        # Возвращает строку вида «принято: 7»
        return f"{self.name}: {self.value}"

# --- Проверка работы ---
if __name__ == "__main__":
    # 1. Создать два счётчика
    ok = Counter("принято")
    bad = Counter("отклонено")

    # 2. Проверяем метод add
    ok.add(7)        # Прибавили 7
    bad.add()        # Прибавили 1 (по умолчанию)
    
    print(ok)
    print(bad)

    # 3. Проверяем метод reset
    ok.reset()
    print("после сброса:", ok)
    
    # 4. Показываем, что они не мешают друг другу (bad остался прежним)
    print(bad)