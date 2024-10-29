from maps.config.database import db

class KeyStore(db.Model):
    __tablename__ = 'key_store'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_key = db.Column(db.String(2000), nullable=False)
    priv_key = db.Column(db.String(2000), nullable=False)
    key_timestamp = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f"<KeyStore(id={self.id}, pub_key={self.pub_key[:10]}...)>"