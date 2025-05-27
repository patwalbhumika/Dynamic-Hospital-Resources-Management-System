from flask import Blueprint, render_template, request, jsonify
from core.model import predict_risk
from core.resource_manager import ResourceManager

routes = Blueprint("routes", __name__)
manager = ResourceManager()

@routes.route("/dashboard")
def dashboard():
    status = manager.status()
    return render_template("dash.html", patients=status["patients"], available=status["available"])

@routes.route("/status")
def status():
    return jsonify(manager.status())

@routes.route("/allocate", methods=["POST"])
def allocate():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    bp = data.get("bp")
    heart_rate = data.get("heart_rate")
    comorbidity_score = data.get("comorbidity_score")
    input_data = {
        "age": age,
        "bp": bp,
        "heart_rate": heart_rate,
        "comorbidity_score": comorbidity_score
    }
    risk, prob = predict_risk(input_data)
    patient = {"name": name, "risk": risk, "prob": prob}
    success, message = manager.allocate(patient)
    return jsonify({"success": success, "message": message})

@routes.route("/emergency", methods=["POST"])
def emergency():
    data = request.get_json()
    name = data.get("name")
    # For demo, you can use dummy values or ask for more info
    patient = {"name": name, "risk": 1, "prob": 1.0}
    success, message = manager.emergency(patient)
    return jsonify({"success": success, "message": message})


