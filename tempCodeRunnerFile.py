from registry import Registry


def main():
    reg = Registry()
    
    if not reg.load("anketa.txt"):
        print("Файл anketa.txt не найден. Положите его рядом с программой.")
        return

    reg.accepted.sort()

    print(f"{'№':>2}  {'ФИО':<30}{'Роль':<16}{'Группа/кафедра':<18}Телефон")
    print("-" * 80)
    for i, p in enumerate(reg.accepted, start=1):
        print(f"{i:>2}  {p.fio:<30}{p.role():<16}{p.extra():<18}{p.masked_phone()}")

    print()
    for num, line, reason in reg.rejected:
        print(f"строка {num}: {reason}")

    print()
    print(f"Принято: {len(reg)} | Отклонено: {len(reg.rejected)}")
    print()
    
    print("По ролям:")
    for role, cnt in reg.stats_roles().items():
        print(f"  {role}: {cnt}")
        
    print("По группам:")
    for g, cnt in reg.stats_groups().items():
        print(f"  {g}: {cnt}")

    reg.save_ok()
    reg.save_errors()
    print("\nСохранено в ok.txt и errors.txt")


if __name__ == "__main__":
    main()