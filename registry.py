from people import parse_line, AnketaError


class Registry:
    def __init__(self):
        self.accepted = []
        self.rejected = []

    def add(self, person):
        self.accepted.append(person)

    def load(self, filename):
        try:
            f = open(filename, encoding="utf-8")
        except FileNotFoundError:
            return False
        
        with f:
            for i, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    self.add(parse_line(line))
                except AnketaError as e:
                    self.rejected.append((i, line, str(e)))
        return True

    def stats_roles(self):
        result = {}
        for p in self.accepted:
            result[p.role()] = result.get(p.role(), 0) + 1
        return result

    def stats_groups(self):
        result = {}
        for p in self.accepted:
            result[p.extra()] = result.get(p.extra(), 0) + 1
        return result

    def save_ok(self, filename="ok.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for p in self.accepted:
                f.write(f"{p.fio};{p.role()};{p.extra()};{p.masked_phone()}\n")

    def save_errors(self, filename="errors.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for num, line, reason in self.rejected:
                f.write(f"строка {num}: {reason}: {line}\n")

    def __len__(self):
        return len(self.accepted)


if __name__ == "__main__":
    r = Registry()
    if r.load("anketa.txt"):
        print(len(r), "принято,", len(r.rejected), "отклонено")
    else:
        print("Файла нет")