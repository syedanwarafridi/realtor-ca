from flask import Flask, request, jsonify
from financial_model import financial_ai_model
from csv_agent import csv_ai_chatbot
import json
import re

app = Flask(__name__)

@app.route('/financial-analyzer', methods=['POST'])
def analyze_finances():
    data = request.json
    salary = data.get('salary', 0)
    rental_income = data.get('rental_income', 0)
    rent_or_mortgage = data.get('rent_or_mortgage', 0)
    utilities = data.get('utilities', 0)
    insurance = data.get('insurance', 0)
    subscriptions = data.get('subscriptions', 0)
    groceries = data.get('groceries', 0)
    transportation = data.get('transportation', 0)
    entertainment = data.get('entertainment', 0)
    cc_payment = data.get('cc_payment', 0)
    cc_interest = data.get('cc_interest', 0.0)
    student_loan_payment = data.get('student_loan_payment', 0)
    student_loan_interest = data.get('student_loan_interest', 0.0)
    savings_account = data.get('savings_account', 0)
    retirement = data.get('retirement', 0)
    house_price = data.get('house_price', 0)
    down_payment = data.get('down_payment', 0)
    loan_amount = data.get('loan_amount', 0)
    annual_interest_rate = data.get('annual_interest_rate', 0.0)
    loan_term_years = data.get('loan_term_years', 0)

    result = financial_ai_model(salary, rental_income, rent_or_mortgage, utilities, insurance, subscriptions, groceries, transportation, entertainment, cc_payment, cc_interest, student_loan_payment, student_loan_interest, savings_account, retirement, house_price, down_payment, loan_amount, annual_interest_rate, loan_term_years)
    result = json.loads(result)
    return jsonify(result)


#------------- CSV AGENT -------------#
@app.route('/csv-chatbot', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get("query", "")
    
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Call the chatbot function
        response = csv_ai_chatbot(user_query)
    except Exception as e:
        response = f"Error: {str(e)}"
        
    pattern = r"'output':\s*'(.*?)'}$"

    # Use re.search to find the match
    match = re.search(pattern, response, re.DOTALL)
    
    # Check if a match was found and print the result
    if match:
        output_text = match.group(1)
    else:
        output_text = response

    return jsonify({"response": output_text})

if __name__ == '__main__':
    app.run(debug=True)
