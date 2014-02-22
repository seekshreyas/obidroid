from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Review(Base):
    __tablename__ = 'review'
    
    reviewid = Column(Integer, primary_key=True)
    playappid = Column(String, nullable=False)
    title = Column(String)
    review = Column(String, nullable=False)

    def __init__(self, playappid, title, review):
        self.playappid = playappid
        self.title = title
        self.review = review

    def __repr__(self):
        return "<Review(reviewid='%d', playappid='%s', title='%s')>" % (
        self.reviewid, self.playappid, self.title)