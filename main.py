from user_menu.user_menu import CustomMenu


def main():
    user_menu = CustomMenu()
    data = user_menu.run()
    print(data)


if __name__ == '__main__':
    main()
