import re

class AnketaError(Exception):
    pass

class Person:
    def __init__(self, fio, email, phone):
        self.fio = self.check_fio(fio)
        self.email = self.check_email(email)
        self.phone = self.check_phone(phone)

    @staticmethod
    def check_fio(fio):
        words = fio.split()
        if len(words) < 2:
            raise AnketaError("В ФИО меньше двух слов")
        return " ".join(w.capitalize() for w in words)

    @staticmethod
    def check_email(email):
        email = email.strip()
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise AnketaError(f"Неправильная почта: {email}")
        return email

    @staticmethod
    def check_phone(phone):
        digits = re.sub(r"\D", "", phone)
        if len(digits) != 11:
            raise AnketaError(f"Неправильный телефон: {phone}")
        return digits

    def masked_phone(self):
        return f"+7 ({self.phone[1:4]}) ***-**-{self.phone[-2:]}"

    def short_fio(self):
        words = self.fio.split()
        res = words[0] + " " + words[1][0] + "."
        if len(words) > 2:
            res += " " + words[2][0] + "."
        return res

    def role(self):
        return "Неизвестно"

    def extra(self):
        return ""

    def __str__(self):
        return f"{self.fio} ({self.role()}, {self.extra()}) {self.masked_phone()}"

    def __lt__(self, other):
        return self.fio < other.fio


class Student(Person):
    def __init__(self, fio, email, phone, group):
        super().__init__(fio, email, phone)
        group = group.strip()
        if not group:
            raise AnketaError("Пустая группа")
        self.group = group

    def role(self):
        return "студент"

    def extra(self):
        return self.group


class Teacher(Person):
    def __init__(self, fio, email, phone, kafedra):
        super().__init__(fio, email, phone)
        kafedra = kafedra.strip()
        if not kafedra:
            raise AnketaError("Пустая кафедра")
        self.kafedra = kafedra

    def role(self):
        return "преподаватель"

    def extra(self):
        return self.kafedra


def parse_line(line):
    fields = [f.strip() for f in line.split(";")]
    if len(fields) != 5:
        raise AnketaError("Неверное количество полей (нужно 5)")
    
    typ, fio, email, phone, last = fields
    
    if typ == "s":
        return Student(fio, email, phone, last)
    if typ == "t":
        return Teacher(fio, email, phone, last)
    
    raise AnketaError(f"Неизвестный тип: {typ}")


if __name__ == "__main__":
    p = Student("иванов иван петрович", "IVanov@Mail.Ru", "+7 (921) 111-22-33", "09c33")
    print(p)
    print(p.short_fio(), p.masked_phone())