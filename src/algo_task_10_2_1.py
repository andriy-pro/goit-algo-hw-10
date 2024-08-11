import matplotlib.pyplot as plt
import numpy as np


# Визначення функції
def f(x):
    return x**2


# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
N = 10000

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Підрахунок кількості точок під кривою
under_curve = y_random < f(x_random)
integral_mc = (b - a) * f(b) * np.mean(under_curve)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ax.fill_between(x, y, color="gray", alpha=0.3)

# Відображення точок
ax.scatter(x_random, y_random, c=under_curve, cmap="coolwarm", s=1, alpha=0.5)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(
    f"Метод Монте-Карло: Інтеграл f(x) = x^2 від {a} до {b}\n"
    f"Оцінка інтеграла: {integral_mc:.4f}"
)
plt.grid()
plt.show()

print(f"Оцінка інтеграла методом Монте-Карло: {integral_mc:.4f}")
