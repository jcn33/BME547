#Health Server
#POST /new_patient
#POST /add_text
#GET /get_result/<patient_id>

from flask import Flask, request, jsonify

app = Flask(__name__)

db = []

@app.route("/", methods=["GET"])
def status():
    return "SUCCESS"


@app.route("/new_patient", methods=["POST"])
def add_patient():
    in_data = request.get_json()
    ans, status = add_patient_driver(in_data)
    return jsonify(ans), status


def add_patient_driver(in_data):
    ans, status = validate_patient(in_data)
    if status != 200:
        return ans, status
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    for i in db:
        print(i)
    return ans, status


def add_patient_to_db(name, id, blood_type):
    new_p = {"name": name, "id": id, "blood type": blood_type, "tests": {"HDL": 100}}
    db.append(new_p)
    return True


def validate_patient(in_data):
    #also check for:
    #extra info/types
    exp_keys = ["name", "id", "blood_type"]
    exp_types = [str, int, str]
    for k, t in zip(exp_keys, exp_types):
        if k not in in_data:
            return "Key {} is missing".format(k), 400
        if type(in_data[k]) is not t:
            return "Wrong input type for key: {}".format(k), 401
    return True, 200

@app.route("/get_patient_name/<idnum>", methods=["GET"])
def get_patient_name(idnum):
    name, status = id_search(idnum)
    return name, status

def id_search(idnum):
    ans, status = validate_patient_id(idnum)
    if status != 200:
        return ans, status
    for i in db:
        if i["id"] == int(idnum):
            return i["name"], 200
    return "No Match", 402

def validate_patient_id(idnum):
    try:
        int(patient_id)
    except ValueError:
        return "Patient ID not an Integer", 403
    else:
        return True, 200

def init_server():
    #logging commands & server initial data
    add_patient_to_db("Ann Ables", 101, "A+")


if __name__ == "__main__":
    init_server()
    app.run()


"""
dict = {"name": <string>,
		"patient id": <int>,
        "blood type": <string>,
        "tests": <dictionary>
"""        