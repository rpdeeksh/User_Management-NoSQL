from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import get_db
from bson.objectid import ObjectId

app = Flask(__name__)
db = get_db()

@app.route("/")
def index():
    users = list(db.find())
    return render_template("index.html", users=users)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = int(request.form["age"])
        db.insert_one({"name": name, "email": email, "age": age})
        return redirect(url_for("index"))

@app.route("/edit_user", methods=["GET", "POST"])
def edit_user():
    if request.method == "POST":
        user_id = request.form["user_id"]
        user = db.find_one({"_id": ObjectId(user_id)})
        if user:
            return render_template("edit_user.html", user=user)
        else:
            return render_template("edit_user.html", users=list(db.find()), error="User not registered.")
    return render_template("edit_user.html")

@app.route("/update_user/<id>", methods=["POST"])
def update_user(id):
    updated_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "age": int(request.form["age"])
    }
    db.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return redirect(url_for("index"))

@app.route("/delete_user/<id>", methods=["POST"])
def delete_user(id):
    db.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
