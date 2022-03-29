from flask import Flask, request, jsonify
from pymodm import connect
from pymodm import errors as pymodm_errors
import logging

# Model in a seperate file for consistent tagging withing MongoDB database
from health_model import Patient

app = Flask(__name__)


def init_server():
    """ Initializes server conditions
    
    This function can be used for any specific tasks that you would like to run
    upon initial server start-up.  Currently, it configures the logging
    functionality and it makes a connection to a MongoDB database.
    
    Note:  As currently written, this function does not need a unit test as
    it does not do any data manipulation itself.
    """
    logging.basicConfig(filename="health_db_server.log", level=logging.DEBUG,
                        filemode='w')
    print("Connecting to database...")
    connect("mongodb+srv://jack-nastas:ArrowHead*9@jack-1.kjtqh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    print("Connection attempt finished")

@app.route("/", methods=["GET"])
def status():
    return "CONNECTION SUCCESS"


@app.route("/new_patient", methods=["POST"])
def new_patient_handler():
    """Handles requests to the /new_patient route for adding a new patient to
    server database
    
    The /new_patient route is a POST request that should receive a JSON-encoded
    string with the following format:
        
    {"name": str, "id": int, "blood_type": str}
    
    The function then calls a driver function that implements the functionality
    of this route and receives an "answer" and "status_code" from this
    driver function.  Finally, it returns the "answer" using jsonify and the
    status_code.
    
    Note: This function only does the three things that a flask handler should
    do.  1. Get data from the request. 2. Call other functions to do the
    work. 3. Return the results.  Therefore, it does not need a unit test.
    
    Returns:
        str, int: message including patient data if successfully added to the
                  database or error message if not, followed by a status code
    """
    in_data = request.get_json()
    ans, status = add_patient_driver(in_data)
    return jsonify(ans), status


def add_patient_driver(in_data):
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    answer, status_code = validate_test(in_data, expected_keys,
                                                expected_types)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    return True, 200


def add_patient_to_db(p_name, id_no, p_blood_type):
    new_p = Patient(name=p_name, patient_id=id_no, blood_type = p_blood_type)
    new_p.save()
    return new_p


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_handler(patient_id):
    """ GET route to obtain database entry for a patient by id number
    
    This function implements a GET route with a variable URL.  The desired
    patient id number is included as part of the URL.  The function calls
    another function to implement the functionality and receives an
    answer and status code from that function, which it then returns.
    
    Args:
        patient_id (str): the patient id taken from the variable URL
        
    Returns:
        str, int: An error message if patient_id was invalid or a results
        string containing the patient data, plus a status code.
    """
    answer, status_code = get_results_driver(patient_id)
    return answer, status_code


def get_results_driver(patient_id):
    answer, status_code = validate_patient_id(patient_id)
    if status_code != 200:
        return answer, status_code
    answer, status_code = get_test(answer)
    return answer, status_code


def validate_patient_id(idnum):
    try:
        nint = int(idnum)
    except ValueError:
        return "TypeError: Patient ID not an Integer", 402
    return nint, 200


def get_test(patient_id):
    try:
        patient = Patient.objects.raw({"_id": patient_id}).first()
    except pymodm_errors.DoesNotExist:
        return "Patient_id {} was not found".format(patient_id), 400
    return patient.tests, 200


def get_patient(idnum):
    try:
        patient = Patient.objects.raw({"_id": idnum}).first()
        return patient, 200
    except pymodm_errors.DoesNotExist:
        return "DatabaseError: Patient {} does not exist".format(idnum), 403


@app.route("/add_test", methods=["POST"])
def new_patient_test():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def add_test_driver(in_data):
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    answer, status_code = validate_test(in_data, expected_keys,
                                                expected_types)
    if status_code != 200:
        return answer, status_code
    answer, status_code = add_test_to_patient(in_data)
    return answer, status_code


def validate_test(in_data, expected_keys, expected_types):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_message = "Key {} is missing".format(key)
            return error_message, 400
        if type(in_data[key]) is not expected_type:
            error_message = "Value of key {} is not of type {}"\
                .format(key, expected_type)
            return error_message, 400
    return True, 200

def add_test_to_patient(in_data):
    patient, code = get_patient(in_data["id"])
    if code == 403:
        return patient, code
    test = in_data["test_name"]
    if test in patient.tests:
        patient.tests[test].append(in_data["test_result"])
    else:
        patient.tests[test] = [in_data["test_result"]]
    patient.save()
    return "Test Added", 200


if __name__ == "__main__":
    init_server()
    app.run()
    