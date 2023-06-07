import asyncio
from presenter import Presenter
from view import View

view = View()
presenter = Presenter(view)
view.presenter = presenter


async def main():
    await view.start()

    while True:
        nickname, name = await view.get_user_input()
        presenter.add_user(nickname=nickname, name=name)

if __name__ == '__main__':
    asyncio.run(main())
