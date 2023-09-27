from flask import Flask, request, jsonify
import csv
global count 
count =1
app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    # Save data to a CSV file
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data["name"], data["age"], data["gender"]])
    global count
    x="OP :"+str(count)+"\n",'Name :'+data["name"]+"\n", "Age :"+ data["age"]+'\n', "Gender :"+data["gender"] + '\n'
    count += 1
    with open("file.txt",'w') as f:
        f.writelines(x)
    return jsonify({"success": True})

if __name__ == "_main_":
    app.run(debug=True)