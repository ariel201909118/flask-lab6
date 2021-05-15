from .db import db

class students(db.Document):
    student_id = db.IntField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    gender = db.StringField(required=True)
    course_studied = db.ListField(required=True)
    program_name = db.StringField(required=True)
    MCIT_second_program = db.BooleanField(required=True) 
    