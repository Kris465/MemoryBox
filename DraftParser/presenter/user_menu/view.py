from domain.chapter_class import Chapter
from domain.project_class import Project


class View:

    def get_info(self, arg):
        return input(arg)

    def ask_user(self, title):
        field_names = ["English name", "Original name", "Russian name",
                       "Rulate", "Language", "URL", "Current chapter"]
        field_values = []
        for field_name in field_names:
            field_value = input(f"Enter the {field_name} of the project: ")
            field_values.append(field_value)

        english_name, original_name, russian_name, \
            rulate, language, url, current_chapter = field_values

        chapter = Chapter(ordinal_number=current_chapter,
                          link=input("Chapter link: "),
                          language=language,
                          original_text='',
                          russian_text='')
        chapters = []
        chapters.append(chapter)

        project = Project(original_name=original_name,
                          english_name=english_name,
                          russian_name=russian_name,
                          rulate=rulate,
                          language=language,
                          url=url,
                          chapters=chapters,
                          current_chapter=current_chapter
                          )
        return project
