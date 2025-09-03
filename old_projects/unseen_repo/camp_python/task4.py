zlodeev = input("Сколько злодеев поймал Человек-паук сегодня?")

if zlodeev.isdigit():
    zlodeev = int(zlodeev)
    print(f"Питер Паркер заработал {zlodeev * 10} долларов на фото!")
else:
    print("Джей Джона Джеймсон злится: 'Это не отчёт!'")
