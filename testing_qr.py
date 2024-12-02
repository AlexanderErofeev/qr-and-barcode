from PIL import Image, ImageDraw
from random import randint
from QR import generate_qr, decode_qr_image


def corrupt_qr_image(input_file, output_file, mode="noise", corruption_level=50):
    """Повреждение QR-кода различными способами."""
    img = Image.open(input_file)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    if mode == "white_noise":
        # Добавление шумовых точек
        for _ in range(corruption_level):
            x, y = randint(0, width - 1), randint(0, height - 1)
            draw.rectangle([x, y, x + 5, y + 5], fill="white")

    if mode == "black_noise":
        # Добавление шумовых точек
        for _ in range(corruption_level):
            x, y = randint(0, width - 1), randint(0, height - 1)
            draw.rectangle([x, y, x + 5, y + 5], fill="black")

    elif mode == "block":
        # Закрытие меньшей центральной части
        center_x, center_y = width // 2, height // 2
        block_size = min(width, height) // 6  # Уменьшено до 1/6 от размера
        draw.rectangle(
            [center_x - block_size, center_y - block_size,
             center_x + block_size, center_y + block_size],
            fill="white"
        )

    elif mode == "corner":
        # Закрытие угла
        corner_size = width // 4
        draw.rectangle([0, 0, corner_size, corner_size], fill="white")  # Верхний левый угол

    elif mode == "line":
        # Проведение линий через QR-код
        for _ in range(corruption_level):
            x1, y1 = randint(0, width - 1), randint(0, height - 1)
            x2, y2 = randint(0, width - 1), randint(0, height - 1)
            draw.line([x1, y1, x2, y2], fill="white", width=5)

    img.save(output_file)
    print(f"Поврежденный QR-код сохранен как {output_file}")


if __name__ == "__main__":
    data = "Пример данных для анализа"
    ecc_level = "H"  # Используем высокий уровень коррекции ошибок

    # Генерация QR-кода
    generate_qr(data, ecc_level=ecc_level, filename="data/qr_code_h.png")

    # Разные повреждения
    corrupt_qr_image("data/qr_code_h.png", "data/corrupted_qr_white_noise.png", mode="white_noise", corruption_level=400)
    corrupt_qr_image("data/qr_code_h.png", "data/corrupted_qr_black_noise.png", mode="black_noise", corruption_level=400)
    corrupt_qr_image("data/qr_code_h.png", "data/corrupted_qr_small_block.png", mode="block")
    corrupt_qr_image("data/qr_code_h.png", "data/corrupted_qr_corner.png", mode="corner")
    corrupt_qr_image("data/qr_code_h.png", "data/corrupted_qr_line.png", mode="line", corruption_level=10)

    # Декодирование QR-кодов
    print("\n=== Декодирование оригинального QR-кода ===")
    decode_qr_image("data/qr_code_h.png")

    print("\n=== Декодирование поврежденного QR-кода (белый шум) ===")
    decode_qr_image("data/corrupted_qr_white_noise.png")

    print("\n=== Декодирование поврежденного QR-кода (чёрный шум) ===")
    decode_qr_image("data/corrupted_qr_black_noise.png")

    print("\n=== Декодирование поврежденного QR-кода (меньший центр закрыт) ===")
    decode_qr_image("data/corrupted_qr_small_block.png")

    print("\n=== Декодирование поврежденного QR-кода (угол закрыт) ===")
    decode_qr_image("data/corrupted_qr_corner.png")

    print("\n=== Декодирование поврежденного QR-кода (линии) ===")
    decode_qr_image("data/corrupted_qr_line.png")
