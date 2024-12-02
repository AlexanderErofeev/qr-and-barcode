from PIL import Image, ImageDraw
from random import randint
from BARCODE import decode_barcode_image, generate_barcode


def corrupt_barcode_image(input_file, output_file, mode="noise", corruption_level=50):
    """Повреждение штрих-кода различными способами."""
    img = Image.open(input_file)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    if mode == "white_noise":
        # Добавление шумовых точек
        for _ in range(corruption_level):
            x, y = randint(0, width - 1), randint(0, height - 1)
            draw.rectangle([x, y, x + 2, y + 2], fill="white")

    if mode == "black_noise":
        # Добавление шумовых точек
        for _ in range(corruption_level):
            x, y = randint(0, width - 1), randint(0, height - 1)
            draw.rectangle([x, y, x + 2, y + 2], fill="black")

    elif mode == "line":
        # Проведение линий через штрих-код
        for _ in range(corruption_level):
            x1, y1 = randint(0, width - 1), randint(0, height - 1)
            x2, y2 = randint(0, width - 1), randint(0, height - 1)
            draw.line([x1, y1, x2, y2], fill="white", width=5)

    elif mode == "block":
        # Закрытие части штрих-кода
        block_width = width // 6  # 1/6 ширины изображения
        block_height = height // 4  # 1/4 высоты изображения
        x = randint(0, width - block_width)
        y = randint(0, height - block_height)
        draw.rectangle([x, y, x + block_width, y + block_height], fill="white")

    img.save(output_file)
    print(f"Поврежденный штрих-код сохранен как {output_file}")


if __name__ == "__main__":
    data = "123456789012"  # Пример данных для штрих-кода

    # Генерация штрих-кода
    generate_barcode(data, filename="data/barcode")

    # Повреждения штрих-кода
    corrupt_barcode_image("data/barcode.png", "data/corrupted_barcode_white_noise.png", mode="white_noise", corruption_level=700)
    corrupt_barcode_image("data/barcode.png", "data/corrupted_barcode_black_noise.png", mode="black_noise", corruption_level=700)
    corrupt_barcode_image("data/barcode.png", "data/corrupted_barcode_block.png", mode="block")
    corrupt_barcode_image("data/barcode.png", "data/corrupted_barcode_line.png", mode="line", corruption_level=10)

    # Декодирование штрих-кодов
    print("\n=== Декодирование оригинального штрих-кода ===")
    decode_barcode_image("data/barcode.png")

    print("\n=== Декодирование поврежденного штрих-кода (белый шум) ===")
    decode_barcode_image("data/corrupted_barcode_white_noise.png")

    print("\n=== Декодирование поврежденного штрих-кода (чёрный шум) ===")
    decode_barcode_image("data/corrupted_barcode_black_noise.png")

    print("\n=== Декодирование поврежденного штрих-кода (блокировка) ===")
    decode_barcode_image("data/corrupted_barcode_block.png")

    print("\n=== Декодирование поврежденного штрих-кода (линии) ===")
    decode_barcode_image("data/corrupted_barcode_line.png")

    print("\n=== Декодирование поврежденного штрих-кода (горизонтальный пропуск) ===")
    decode_barcode_image("data/barcode_1.png")

    print("\n=== Декодирование поврежденного штрих-кода (вертикальный пропуск) ===")
    decode_barcode_image("data/barcode_2.png")