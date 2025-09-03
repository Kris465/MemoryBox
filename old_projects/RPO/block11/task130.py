scores = [1, 3, 1, 0, 3, 0]

try:
    first_win_index = scores.index(3)
except ValueError:
    first_win_index = None

try:
    first_loss_index = scores.index(0)
except ValueError:
    first_loss_index = None

if first_win_index is not None and first_loss_index is not None:
    if first_win_index < first_loss_index:
        print("Первый выигрыш был раньше.")
    elif first_loss_index < first_win_index:
        print("Первый проигрыш был раньше.")
    else:
        print("Выигрыш и проигрыш произошли одновременно.")
elif first_win_index is not None:
    print("Был только первый выигрыш.")
elif first_loss_index is not None:
    print("Был только первый проигрыш.")
else:
    print("В списке не было ни выигрыша, ни проигрыша.")
