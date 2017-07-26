# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug import secure_filename
from kerasmodel import catdogclassifier

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET','POST'])
def form():
    return render_template('form_submit.html')

    
@app.route('/uploadcomplete', methods = ['GET', 'POST'])
def upload_complete():
    
    f = request.files['file']
    f.save('static/images/' + secure_filename(f.filename))

    imgpred = catdogclassifier('static/images/' + secure_filename(f.filename))
    if imgpred[0] == [[1]]:
        imgclass="dog"
    else: 
        imgclass="cat"


    return render_template('file_uploading.html', filename=secure_filename(f.filename), imgclass=imgclass)

# Run the app :)
if __name__ == '__main__':
    app.run()
