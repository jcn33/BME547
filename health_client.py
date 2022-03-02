import requests

server = "http://127.0.0.1:5000"

new_patient = {"name": "Jack Nastas", "id": 102, "blood_type": "O-"}

r = requests.get(server + "/")
print(r.status_code)
print(r.text)

r = requests.post(server + "/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_patient_name/102")
print(r.status_code)
print(r.text)
