from flask import Flask, render_template, request, redirect
from jsondb import JsonDB

app=Flask(__name__)
db = JsonDB('db.json')
db.load()

@app.route('/', methods=['GET', 'POST'])

def index():
    todo = db.get('todos')
    if request.method == 'POST':
        task = request.form['input_text']
        priority = request.form['priority']
        new_task = {'text':task, 'priority':priority}
        todo.append(new_task)
        db.set('todos', todo)
        db.save()
        return redirect('/')
    return render_template('index.html', todo = todo)

app.run(debug=True)

