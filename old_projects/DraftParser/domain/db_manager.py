from langdetect import detect
from domain.project_class import Project
from presenter.database.models import Chapters, Novel, Projects

from presenter.database.session import get_session


class DBManager:
    def find(title):
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
