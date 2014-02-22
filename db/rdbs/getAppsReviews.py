from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from itertools import islice, count
from models.review import Review
from models.app import App
import pdb

engine = create_engine('postgresql://postgres:i219kkls@munners.dlinkddns.com:28432/obidroid')
engine.echo = True
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



def get_all_apps():
    return session.query(App).all()

def get_app_by_appid(appid):
    return session.query(App).filter(App.appid==appid).first()
    
def get_apps_by_category(category):
    return session.query(App).filter(App.category==category).all()

def get_reviews_by_category(category):
    qry = session.query(App, Review).filter(App.category==category)
    reviews = qry.filter(App.appid==Review.playappid).all()
    return reviews
    
def get_reviews_by_appid(appid):
    return session.query(Review).filter(Review.playappid==appid).all()

if __name__ == '__main__':
    #main
    pass
    #app_instance = get_reviews_by_appid('test.luis.app')
    #revs = get_reviews_by_category('Test')
    #print revs