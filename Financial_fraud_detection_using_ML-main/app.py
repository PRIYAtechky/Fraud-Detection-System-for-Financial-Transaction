from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the saved scaler, model, and column names
with open(r'C:\Users\Badmapriya S\Desktop\Financial_fraud_detection_using_ML-main\Financial_fraud_detection_using_ML-main\scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open(r'C:\Users\Badmapriya S\Desktop\Financial_fraud_detection_using_ML-main\Financial_fraud_detection_using_ML-main\xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open(r'C:\Users\Badmapriya S\Desktop\Financial_fraud_detection_using_ML-main\Financial_fraud_detection_using_ML-main\column_names.pkl', 'rb') as file:
    column_names = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = {
            'step': [float(request.form['step'])],
            'amount': [float(request.form['amount'])],
            'oldbalanceOrg': [float(request.form['oldbalanceOrg'])],
            'newbalanceOrig': [float(request.form['newbalanceOrig'])],
            'oldbalanceDest': [float(request.form['oldbalanceDest'])],
            'newbalanceDest': [float(request.form['newbalanceDest'])],
            'type_CASH_OUT': [int(request.form.get('type') == 'CASH_OUT')],
            'type_DEBIT': [int(request.form.get('type') == 'DEBIT')],
            'type_PAYMENT': [int(request.form.get('type') == 'PAYMENT')],
            'type_TRANSFER': [int(request.form.get('type') == 'TRANSFER')]
        }
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Standardize numerical variables
        numerical_variables = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
        df[numerical_variables] = scaler.transform(df[numerical_variables])
        
        # Ensure all columns are present in the DataFrame
        df = df.reindex(columns=column_names, fill_value=0)
        
        # Predict the result
        prediction = model.predict(df)
        result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
    except Exception as e:
        result = str(e)

    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)


