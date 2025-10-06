# Дополнительно устанавливаемы модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
# Операции с изображением
from PIL import Image, ImageFilter

image = Image.open('images/python.jpg')
pixel = image.load()
w, h = image.size

# Размытие
blur = image.filter(ImageFilter.GaussianBlur(2.5))
blur.save('images/python3.jpg')

# Вырезаем фрагмент
cropped = image.crop(
    (175, 80, 380, 205)
)
cropped.save('images/python4.jpg')

# контуры
contour = image.filter(ImageFilter.CONTOUR)
contour.save('images/python5.jpg')

# отражение по горизонтали
h_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
h_mirror.save('images/python6.jpg')

# отражение по вертикали
w_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
w_mirror.save('images/python7.jpg')