import re


def main():
    course_url = input("Введите ссылку на курс: ")
    course_id = re.search(r'\d+', course_url)
    print(course_id)


if __name__ == "__main__":
    main()
