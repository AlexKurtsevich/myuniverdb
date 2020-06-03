# -*- coding: cp1251 -*-
import os, random, string

# declarative_base, sessionmaker, create_engine + SQLAlchemy datatypes

from sqlalchemy import create_engine # database engine
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey # SQLAlchemy datatypes
from sqlalchemy.orm import relationship # SQLAlchemy relationships

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() # create Base class for the Object-Relational Mapping.

from sqlalchemy.orm import sessionmaker # import session maker

DB_NAME = 'myuniverdb.db'

class Exam(Base):
    '''
    Class for Exams
    It contains the id, teacher's id and discipline
    '''
    
    __tablename__ = 'Exam'
    
    id = Column('id', Integer, primary_key=True)
    discipline = Column('discipline', String(255))
    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'))
    
    exam_records = relationship('Exam_record')
    staff = relationship('Staff', foreign_keys=[staff_id])
    
    @property
    def student(self):
        students = set([record.student for record in self.exam_records])
        student.discard(None)
        return list(students)
        
    @property
    def HR(self):
        HR_rec = set([staffs.HR for staff in self.staff])
        HR_rec.discard(None)
        return list(HR_rec)
        	
    def __repr__(self):
        return self.discipline

class Exam_record(Base):
    '''
    Which exams each student passed
    '''
    
    __tablename__ = 'Exam_record'

    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('Student.id'))
    exam_id = Column('exam_id', Integer, ForeignKey('Exam.id'))
    date = Column('date', String(255))
    grade = Column('grade', Integer)
    
    exam = relationship('Exam', foreign_keys=[exam_id])
    student = relationship('Student', foreign_keys=[student_id])
    
    @property
    def staff(self):
        staffs = set([exams.staff for exams in self.exam])
        staffs.discard(None)
        return list(staffs)
        
    @property
    def FGroup(self):
        group = set([stud.fgroup for stud in self.student])
        group.discard(None)
        return list(group)
    
class Student(Base):
    '''
    Class for Student. Stores minimal information about 
    student such as first and last name.
    '''
    
    __tablename__ = 'Student'
    
    id = Column('id', Integer, primary_key=True)
    group_id = Column('group_id', Integer, ForeignKey('FGroup.id'))
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))
    
    exam_record = relationship('Exam_record')
    fgroup = relationship('FGroup', foreign_keys=[group_id])
    
    @property
    def exam(self):
        exams = set([exam_rec.exam for exam_rec in self.exam_record])
        exams.discard(None)
        return list(exams)
        
    @property
    def Facult(self):
        facult = set([group.faculty for group in self.fgroup])
        facult.discard(None)
        return list(facult)
    
    def __repr__(self):
        return '%s %s'%\
            (self.first_name, self.last_name)

class FGroup(Base):
    '''
    
    '''
    
    __tablename__ = 'FGroup'
    
    id = Column('id', Integer, primary_key=True)
    number = Column('number', Integer)
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'))
    
    student = relationship('Student')
    faculty = relationship('Faculty', foreign_keys=[faculty_id])
    
    def __repr__(self):
        return '%d' %\
               (self.number)
        

class Faculty(Base):
    '''
    
    '''
    
    __tablename__ = 'Faculty'
    
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    
    group = relationship('FGroup')
    hr = relationship('HR_record')
    
    @property
    def staff(self):
        staffs = set([hr_rec.staff for hr_rec in self.hr])
        staffs.discard(None)
        return list(staffs)
        
    @property
    def Stud(self):
        stud = set([groups.student for groups in self.group])
        stud.discard(None)
        return list(stud)
    
    def __repr__(self):
        return '%s' %\
               self.name

class HR_record(Base):
    '''
    
    '''
    
    __tablename__ = 'HR_record'

    id = Column('id', Integer, primary_key=True)
    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'))
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'))
    position = Column('position', String(255))
    
    staff = relationship('Staff', foreign_keys=[staff_id])
    faculty = relationship('Faculty', foreign_keys=[faculty_id])
    
    @property
    def Exam(self):
        exams = set([staffs.exam for staffs in self.staff])
        exams.discard(None)
        return list(exams)

class Staff(Base):
    '''
    
    '''
    
    __tablename__ = 'Staff'
    
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))
    
    HR = relationship('HR_record')
    exam = relationship('Exam')
    
    @property
    def Facultets(self):
        facultets = set([hr.faculty for hr in self.HR])
        facultets.discard(None)
        return list(facultets)
    
    def __repr__(self):
         return '%s %s'%\
            (self.first_name, self.last_name) 

engine = create_engine('sqlite:///%s'%DB_NAME,echo=False)
            
if os.path.isfile(DB_NAME): # if found the database file, just connect to it
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session.query(Student).all()) # print test query
else: # if database file is absent, create an empty file with the DB schema
    Base.metadata.create_all(engine)
