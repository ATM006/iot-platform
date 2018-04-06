from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

 
students = []
 
@app.route('/student/', methods=['POST'])
def add_student():
	abort(400)
	student = {
        'name' : request.json['name'],
        'grade' : request.json['grade']
    }
	students.append(student)
	
	print(students)
	return "success"

if __name__ == '__main__':
	app.run(debug=False)

