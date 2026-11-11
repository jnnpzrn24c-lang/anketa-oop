"""
Программа «Сведение расходов».
Объединяет два словаря расходов по категориям за два месяца,
суммируя значения при совпадении категорий.
"""


def validate_expenses(expenses: dict, month_name: str) -> None:
    """
    Проверяет корректность словаря расходов.

    :param expenses: словарь вида {категория: сумма}
    :param month_name: название месяца (для сообщения об ошибке)
    :raises TypeError: если передан не словарь
    :raises ValueError: если сумма отрицательная или не число
    """
    if not isinstance(expenses, dict):
        raise TypeError(f"Расходы за {month_name} должны быть словарём")

    for category, amount in expenses.items():
        if not isinstance(amount, (int, float)):
            raise ValueError(
                f"Сумма по категории '{category}' ({month_name}) "
                f"должна быть числом"
            )
        if amount < 0:
            raise ValueError(
                f"Сумма по категории '{category}' ({month_name}) "
                f"не может быть отрицательной"
            )


def merge_expenses(month1: dict, month2: dict) -> dict:
    """
    Объединяет два словаря расходов в один, суммируя значения
    по совпадающим категориям.

    Категории, присутствующие только в одном из месяцев,
    переносятся в результат без изменений.

    :param month1: расходы за первый месяц {категория: сумма}
    :param month2: расходы за второй месяц {категория: сумма}
    :return: объединённый словарь {категория: суммарная сумма}
    """
    validate_expenses(month1, "первый месяц")
    validate_expenses(month2, "второй месяц")

    # Обрабатываем граничный случай: оба словаря пусты
    if not month1 and not month2:
        raise ValueError("Оба словаря расходов пусты — нечего объединять")

    # Копируем первый месяц, чтобы не изменять исходные данные
    merged = dict(month1)

    for category, amount in month2.items():
        merged[category] = merged.get(category, 0) + amount

    return merged


def print_report(merged: dict) -> None:
    """
    Выводит итоговый отчёт по объединённым расходам.

    :param merged: объединённый словарь {категория: сумма}
    """
    if not merged:
        print("Нет данных для отчёта.")
        return

    print("\n=== Сводный отчёт по расходам ===")
    total = 0
    for category, amount in sorted(merged.items(), key=lambda x: -x[1]):
        print(f"{category:<20} {amount:>10.2f} руб.")
        total += amount
    print("-" * 32)
    print(f"{'ИТОГО':<20} {total:>10.2f} руб.")


def main() -> None:
    """Точка входа: демонстрация работы программы."""
    # Расходы за январь и февраль
    january = {
        "Продукты": 15000,
        "Транспорт": 3000,
        "Коммунальные": 5000,
        "Развлечения": 2500,
    }
    february = {
        "Продукты": 16000,
        "Коммунальные": 5200,
        "Здоровье": 4000,
        "Транспорт": 2800,
    }

    print("Январь:  ", january)
    print("Февраль: ", february)

    merged = merge_expenses(january, february)
    print_report(merged)

    # Проверка граничных случаев
    print("\n--- Проверка граничных случаев ---")
    try:
        merge_expenses({}, {})
    except ValueError as e:
        print("Ошибка (пустые словари):", e)

    try:
        merge_expenses({"Еда": -100}, {"Еда": 50})
    except ValueError as e:
        print("Ошибка (отрицательная сумма):", e)

    try:
        merge_expenses({"Еда": "много"}, {"Еда": 50})
    except ValueError as e:
        print("Ошибка (не число):", e)

    # Один словарь пуст — второй должен пройти без ошибок
    result = merge_expenses({}, {"Еда": 1000})
    print("Объединение пустого и непустого словаря:", result)


if __name__ == "__main__":
    main()

