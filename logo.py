from PIL import Image

# Загрузка оригинального изображения
image = Image.open("/Users/daysw/Documents/GitHub/pixel-logo/Logo q3.png")

# Изменение размера изображения для создания пиксельного эффекта
pixel_size = 15  # Размер блока пикселя
image = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)

# Увеличение изображения обратно до исходного размера
image = image.resize((image.width * pixel_size, image.height * pixel_size), Image.NEAREST)

# Сохранение пиксельного изображения
image.save("quake_logo_pixel.png")

# Открыть изображение для просмотра
image.show()