from flask import Flask, render_template, request
from core.model import predict_risk
from core.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        bp = int(request.form['bp'])
        heart_rate = int(request.form['heart_rate'])
        comorbidity_score = int(request.form['comorbidity_score'])
        input_data = {
            'age': age,
            'bp': bp,
            'heart_rate': heart_rate,
            'comorbidity_score': comorbidity_score
        }
        risk, prob = predict_risk(input_data)
        return render_template('result.html', risk=risk, probability=f"{prob:.2f}")
    except Exception as e:
        return render_template('result.html', risk="Error", probability=str(e))

if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask, render_template, request
# import pandas as pd
# from core.model import train_model, predict_risk
# # from model import train_model, predict_risk
# import matplotlib.pyplot as plt
# import os

# app = Flask(__name__)

# # Load and preprocess the dataset
# df = pd.read_csv('healthcare_dataset.csv')

# # Train the model
# model = train_model(df)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extract features from form
#     features = {
#         'Age': int(request.form['age']),
#         'Gender': request.form['gender'],
#         'Blood Type': request.form['blood_type'],
#         'Medical Condition': request.form['medical_condition'],
#         'Test Results': request.form['test_results']
#     }
#     risk_score, risk_level = predict_risk(model, features)
#     return render_template('index.html', risk_level=risk_level)

# @app.route('/dashboard')
# def dashboard():
#     # Generate visualizations
#     billing_by_condition = df.groupby('Medical Condition')['Billing Amount'].sum()
#     billing_by_condition.plot(kind='bar')
#     plt.title('Total Billing Amount by Medical Condition')
#     plt.xlabel('Medical Condition')
#     plt.ylabel('Total Billing Amount')
#     plt.tight_layout()
#     plt.savefig('static/billing_by_condition.png')
#     plt.clf()

#     admission_types = df['Admission Type'].value_counts()
#     admission_types.plot(kind='pie', autopct='%1.1f%%')
#     plt.title('Admission Types Distribution')
#     plt.ylabel('')
#     plt.tight_layout()
#     plt.savefig('static/admission_types.png')
#     plt.clf()

#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request
# import pandas as pd
# import plotly.express as px
# import os

# app = Flask(__name__)

# # Load dataset
# DATA_PATH = os.path.join(os.path.dirname(__file__), 'healthcare_dataset.csv')
# df = pd.read_csv(DATA_PATH, parse_dates=['Date of Admission', 'Discharge Date'])

# @app.route('/', methods=['GET', 'POST'])
# def dashboard():
#     # Bar chart: Number of patients per hospital
#     hospital_counts = df['Hospital'].value_counts().reset_index()
#     hospital_counts.columns = ['Hospital', 'Patient Count']
#     bar_fig = px.bar(hospital_counts, x='Hospital', y='Patient Count', title='Patients per Hospital')

#     # Pie chart: Distribution of medical conditions
#     condition_counts = df['Medical Condition'].value_counts().reset_index()
#     condition_counts.columns = ['Medical Condition', 'Count']
#     pie_fig = px.pie(condition_counts, names='Medical Condition', values='Count', title='Medical Condition Distribution')

#     # Convert plots to HTML
#     bar_chart = bar_fig.to_html(full_html=False)
#     pie_chart = pie_fig.to_html(full_html=False)

#     # Handle allocation form submission
#     allocation_message = ''
#     if request.method == 'POST':
#         patient_name = request.form.get('patient_name')
#         room_number = request.form.get('room_number')
#         # Implement allocation logic here
#         allocation_message = f'Allocated Room {room_number} to {patient_name}.'

#     return render_template('dashboard.html', bar_chart=bar_chart, pie_chart=pie_chart, message=allocation_message)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask
# from core.routes import routes

# app = Flask(__name__)
# app.register_blueprint(routes)

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask
# from core.routes import routes

# app = Flask(__name__)
# app.register_blueprint(routes)

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, render_template, request
# from core.routes import init_routes
# import joblib
# import pandas as pd

# app = Flask(__name__)
# init_routes(app)

# model = joblib.load("risk_model.joblib")

# def risk_score(patient_data):
#     df = pd.DataFrame([patient_data])
#     return float(model.predict_proba(df)[0][1])

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         fever = int(request.form.get('fever', 0))
#         bp_low = int(request.form.get('bp_low', 0))
#         diabetes = int(request.form.get('diabetes', 0))

#         features = {'fever': fever, 'bp_low': bp_low, 'diabetes': diabetes}
#         risk_prob = risk_score(features)
#         risk_label = "High" if risk_prob >= 0.5 else "Low"

#         return render_template('result.html', risk=risk_label, probability=f"{risk_prob:.2f}")
#     except Exception as e:
#         return render_template('result.html', risk=f'Error: {str(e)}', probability="N/A")

# if __name__ == "__main__":
#     print("🚀 Server running at http://127.0.0.1:5000")
#     app.run(debug=True)



# from flask import Flask, render_template, request
# import joblib
# import pandas as pd
# from core.routes import init_routes

# app = Flask(__name__)
# init_routes(app)

# # Load the trained model
# model = joblib.load(r"C:\Users\Saumya Sati\Desktop\project\OS\core\risk_model.joblib")
# def risk_score(patient_data):
#     df = pd.DataFrame([patient_data])
#     return float(model.predict_proba(df)[0][1])

# @app.route('/')
# def home():
#     return render_template('index.html')

# # ...rest of your code...

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract features from form (checkboxes or similar)
#         fever = int(request.form.get('fever', 0))
#         bp_low = int(request.form.get('bp_low', 0))
#         diabetes = int(request.form.get('diabetes', 0))

#         features = {
#             'fever': fever,
#             'bp_low': bp_low,
#             'diabetes': diabetes
#         }

#         risk_prob = risk_score(features)
#         risk_label = "High" if risk_prob >= 0.5 else "Low"
#         return render_template('result.html', risk=risk_label, probability=f"{risk_prob:.2f}")
#     except Exception as e:
#         return render_template('result.html', risk=f'Prediction error: {str(e)}', probability="N/A")

# if __name__ == "__main__":
#     print("🚀 Hospital Resource Management System running at http://127.0.0.1:5000")
#     app.run(debug=True)


# # app.py
# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# import joblib

# model = joblib.load("risk_model.joblib")

# def risk_score(patient_data):
#     import pandas as pd
#     df = pd.DataFrame([patient_data])
#     return float(model.predict_proba(df)[0][1])


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Predict
#     if model is None:
#         # Show a user-friendly message if the model is missing
#         return render_template('result.html', risk='Model file not found. Please contact the administrator.')

#     try:
#         # Extract features from form
#         features = [
#             int(request.form['age']),
#             int(request.form['bp_high']),
#             int(request.form['bp_low']),
#             int(request.form['diabetes'])
#         ]

#         # Predict
#         risk = model.predict([features])[0]
#         return render_template('result.html', risk='High' if risk == 1 else 'Low')
#     except Exception as e:
#         # Handle any unexpected errors gracefully
#         return render_template('result.html', risk=f'Prediction error: {str(e)}')



# from flask import Flask
# from core.routes import init_routes

# app = Flask(__name__)
# init_routes(app)

# if __name__ == "__main__":
#     print("🚀 Hospital Resource Management System running at http://127.0.0.1:5000")
#     app.run(debug=True)
