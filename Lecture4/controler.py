import model_mult
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_mult.init(value_a, value_b)
    result = model_mult.mult()
    view.view_data(result)