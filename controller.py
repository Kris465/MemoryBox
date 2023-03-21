import getter_chapter
import writer

def logic():
    URL = input("URL:")
    running(URL, 0)

def running(URL, number):
    text = getter_chapter.getter_chapter(URL)
    print(text)
    if '[ Next ]' or '[Next]' in text:
        number = int(URL[-2])
        writer.write(URL + text, number)
        URL = URL[0:-2] + str(number + 1) + "/"
        running(URL, number)
        print("Done!")
