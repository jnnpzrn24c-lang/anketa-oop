# Ввод данных
T = float(input("Длительность эксперимента T: "))
N = int(input("Количество элементов N: "))
t1 = float(input("Начало интервала t1: "))
t2 = float(input("Конец интервала t2: "))

# Ввод моментов отказов (через пробел)
times = list(map(float, input("Моменты отказов через пробел: ").split()))

# Считаем отказы к моментам времени
n_T = sum(1 for x in times if x <= T)
n1 = sum(1 for x in times if x <= t1)
n2 = sum(1 for x in times if x <= t2)
dn = n2 - n1
dt = t2 - t1

# За весь период
P_total = (N - n_T) / N
Q_total = n_T / N

# На участке
P_t1 = (N - n1) / N
P_t2 = (N - n2) / N
P_int = P_t2 / P_t1
Q_int = 1 - P_int

# Частота и интенсивность отказов
f = dn / (N * dt)
N_avg = ((N - n1) + (N - n2)) / 2
lam = dn / (N_avg * dt)

# Вывод
print("\n--- За весь период ---")
print("P =", P_total)
print("Q =", Q_total)

print("\n--- На участке [t1, t2] ---")
print("P =", P_int)
print("Q =", Q_int)

print("\nЧастота отказов f =", f)
print("Интенсивность отказов λ =", lam)