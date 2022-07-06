import randoms
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
object = randoms.Randoms()
# pword = []


@app.route('/', methods=('GET', 'POST'))
def index():
    
    if request.method == 'POST':
        uppers = int(request.form['uppercase'])
        lowers = int(request.form['lowercase'])
        nums = int(request.form['numbers'])
        special = int(request.form['special'])
        password = object.random_password(uppers, lowers, nums, special)
        # pword.append(password)
        return render_template('user.html', ps=password)

    return render_template('index.html')

# @app.route('/user.html', methods=['GET'])
# def user():

#     ps = pword[0]
#     # print('password', pword)
#     return render_template('user.html', ps=ps)


app.run(debug=True)

