import requests

def compatibility(rblood, dblood):
    if "-" in rblood and "+" in dblood:
        return "No"
    elif "B" not in rblood and "B" in dblood:
        return "No"
    elif "A" not in rblood and "A" in dblood:
        return "No"
    else:
        return "Yes"

r = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_patients/jcn33")
recip = r.json().get("Recipient")
donor = r.json().get("Donor")

rblood = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(recip)).text
dblood = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(donor)).text

match = compatibility(rblood, dblood)
out_data = {
   "Name": "jcn33",
   "Match": match
}
ans = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)