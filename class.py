from flask import Flask,jsonify, request

# flask object - app
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': u'998764456',
        'name': u'raju', 
        'done': False
    },
    {
        'id': 2,
        'contact': u'9876543222',
        'name': u'rahul', 
        'done': False
    }
]

# GET ,POST  ,PUT , DELETE

#  127.0.0.1.5000/
@app.route("/")
def hello_world():
    return "Hello World!"

# #  127.0.0.1.5000/add-data
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
# 127.0.0.1.5000/get-data
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)