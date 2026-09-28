import numpy as np

data_coffee = np.array([
    245, 310, 180, 260, 290, 3500, 220, 275, 240, 310,
    190, 265, 285, 210, 245, 300, 180, 4000, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245,
    300, 180, 260, 290, 150, 330, 220, 275, 240, 310,
    190, 265, 285, 210, 176, 300, 180, 260, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245
])

A = np.array([210, 245, 300, 180, 260,
               290, 150, 330, 220, 275, 
               240, 310, 190, 265, 285])


mean_val = np.mean(data_coffee)
median_val = np.median(data_coffee)
std_val = np.std(data_coffee)
var_val = np.var(data_coffee)
max_val = np.max(data_coffee)
min_val = np.min(data_coffee)
ptp_val = np.ptp(data_coffee)
p25, p50, p75, p90, p99 = np.percentile(data_coffee, [25, 50, 75, 90, 99])
q1, q3 = np.percentile(data_coffee, [25, 75])
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data_coffee[(data_coffee < lower_bound) | (data_coffee > upper_bound)]

print(f"Среднее значение: {mean_val:.2f}")
print(f"Медиана: {median_val:.2f}")
print(f"Стандартное отклонение: {std_val:.2f}")
print(f"Дисперсия: {var_val:.2f}")
print(f"Максимальное значение: {max_val}")
print(f"Минимальное значение: {min_val}")
print(f"Размах данных: {ptp_val}")
print(f"Перцентили (25, 50, 75, 90, 99): {p25}, {p50}, {p75}, {p90}, {p99}")
print(f"Первый квартиль (Q1): {q1}")
print(f"Третий квартиль (Q3): {q3}")
print(f"Межквартильный размах : {iqr}")
print(f"Выбросы : {outliers}")

print("\nАнализ выбросов")
print("Причины появления выбросов (3500 и 4000 руб.):")
print("- Ошибка ввода данных оператором (лишний ноль при вводе 350 или 400 руб.).")
print("- Банкет, крупный корпоративный заказ или покупка дорогой кофемашины/зерна в зернах.")
print("Что делать с выбросами:")
print("- Если это ошибка ввода: удалить или заменить на медиану.")
print("- Если это реальный крупный заказ: оставить для оценки выручки, но для расчета средних чеков использовать медиану.")


A_matrix = A.reshape(3, 5)
print("Матрица 3х5:\n", A_matrix)
print(f"Размерность матрицы: {A_matrix.shape}")
print(f"Общее количество элементов: {A_matrix.size}")
print(f"Сумма по строкам: {np.sum(A_matrix, axis=1)}")
print(f"Сумма по столбцам: {np.sum(A_matrix, axis=0)}")
print("Транспонированная матрица:\n", A_matrix.T)

a_mean = np.mean(A_matrix)
a_std = np.std(A_matrix)
a_var = np.var(A_matrix)
a_q1, a_q2, a_q3 = np.percentile(A_matrix, [25, 50, 75])

print(f"Среднее значение (A): {a_mean:.2f}")
print(f"Стандартное отклонение (A): {a_std:.2f}")
print(f"Дисперсия (A): {a_var:.2f}")
print(f"Квартили матрицы A (Q1, Q2, Q3): {a_q1}, {a_q2}, {a_q3}")


total_revenue = np.sum(data_coffee)
print(f"Общая выручка за 60 дней: {total_revenue} руб.")
print("Причины чеков ниже 200 рублей (150, 176, 180, 190 руб.):")
print("- Покупка только одного напитка (эпрессо/эссенциальные позиции) без выпечки.")
print("- Применение скидок, купонов, бонусов или акций (например, 'кофе с собой до 9 AM').")
print("- Низкая активность в выходные или непиковые часы работы.")
