from flask import Flask, request, jsonify

app = Flask(__name__)

# simple memory database
users = {}

# get user info
@app.route("/user")
def user():
    uid = request.args.get("uid")

    if uid not in users:
        users[uid] = {"points": 0}

    return jsonify(users[uid])

# tap system
@app.route("/tap", methods=["POST"])
def tap():
    uid = request.json["uid"]

    if uid not in users:
        users[uid] = {"points": 0}

    users[uid]["points"] += 1

    return jsonify(users[uid])

# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
