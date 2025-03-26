import pyaudio
import numpy as np
import audioop

# Инициализация PyAudio
p = pyaudio.PyAudio()

# Параметры для захвата аудиопотока
FORMAT = pyaudio.paInt16  # Формат аудиоданных
CHANNELS = 1              # Количество каналов (моно)
RATE = 44100              # Частота дискретизации
CHUNK = 1024              # Количество фреймов в одном блоке данных
as_loopback = True        # Использование loopback для захвата звука с устройства

# Открытие потока
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                as_loopback=as_loopback)

try:
    while True:
        # Чтение данных из потока
        data = stream.read(CHUNK)
        
        # Преобразование данных в массив numpy
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Вычисление амплитуды (разница между максимальным и минимальным значением)
        amplitude = np.max(audio_data) - np.min(audio_data)
        
        # Преобразование амплитуды в процент громкости
        volume_percent = (amplitude * 100) / (2**16)
        
        # Вывод результата
        print(f"Громкость: {volume_percent:.2f}%")

except KeyboardInterrupt:
    # Остановка и закрытие потока при прерывании
    stream.stop_stream()
    stream.close()
    p.terminate()
