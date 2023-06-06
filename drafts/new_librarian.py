from parser_class import Parser
from modules.writer_to_json import write


def new_librarian():
    title = 'She was sent by God'
    chapter = 1
    link = 'https://mesmerizingmemoirs.com/novel/she-was-sent-by-god/ss-01/'
    tag = 'div'
    class_ = "entry-content"
    all_chapters = {}
    temp_dict = {title: link}

    while True:
        link = f'https://mesmerizingmemoirs.com/novel/she-was-sent-by-god/ss-{chapter}/'
        parser = Parser(link, tag, class_)
        result = parser.parse()
        temp_dict = {chapter: i.text for i in result}
        print(temp_dict)
        chapter += 1
        print(chapter)
        all_chapters.update(temp_dict)

    write(title, all_chapters)


new_librarian()
