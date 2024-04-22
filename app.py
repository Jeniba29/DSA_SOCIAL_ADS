from flask import Flask,render_template,request
import pickle

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        estimatedsalary =int(request.form['estimatedsalary'])

        model = pickle.load(open('model.pkl','rb'))

        prediction= model.predict([[(gender,age,estimatedsalary)]])
        print(prediction[0])

    return render_template('prediction.html',target=prediction[0])
    
if __name__ =='__main__':

   app.run(port=5002,debug=True)