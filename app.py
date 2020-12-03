from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import face_recognition

app=Flask(__name__)
app.static_folder = 'static'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
# db= SQLAlchemy(app)

class first(db.Model): 
    id= db.Column(db.Integer, primary_key= True)

    def __repr__(self):
        return '<Image %r>' % self.id


@app.route('/upload_image', methods=["GET", "POST"])
def index():

    
    if request.method == "POST":

        if request.files: #unique storage

            image1 = request.files['image1']
            image2 = request.files['image2']

            
            first= face_recognition.load_image_file(image1)
            first_encoding = face_recognition.face_encodings(first)[0]

            second= face_recognition.load_image_file(image2)
            second_encoding = face_recognition.face_encodings(second)[0]

            result= face_recognition.compare_faces([first_encoding], second_encoding)

            if result[0]:
                
                res="The faces are similar"
                return render_template("index.html", res=res, img=image1, img1=image2)
               
            else:
                res="Sed, not similar"
                return render_template("index.html", res=res)

            #return redirect(request.url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
