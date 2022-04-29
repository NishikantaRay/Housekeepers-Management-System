import csv
records=[
{"E-mail":"a@gmail.com","Password" :1,"contact":"","services": {}},
{"E-mail":"b@gmail.com","Password" :2,"contact":"","services": {}},
{"E-mail":"c@gmail.com", "Password":3,"contact":"","services": {}},
{"E-mail":"d@gmail.com", "Password":4,"contact":"","services": {}},
{"E-mail":"f@gmail.com", "Password":5,"contact":"","services": {}},
{"E-mail":"g@gmail.com", "Password":6,"contact":"","services": {}},
]
csvwriter= csv.writer(open("newdata.csv","w"))
csvwriter.writerow(["E-mail","Password","contact","services"])
for r in records:
    csvwriter.writerow([r])