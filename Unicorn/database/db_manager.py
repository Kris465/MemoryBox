from langdetect import detect
from database.db_session import get_session
from database.models import Chapters, Novel, Projects
from domain.project_class import Project


class DBManager:
    def find(self, title):
        language = detect(title)
        session = get_session()

        if language == "ru":
            novel = session.query(Novel).filter(
                Novel.russian_name == title).first()
        elif language == "en":
            novel = session.query(Novel).filter(
                Novel.english_name == title).first()
        else:
            novel = session.query(Novel).filter(
                Novel.original_name == title).first()

        if novel is None:
            return None
        else:
            db_project = session.query(Projects).filter(
                Projects.id == novel.project_id).first()

            chapters = session.query(Chapters).filter_by(
                Chapters.novel_id == novel.id).all()

            max_ordinal_number = max(
                chapter.ordinal_number for chapter in chapters)

            project = Project(original_name=novel.original_name,
                              english_name=novel.english_name,
                              russian_name=novel.russian_name,
                              rulate=db_project.rulate,
                              url=novel.webpage,
                              current_chapter=max_ordinal_number,
                              chapters=chapters)
            session.close()
            return project
