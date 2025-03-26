import pyaudio
import numpy as np
import psutil
import os
import time
from pycaw.pycaw import AudioUtilities

# Настройки аудиопотока
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Инициализация PyAudio
p = pyaudio.PyAudio()

# Открытие аудиопотока
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_db_level(data):
    """Вычисление уровня громкости в децибелах."""
    rms = np.sqrt(np.mean(np.square(data)))
    return 20 * np.log10(rms + 1e-9)  # Добавляем маленькое значение, чтобы избежать log(0)

def get_active_apps_with_volume():
    """Получение списка активных приложений с их громкостью."""
    active_apps = []
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        if session.Process:
            app_name = session.Process.name()
            volume = session.SimpleAudioVolume.GetMasterVolume()
            active_apps.append((app_name, volume))
    return active_apps

try:
    while True:
        # Чтение данных из аудиопотока
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        
        # Вычисление уровня громкости в децибелах
        db_level = get_db_level(data)
        
        # Получение активных приложений с их громкостью
        active_apps = get_active_apps_with_volume()
        
        # Очистка консоли
        os.system('cls')
        
        # Вывод информации
        print("Активные приложения и уровень звука в децибелах:")
        
        # Вывод списка приложений и их уровня звука
        for app, volume in active_apps:
            print(f"- {app}: {db_level:.2f} dB")
        
        # Пауза перед следующим измерением
        time.sleep(1)

except KeyboardInterrupt:
    # Остановка и закрытие аудиопотока
    stream.stop_stream()
    stream.close()
    p.terminate()
