import os
import struct
import re
from typing import Tuple


class BMPImage:
    """Класс для работы с BMP-файлом"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_size(self) -> Tuple[int, int]:
        """ Читает размер изображения из заголовка BMP без загрузки файла в память.
        .bmp файлы имеют:
            - Header (14 байт) c информацией о файле,
            - DIB Header (40 байт) c информацией о изображении,
            - Байты изображения - пиксели
        Ширина и высота — расположены начиная с 18-го байта и занимают по 4 байта
        Первые 4 байта — ширина
        Следующие 4 байта — высота
        """

        # открываем файл для чтения в байтовом режиме
        with open(self.file_path, "rb") as f:
            f.seek(18)  # Смещение на 18 байт
            width, height = struct.unpack("<II", f.read(8))  # Читаем два 4-байтовых числа в little-endian
        return width, height


class BMPImageProxy:
    """Заместитель BMPImage"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._real_image = None

    def get_size(self) -> Tuple[int, int]:
        """Пытается получить размер из имени файла, иначе читает BMP-заголовок"""
        match = re.search(r"_(\d+)x(\d+)\.bmp$", self.file_path, re.IGNORECASE)
        if match:
            width, height = match.groups()
            print("Прочитано из имени файла")
            return int(width), int(height)

        # Если формат имени неверный, создаем реальный объект и читаем заголовок BMP
        if self._real_image is None:
            self._real_image = BMPImage(self.file_path)
            print("Прочитано из файла")
        return self._real_image.get_size()


if __name__ == '__main__':
    images = [
        "vasya_124x768.bmp",
        "kate_200x30.bmp",
        "tree_256xmax.bmp",
    ]

    for img in images:
        proxy = BMPImageProxy(img)
        try:
            print(f"{img}: размер {proxy.get_size()}")
        except FileNotFoundError:
            print(f"{img}: Файл не найден")
