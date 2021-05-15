from flask import Response, request
from database.models import students
from flask_restful import Resource

class StudentsAPI(Resource):

    def get(self):
        student = students.objects().to_json()
        return Response(student, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        student = students(**body).save()
        identification = student.student_id
        return {'id' : int(identification)}, 200

class SingleStudentAPI(Resource):

    def get(self, id):
        student = students.objects.get(student_id=id).to_json()
        return Response(student, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        students.objects.get(student_id=id).update(**body)
        return 'Student Updated', 200
    
    def delete(self, id):
        students.objects.get(student_id=id).delete()
        return Response('Student Deleted Successfully', mimetype="application/json", status=200)