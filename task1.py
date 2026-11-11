class Student:
    def __init__(self, fio, group):
        # Сохраняем ФИО и группу в поля объекта
        self.fio = fio
        self.group = group

    def short(self):
        # Разбиваем ФИО на отдельные слова
        parts = self.fio.split()
        
        # Берем фамилию и первую букву имени
        result = parts[0] + " " + parts[1][0] + "."
        
        # Если есть отчество (третье слово), добавляем и его первую букву
        if len(parts) > 2:
            result += " " + parts[2][0] + "."
            
        return result

# --- Проверка работы (то, что должно выполниться) ---
if __name__ == "__main__":
    # 1. Создаем два объекта
    s1 = Student("Иванов Иван Петрович", "09с33")
    s2 = Student("Петрова Анна", "09с34")

    # 2. Показываем, что short() работает правильно
    print(s1.fio, "->", s1.short())
    print(s2.fio, "->", s2.short())

    # 3. Показываем, что поля у них независимы
    # Меняем группу только у первого студента
    s1.group = "09с99"
    
    print("Группа s1:", s1.group)
    print("Группа s2:", s2.group)