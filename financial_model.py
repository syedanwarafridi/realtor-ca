from openai import OpenAI

client = OpenAI(api_key="")

def financial_ai_model(salary, rental_income, rent_or_mortgage, utilities, insurance, subscriptions, groceries, transportation, entertainment, cc_payment, cc_interest, student_loan_payment, student_loan_interest, savings_account, retirement, house_price, down_payment, loan_amount, annual_interest_rate, loan_term_years):
    system_prompt = "You are a Real Estate Financial Analyzer Expert"

    # Define the prompt with the user's input
    prompt = f"""
            You are an AI financial assistant. I will provide you with detailed financial data, including income sources, expenses, debt information, savings contributions, and details about a potential house purchase. Your task is to perform calculations, analyze the data, and provide financial recommendations.

            ### Here is the data:

            - **Income Sources:**
            - Salary: {salary}
            - Rental Income: {rental_income}

            - **Fixed Expenses:**
            - Rent/Mortgage: {rent_or_mortgage}
            - Utilities: {utilities}
            - Insurance: {insurance}
            - Subscriptions: {subscriptions}

            - **Variable Expenses:**
            - Groceries: {groceries}
            - Transportation: {transportation}
            - Entertainment: {entertainment}

            - **Debt Information:**
            - Credit Card Payment: {cc_payment}
            - Credit Card Interest Rate: {cc_interest}
            - Student Loan Payment: {student_loan_payment}
            - Student Loan Interest Rate: {student_loan_interest}

            - **Savings Contributions:**
            - Savings Account Contribution: {savings_account}
            - Retirement Contribution: {retirement}

            - **House Purchase Details:**
            - House Price: {house_price}
            - Down Payment: {down_payment}
            - Loan Amount: {loan_amount}
            - Annual Interest Rate: {annual_interest_rate}
            - Loan Term in Years: {loan_term_years}

            ### Here's what you need to do:

            1. **Calculate the following:**
            - Total Monthly Income.
            - Total Monthly Expenses.
            - Total Monthly Debt Payments and Total Debt Interest.
            - Total Monthly Savings Contributions.
            - Monthly Mortgage Payment.

            2. **Create a Budget Summary:**
            - Net Monthly Income (Total Income - Total Expenses).
            - Disposable Income (Net Monthly Income - Debt Payments - Savings Contributions - Mortgage Payment).

            3. **Identify Budget Issues:**
            - Determine if there is a budget shortfall (if Disposable Income < 0).
            - Identify if there is any high-interest debt (any debt with an interest rate > 10%).

            4. **Generate Financial Recommendations:**
            - Provide tips on how to reduce variable expenses or increase income if there is a budget shortfall.
            - Suggest prioritizing the repayment of high-interest debt.
            - If disposable income is positive, recommend allocating funds to savings, mortgage prepayments, or discretionary spending.
            - Include additional tips on:
                - Opening a TFSA (Tax-Free Savings Account).
                - Investing in the stock market.
                - Home loan options for first-time buyers.

            5. **Include Client's Personal Goals:**
            - Consider client's goals for house purchasing price and down payments.
            - Suggest steps they can take to achieve these goals, such as adjusting savings contributions or exploring different loan options.

            ### Return the results as a JSON object with the following structure:

            {{
            "calculations": {{
                "total_income": <calculated_value>,
                "total_expenses": <calculated_value>,
                "total_debt_payments": <calculated_value>,
                "total_debt_interest": <calculated_value>,
                "total_savings_contributions": <calculated_value>,
                "mortgage_payment": <calculated_value>,
                "net_monthly_income": <calculated_value>,
                "disposable_income": <calculated_value>
            }},
            "issues": {{
                "budget_shortfall": <true/false>,
                "high_interest_debt": <true/false>
            }},
            "recommendations": {{
                "budget_recommendations": [
                <list_of_recommendations>
                ],
                "investment_tips": [
                "Consider opening a TFSA to save for your goals.",
                "Explore stock market investments for potential long-term growth."
                ],
                "home_loan_options": [
                <list_of_home_loan_tips>
                ],
                "personal_goals": {{
                "house_price_goal": {house_price},
                "down_payment_goal": {down_payment},
                "steps_to_achieve_goals": [
                    <list_of_steps>
                ]
                }}
            }}
            }}
            """

    # messages = [
    #     {"role": "system", "content": system_prompt},
    #     {"role": "user", "content": prompt}
    # ]

    # response = client.chat.completions.create(
    #     model='gpt-4-turbo',
    #     messages=messages,
    #     temperature=0,
    #     response_format={ "type": "json_object" },
    # )

    # json_string = response.choices[0].message.content
    static_response = {
    "calculations": {
        "disposable_income": 1601.91,
        "mortgage_payment": 898.09,
        "net_monthly_income": 3500,
        "total_debt_interest": 137.5,
        "total_debt_payments": 500,
        "total_expenses": 2500,
        "total_income": 6000,
        "total_savings_contributions": 500
    },
    "issues": {
        "budget_shortfall": False,
        "high_interest_debt": True
    },
    "recommendations": {
        "budget_recommendations": [
            "Review and possibly reduce entertainment and grocery expenses to increase savings.",
            "Consider additional income sources such as a part-time job or freelancing.",
            "Prioritize repayment of the high-interest credit card debt."
        ],
        "home_loan_options": [
            "Explore first-time homebuyer programs which may offer better interest rates or down payment assistance.",
            "Consider a shorter loan term if future income increases are expected, to save on total interest paid."
        ],
        "investment_tips": [
            "Consider opening a TFSA to save for your goals.",
            "Explore stock market investments for potential long-term growth."
        ],
        "personal_goals": {
            "down_payment_goal": 50000,
            "house_price_goal": 250000,
            "steps_to_achieve_goals": [
                "Continue saving aggressively towards the down payment.",
                "Adjust the monthly savings contribution to meet the down payment goal faster.",
                "Consult with a mortgage advisor to understand the best loan options available."
                    ]
                }
            }
        }


    return static_response
