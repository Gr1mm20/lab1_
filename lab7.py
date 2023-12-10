class ChartDrawer:
    def __init__(self):
        self._points = []

    def add_point(self, x, y):
        """
        Метод для добавления новой точки в список координат.

        Parameters:
        - x (float): Координата x новой точки.
        - y (float): Координата y новой точки.
        """
        self._points.append((x, y))

    def remove_point(self, x, y):
        """
        Метод для удаления точек с указанными координатами из списка.

        Parameters:
        - x (float): Координата x точки для удаления.
        - y (float): Координата y точки для удаления.
        """
        self._points = [point for point in self._points if point != (x, y)]

    def get_points(self):
        """
        Метод для получения списка всех точек.

        Returns:
        - list: Список координат всех точек.
        """
        return self._points

# Пример использования класса ChartDrawer
chart = ChartDrawer()

# Добавление точек
chart.add_point(1, 2)
chart.add_point(3, 4)
chart.add_point(5, 6)

# Получение списка точек
points_before_removal = chart.get_points()
print("Точки до удаления:", points_before_removal)

# Удаление точки
chart.remove_point(3, 4)

# Получение обновленного списка точек
points_after_removal = chart.get_points()
print("Точки после удаления:", points_after_removal)
