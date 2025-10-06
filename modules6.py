# Дополнительно устанавливаемы модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
# Создание и рисование: Drow из ImageDraw
from PIL import Image, ImageFilter, ImageDraw


image = Image.open('images/python.jpg')

# Создание холста
new_image = Image.new('RGB', (600, 400), (255, 255, 255))
new_image.save('images/canvas.jpg')

# Вырезаем фрагмент
# cropped = image.crop(
#     (175, 80, 380, 205)
# )
new_size = image.resize((150, 100))

new_image.paste(new_size, (180, 120))
draw = ImageDraw.Draw(new_image)
draw.rectangle((180, 120, 330, 220), outline=(255, 0, 255), width=15)

new_image.save('images/canvas.jpg')
