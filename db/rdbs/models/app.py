from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String

Base = declarative_base()

class App(Base):
    __tablename__ = 'app'
    
    appid = Column(String, primary_key=True)
    category = Column(String)
    company = Column(String)
    content_rating = Column(String)
    description = Column(String)
    dev_mail = Column(String)
    dev_privacy_url = Column(String)
    dev_url = Column(String)
    install = Column(String)
    name = Column(String)
    rating = Column(Float)
    screen_count = Column(Integer)
    size = Column(String)
    total_reviewers = Column(Integer)
    version = Column(String)
    
    def __init__(self, appid, category, company, content_rating, description, dev_mail, dev_privacy_url, dev_url, 
    install, name, rating, screen_count, size, total_reviewers, version):
        self.appid = appid
        self.category = category
        self.company = company
        self.content_rating = content_rating
        self.description = description
        self.dev_mail = dev_mail
        self.dev_privacy_url = dev_privacy_url
        self.dev_url = dev_url
        self.install = install
        self.name = name
        self.rating = rating
        self.screen_count = screen_count
        self.size = size
        self.total_reviewers = total_reviewers
        self.version = version

    def __repr__(self):
        return "<App(appid='%s', name='%s', description='%s')>" % (
        self.appid, self.name, self.description)