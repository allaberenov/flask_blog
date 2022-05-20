import flask

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base.db'
app.config['SQLAACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(500), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
