import scipy.integrate as spi


# Функція для інтегрування
def f(x):
    return x**2


# Межі інтегрування
a = 0
b = 2

# Обчислення інтеграла за допомогою SciPy
result, error = spi.quad(f, a, b)
print(f"Точне значення інтеграла: {result:.4f}")
