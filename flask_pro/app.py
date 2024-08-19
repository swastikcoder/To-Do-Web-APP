from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    desc_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

@app.route('/')
def hello_world():
    return render_template('index.html')




@app.route('/product')
def product():
    return '<h1> this is products page </h1>'


if __name__ == '__main__':
    app.run(debug = True)