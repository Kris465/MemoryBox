def calcukate_yield(initial_yield, area_increase, yield_decrease):
    final_area = initial_yield * (1 + area_increase)
    final_yield = initial_yield * (1 - yield_decrease)
    return final_yield

initial_yield = 29
area_increase = 0.03
yield_decrease = 0.03
final_yield = calcukate_yield(initial_yield, area_increase, yield_decrease)
print("Урожайность в этом году: {:.2f} центнеров с гектара".format(final_yield))
