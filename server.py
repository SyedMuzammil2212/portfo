from flask import Flask,render_template
from flask import request,url_for,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_tofile(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        
        file=database.write(f'\n {email},{subject} \n {message} \n')

def write_tocsv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        
        csv_writer=csv.writer(database2,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_tocsv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'