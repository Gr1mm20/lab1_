import numpy as np
import matplotlib.pyplot as plt

def shuffle_numbers_numpy(input_list):
    """
    Перемешивает список целых чисел с использованием NumPy.

    Parameters:
    - input_list (list): Список целых чисел.

    Returns:
    - numpy.ndarray: Перемешанный массив целых чисел.
    """
    shuffled_array = np.array(input_list)
    np.random.shuffle(shuffled_array)
    return shuffled_array

# Пример использования с NumPy
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_numbers_numpy(original_list)
print("Оригинальный список:", original_list)
print("Перемешанный список (NumPy):", shuffled_result)

# Пример использования с Matplotlib для построения графика
plt.plot(original_list, label='Оригинальный список')
plt.plot(shuffled_result, label='Перемешанный список (NumPy)')
plt.legend()
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.title('График оригинального и перемешанного списков')
plt.show()
