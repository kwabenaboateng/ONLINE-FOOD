#from flask import Flask, render_template, request
#import pandas as pd
#import numpy as np
#import pickle
#import streamlit

#app = Flask(__name__)

# Load the pre-trained model
#model = pickle.load(open('model.pkl', 'rb'))

#@app.route('/')
#def home():
    #return render_template('index.html')

#@app.route('/predict', methods=['POST'])
#def predict():
    # Get user input from the form
    #age = int(request.form['age'])python app.py
    #monthly_income = int(request.form['monthly_income'])
    #family_size = int(request.form['family_size'])

    # Make prediction using the model
    prediction = model.predict([[age, monthly_income, family_size]])

    # Map prediction to human-readable output
   # output = "Satisfied" if prediction[0] == 1 else "Not Satisfied"

    #return render_template('index.html', prediction_text='Customer is {}'.format(output))

#if __name__ == '__main__':
#    app.run(debug=True)


from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__prediction__)

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    age = int(request.form['age'])
    monthly_income = int(request.form['monthly_income'])
    family_size = int(request.form['family_size'])

    # Make prediction using the model
    prediction = model.predict([[age, monthly_income, family_size]])

    # Map prediction to human-readable output
    output = "Satisfied" if prediction[0] == 1 else "Not Satisfied"

    return render_template('index.html', prediction_text='Customer is {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)





# Add description and title
st.write("""
# Online Food Feedback App
""")

# Add image
image = st.image("images.png", width=200)

# Get user input
text = st.text_input("Type here:")
button = st.button('Analyze')

# Define the CSS style for the app
st.markdown(
"""
<style>
body {
    background-color: #f5f5f5;
}
h1 {
    color: #4e79a7;
}
</style>
""",
unsafe_allow_html=True
) 
