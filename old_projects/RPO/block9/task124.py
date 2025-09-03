def correct_errors():
    corrections = {
        "прроцесор": "процессор",
        "теекстовыйфайл": "текстовый файл",
        "програма": "программа",
        "аллгоритм": "алгоритм",
        "процесор": "процессор",
        "паммять": "память"
    }
    
    for error, correction in corrections.items():
        print(f"Исправлено: '{error}' -> '{correction}'")

correct_errors()
