from pymodm import connect
from pymodm import connect

connect("mongodb+srv://jack-nastas:ArrowHead*9@jack-1.kjtqh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def test_add_patient_to_db():
    from health_server import add_patient_to_db
    name = "Test Patient"
    p_id = 2
    blood_type = "O+"
    answer = add_patient_to_db(name, p_id, blood_type)
    answer.delete() # Only deletes on server
    assert answer.name == name
    assert answer.patient_id == p_id