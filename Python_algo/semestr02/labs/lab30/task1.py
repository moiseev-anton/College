"""
Программа для побайтового реверса .wav файла
"""

import wave
import struct

# открываем WAV-файл
source = wave.open("in.wav", mode="rb")

# содаем новый WAV-файл для записи перевёрнутого аудио
dest = wave.open("out.wav", mode="wb")

# устанавливаем параметры аудиопотока как у исходного файла
dest.setparams(source.getparams())

# получаем количество фреймов в исходном файле
frames_count = source.getnframes()

# читаем фреймы как строку байтов
audio_frames = source.readframes(frames_count)

# перобразуем строку байтов в список значений
data = struct.unpack("<" + str(frames_count) + "h", audio_frames)

# делаем реверс списка байтов
newdata = data[::-1]

# упоковываем список значений обратно в строку байтов
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

# записываем перевёрнутые фреймы в новый файл
dest.writeframes(newframes)

# закрываем файлы
source.close()
dest.close()




