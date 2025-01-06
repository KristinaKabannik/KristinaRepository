from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Student(Base):  #таблиця student
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)

    courses = relationship('Course', secondary='enrollments', back_populates='students')

class Course(Base): # Nаблиця course
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)

    students = relationship('Student', secondary='enrollments', back_populates='courses')

class Rel(Base):  # Таблиця table_rel
    __tablename__ = 'table_rel'

    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'), primary_key=True)

engine = create_engine("postgresql://kristina:kristina@localhost:5432/new_db") # Створення бд та таблиці
Base.metadata.create_all(engine)
