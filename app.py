from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Model
class Todos(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(400), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'{self.title} - {self.description}'


# Add Todo Endpoint
@app.route('/', methods = ['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        title = request.form['title']
        descripion = request.form['description']
        todo = Todos(title = title, description = descripion)
        db.session.add(todo)
        db.session.commit()

    all_todo = Todos.query.all()
    return render_template('index.html', all_todo = all_todo)


# Update Todo Endpoint
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def updateTodo(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        todo = Todos.query.filter_by(sno=id).first()
        todo.title = title
        todo.description = description
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todos.query.filter_by(sno=id).first()
    return render_template('update.html', todo = todo)


# Delete Todo Endpoint
@app.route('/delete/<int:id>')
def deleteTodo(id):
    todo = Todos.query.filter_by(sno=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)