from flask import Flask,render_template,request,url_for, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def function1():
    return render_template('login.html')

@app.route('/<string:page_name>')
def function2(page_name):
    return render_template(page_name)

def write_to_file(datas):
    with open('data.txt',mode='a') as data:
        username = datas['username']
        file = data.write(f'\n{username}')

def write_to_csv(datas):
    with open('datas.csv',mode='a',newline='') as data2:
        username = datas['username']
        csv_writer = csv.writer(data2,delimiter = ',',quotechar='"',quoting = csv.QUOTE_MINIMAL)

        csv_writer.writerow([username])

@app.route('/submit_form',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        print(data)
        return redirect('submit.html')