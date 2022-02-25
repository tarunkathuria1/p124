from flask import Flask,jsonify, request

app = Flask(__name__)

datas = [
    {
        'id': 1,
        'contact': '9987644456',
        'name': 'Raju', 
        'done': False
    },
    {
        'id': 2,
        'contact': ' 9876543222',
        'name': 'Rahul', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    data = {
        'id': datas[-1]['id'] + 1,
        'contact': request.json['contact'],
        'name': request.json.get('name', ""),
        'done': False
    }
    datas.append(data)
    return jsonify({
        "status":"success",
        "message": "data added succesfully!"
    })
    

@app.route("/get-data")
def get_data():
    return jsonify({
        "data" : datas
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)