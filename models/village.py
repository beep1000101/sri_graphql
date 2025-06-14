from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Village(db.Model):
    __tablename__ = 'villages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    leader_name = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Village {self.name}>'
