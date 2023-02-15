import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Create an account on https://firebase.google.com/ then use your own credentials

cred = credentials.Certificate("serviceAccountKey.json") #download your own account key file

firebase_admin.initialize_app(cred, {
    "databaseURL" : "" #add your own URL
})

ref = db.reference('Students')

data = {
    "100":
        {
            "name": "Ana D Armas",
            "major": "Dramatics",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-12 23:24:34"
        },
    # "101":   // No need for this image (or) add another image named "101.png" then use
    #     {
    #         "name": "Rishabh",
    #         "major": "AI",
    #         "starting_year": 2020,
    #         "total_attendance": 12,
    #         "standing": "G",
    #         "year": 3,
    #         "last_attendance_time": "2023-02-15 23:24:34"
    #     },
    "102":
        {
            "name": "MS Dhoni",
            "major": "Cricket",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-12 23:24:34"
        },
    "103":
        {
            "name": "Elon Musk",
            "major": "AI",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-12 23:24:34"
        },
    "104":
        {
            "name": "Sundar Pichai",
            "major": "Management",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-12-12 23:24:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)