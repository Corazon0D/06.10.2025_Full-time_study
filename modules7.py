# Создание холста
from PIL import Image, ImageFilter, ImageDraw

new_image = Image.new('RGB', (600, 400), (180, 180, 180))


# Создаём объект для рисования и указываем на чём рисовать
draw = ImageDraw.Draw(new_image)

# Рисуем прямоугольник по контору и толщиной 3 пикселя
draw.rectangle((0, 0, 599, 399), outline=(255, 0, 255), width=3)
# Рисуем линию, разделяющую холст пополам
draw.line((299, 0, 299, 399), fill=(255, 0, 255), width=3)
# Рисуем две диагонали
draw.line((0, 0, 599, 399), fill=(255, 0, 255), width=3)
draw.line((599, 0, 0, 399), fill=(255, 0, 255), width=3)
new_image.save('images/canvas.jpg')