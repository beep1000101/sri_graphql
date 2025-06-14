from flask_sqlalchemy import SQLAlchemy

from models.enums import NinjaRank, KekkeiGenkai

db = SQLAlchemy()


class Ninja(db.Model):
    __tablename__ = 'ninjas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    rank = db.Column(NinjaRank, nullable=False, default=NinjaRank.GENIN)
    kekkei_genkai = db.Column(
        KekkeiGenkai,
        nullable=False,
        default=KekkeiGenkai.NONE
    )
    is_cool = db.Column(db.Boolean, default=False)
    village_id = db.Column(db.Integer, db.ForeignKey(
        'village.id'), nullable=False)
    village = db.relationship('Village', backref='ninjas')

    def __repr__(self):
        return f'<Ninja {self.name}>'
