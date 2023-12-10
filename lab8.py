from PIL import Image

def replace_color(image_path, target_color, replacement_color):
    # Открываем изображение
    img = Image.open(image_path)

    # Получаем пиксели изображения в виде одномерного массива
    pixels = list(img.getdata())

    # Заменяем целевой цвет на новый цвет
    new_pixels = [replacement_color if pixel == target_color else pixel for pixel in pixels]

    # Создаем новый объект изображения с обновленными пикселями
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)

    # Сохраняем новое изображение
    new_image_path = image_path.replace('.', '_modified.')
    new_img.save(new_image_path)

    return new_image_path

# Пример использования
image_path = 'image_/black_image.png'
target_color = (0, 0, 0)
replacement_color = (0, 255, 255)

result_image_path = replace_color(image_path, target_color, replacement_color)
print(f"Изображение сохранено по пути: {result_image_path}")
