def display_powers(hero, powers):
    print(f"Способности супергероя {hero}")
    for power in powers:
        print(f" - {power}")


powers = ["Сила", "Полет", "Невидимость"]
display_powers("Чудо-женщина", powers)
