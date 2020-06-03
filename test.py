# -*- coding: cp1251 -*-
from sqlalchemy.orm import sessionmaker
from models import *

# Открываем базу данных 
engine = create_engine('sqlite:///myuniverdb.db')
Session = sessionmaker(bind=engine)
session = Session()

# Делаем тестовые запросы
len1 = len(session.query(Student).join(Exam_record).all())
len2 = len(session.query(Exam_record).join(Exam).filter(Exam.discipline.like('Math')).all())
len3 = len(session.query(Exam_record).join(Exam).join(Staff).filter(Staff.last_name.like('Gavrilova')).all())

# Печатаем результат для проверки
print(len1*len2*len3)
