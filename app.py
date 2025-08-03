from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("model/model.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        img_file = request.files["image"]
        if img_file:
            img_path = os.path.join("static", img_file.filename)
            img_file.save(img_path)

            img = image.load_img(img_path, target_size=(150, 150))
            img_tensor = image.img_to_array(img)
            img_tensor = np.expand_dims(img_tensor, axis=0) / 255.0

            prediction = model.predict(img_tensor)
            result = "PNEUMONIA" if prediction[0][0] > 0.5 else "NORMAL"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
