from sqlalchemy import Column, Integer, String, DateTime, text
from maps.config.database import db
 
class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.String(16), nullable=False)
    userpw = db.Column(db.String(512), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(256), nullable=False, server_default=text("''"))
    email = db.Column(db.String(60), nullable=False, server_default=text("''"))
    group0 = db.Column(db.String(32), nullable=True, server_default=text("''"))
    group1 = db.Column(db.String(32), nullable=False, server_default=text("''"))
    group2 = db.Column(db.String(32), nullable=False, server_default=text("''"))
    group3 = db.Column(db.String(32), nullable=False, server_default=text("''"))
    group4 = db.Column(db.String(32), nullable=False, server_default=text("''"))
    group5 = db.Column(db.String(32), nullable=False, server_default=text("''"))
    image = db.Column(db.String(512), nullable=False, server_default=text("''"))
    group_code = db.Column(db.String(16), nullable=False, server_default=text("''"))
    authority = db.Column(db.Integer, nullable=False, server_default=text('-1'))
    leader = db.Column(db.Integer, nullable=False, server_default=text('-1'))
    token = db.Column(db.String(32), nullable=False, server_default=text("''"))
    pwd_date = db.Column(db.DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00.000000'"))
    reg_date = db.Column(db.DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00.000000'"))
    removed = db.Column(db.Integer, nullable=False, server_default=text('0'))

    def __repr__(self):
        return f"<Member(id={self.id}, userid={self.userid}, name={self.name}, email={self.email})>"
    