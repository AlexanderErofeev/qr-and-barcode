import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def generate_qr(data, ecc_level, filename="qr_code.png"):
    """Генерация QR-кода с заданным уровнем коррекции ошибок."""
    ecc_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H,
    }
    qr = qrcode.QRCode(
        version=1,
        error_correction=ecc_levels.get(ecc_level, qrcode.constants.ERROR_CORRECT_M),
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR-код с уровнем ECC {ecc_level} сохранен как {filename}")


def decode_qr_image(filename):
    """Декодирование QR-кода из изображения."""
    img = Image.open(filename)
    decoded_objects = decode(img)
    if not decoded_objects:
        print(f"QR-код в файле {filename} не удалось распознать.")
    else:
        for obj in decoded_objects:
            print(f"Данные: {obj.data.decode('utf-8')}")
            print(f"Тип кодировки: {obj.type}")
