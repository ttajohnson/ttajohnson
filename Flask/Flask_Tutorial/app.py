# Import the Flask Framework
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

### Define Routes and Views

# # Route
# @app.route("/")

# # Views
# def index():
#     return "Hello, via Flask!"

@app.route("/")
def index():
    return render_template('index.html')

if  __name__ == "__main__":
    app.run()

