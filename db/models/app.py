from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class App(Base):
    __tablename__ = 'app'
    
    appid = Column(String, primary_key=True)
    category = Column(String)
    company = Column(String)
    content_rating = Column(String)
    description = Column(String)
    install = Column(String)
    name = Column(String)
    screen_count = Column(Integer)
    size = Column(String)
    total_reviewers = Column(Integer)
    version = Column(String)
    
    def __init__(self, appid, category, company, content_rating, description, install, name, screen_count, size, total_reviewers, version):
        self.appid = appid
        self.category = category
        self.company = company
        self.content_rating = content_rating
        self.description = description
        self.install = install
        self.name = name
        self.screen_count = screen_count
        self.size = size
        self.total_reviewers = total_reviewers
        self.version = version

    def __repr__(self):
        return "<App(appid='%d', name='%s', description='%s')>" % (
        self.appid, self.name, self.description)