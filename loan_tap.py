from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/')
def ping():

    return '<H1>loan approval application</H1>'

pickle_in = open('classifier.pkl', 'rb')
clf=pickle.load(pickle_in)

@app.route('/predict',methods=['POST'])
def predict():
    loan_req=request.get_json(force=True)
    print(loan_req)

    if loan_req['Gender']=='Male':
        Gender=0
    else:
        Gender=1

    if loan_req['Married']=='Unmarried':
        Married=0
    else:
        Married=1

    ApplicantIncome=loan_req['ApplicantIncome']
    LoanAmount=loan_req['LoanAmount']
    Credit_History=loan_req['Credit_History']

    result=clf.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])

    if result==0:
        pred='Rejected'

    else:
        pred='Accepted'

    return {'Loan_approval_status:':pred}
