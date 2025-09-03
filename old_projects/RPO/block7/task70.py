def min_population_density(populations, areas):
    densities = [population / area for population, area in zip(populations,
                                                               areas)]
    return min(densities)


populations = [50, 100, 80]
areas = [500, 1000, 400]
result = min_population_density(populations, areas)
print(f"Минимальная плотность населения: {result:.2f} млн/тыс. км²")
