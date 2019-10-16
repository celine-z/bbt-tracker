from sqlalchemy import Column, ForeignKey, Integer, String

from app import db


class Store(db.Model):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    comments = Column(String(250))

    def __init__(self, name, comments=None):
        self.name = name
        self.comments = comments

    def __repr__(self):
        return "<name: {}, img_file: {}, comments{}>".format(self.name, self.img_file, self.comments)


class Drink(db.Model):
    __tablename__ = 'drink'

    id = Column(Integer, primary_key=True)
    store = Column(String(20), ForeignKey('store.name', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    name = Column(String(50), nullable=False)
    sugar_level = Column(Integer)
    ice_level = Column(Integer)
    rating = Column(Integer)
    comments = Column(String(250))

    def __init__(self, store, name, sugar_level, ice_level, rating, comments):
        self.store = store
        self.name = name
        self.sugar_level = sugar_level
        self.ice_level = ice_level
        self.rating = rating
        self.comments = comments

    def __repr__(self):
        return "<name: {}, store: {}, sugar_level: {}, ice_level: {}, ratings: {}, comments: {}>".format(
            self.name, self.store, self.sugar_level, self.ice_level, self.rating, self.comments)
