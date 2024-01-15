import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

group_A = 360
std_dev_A = 40
n_A = 9802

group_B = 352
std_dev_B = 58
n_B = 9789

# t-тест
t_statistic, p_value = ttest_ind(np.random.normal(group_A, std_dev_A, n_A), np.random.normal(group_B, std_dev_B, n_B))

alpha = 0.2
print(f"P-значение: {p_value}")
print(f"Уровень значимости: {alpha}")

if p_value < alpha:
    print("Различия статистически значимы. Рекомендуется выкатить версию A.")
else:
    print("Различия не статистически значимы. Рекомендуется выкатить версию B.")


print('__________')

data_A = np.random.normal(group_A, std_dev_A, n_A)
data_B = np.random.normal(group_B, std_dev_B, n_B)

# U-тест
statistic, p_value = mannwhitneyu(data_A, data_B)

print(f"P-значение: {p_value}")
print(f"Уровень значимости: {alpha}")

if p_value < alpha:
    print("Различия статистически значимы. Рекомендуется выкатить версию A.")
else:
    print("Различия не статистически значимы. Рекомендуется выкатить версию B.")