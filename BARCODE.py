from PIL import Image
from barcode.codex import Code128
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode


def generate_barcode(data, filename="barcode.png"):
    """Генерация штрих-кода Code128."""
    barcode = Code128(data, writer=ImageWriter())
    barcode.save(filename)
    print(f"Штрих-код Code128 сохранен как {filename}")


def decode_barcode_image(filename):
    """Декодирование штрих-кода из изображения."""
    img = Image.open(filename)
    decoded_objects = decode(img)
    if not decoded_objects:
        print(f"Штрих-код в файле {filename} не удалось распознать.")
    else:
        for obj in decoded_objects:
            print(f"Данные: {obj.data.decode('utf-8')}")
            print(f"Тип кодировки: {obj.type}")
