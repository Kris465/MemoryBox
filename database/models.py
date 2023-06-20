from sqlalchemy import Date, Text, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Parser(Base):
    __tablename__ = 'parser'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(100), nullable=False)
    tag = Column(String(10), nullable=False)
    cl = Column(String(30))
    word = Column(String(10))


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(12))
    projects = relationship("Projects", back_populates="status")


class Workers(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(30), nullable=False)
    name = Column(String(12), nullable=False)
    phone = Column(String(12))
    email = Column(String(25))
    vk = Column(String(30))
    birthday = Column(Date)
    comment = Column(String(20))
    projects = relationship("Projects", back_populates='workers')


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    comment = Column(String(20))
    worker_id = Column(Integer, ForeignKey("workers.id"), nullable=False)
    rulate = Column(String(60))
    status = relationship("Status", back_populates='projects')
    workers = relationship("Workers", back_populates='projects')
    novel = relationship("Novel", back_populates='projects')


class Novel(Base):
    __tablename__ = 'novel'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    russian_name = Column(String(100), nullable=False)
    original_name = Column(String(70))
    english_name = Column(String(70))
    notes = Column(String(10))
    webpage = Column(String(80))
    strategy = Column(String(40))
    projects = relationship("Projects", back_populates='novel')
    chapters = relationship("Chapters", back_populates="novel")


class Chapters(Base):
    __tablename__ = 'chapters'
    id = Column(Integer, primary_key=True, index=True)
    novel_id = Column(Integer, ForeignKey('novel.id'), nullable=False)
    ordinal_number = Column(Integer, nullable=False)
    language = Column(String(10))
    link = Column(String(150))
    original_text = Column(Text)
    russian_text = Column(Text)
    novel = relationship("Novel", back_populates='chapters')
