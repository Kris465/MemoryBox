def generate_joke(hero):
    line = f"Почему {hero} никогда ничего не теряет?"
    line2 = "Потому что у него есть супер-сила!"
    return line, line2


print(*generate_joke("Супермен"))
