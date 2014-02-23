from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import json
from itertools import islice, count
from pprint import pprint
from models.review import Review
from models.app import App

#engine = create_engine('postgresql://postgres:i219kkls@munners.dlinkddns.com:28432/obidroid')
engine = create_engine('postgresql://uzwispzaxfcipd:aSkx0cJOSmD2N4tZ2rk4hmJ8EU@ec2-54-204-20-28.compute-1.amazonaws.com:5432/obidroid')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def parse_review_json(fname='../exports/rawdata_reviews.json'):
    json_data = open(fname).read()
    return json.loads(json_data)

def parse_all_json(fname='../exports/game_brain_all.json'):
    json_data = open(fname).read()
    return json.loads(json_data)

def calculateSingularRating(ratings):
    total = 0; count = 0
    for rating in ratings:
        total = total + (int(rating[0].strip()) * int(rating[1]))
        count = count + int(rating[1])
    return total/float(count)

def parse_reviews():
    # list container 
    review_list = list()

    # loop through the json file, first by app and then by reviews
    for idx, app in enumerate(islice(parse_review_json(), None)):
        for review in app['reviews']:
            r = Review(app['appId'], review[0], review[1])
            review_list.append(r)

    # only commit all the review for every 10 apps
    if idx % 25 == 0:
        session.add_all(review_list)
        session.commit()
        review_list = list()

    # commit the rest of the review from the rest of the apps
    session.add_all(review_list)
    session.commit()
    session.close()

def parse_apps():
    # app container 
    app_list = list()

    # loop through the json file, first by app and then by reviews
    for idx, app in enumerate(islice(parse_all_json(), 1)):
        a = App(app['id'], app['category'], app['company'], app['contentRating'], 
        app['description'], app['install'], app['name'], calculateSingularRating(app['rating']),
        app['screenCount'], app['size'], app['totalReviewers'], app['version'])
        app_list.append(a)

    # only commit all the review for every 10 apps
    if idx % 25 == 0:
        session.add_all(app_list)
        session.commit()
        app_list = list()

    # commit the rest of the review from the rest of the apps
    session.add_all(app_list)
    session.commit()
    session.close()

def parse_all():
    # app and review list container
    app_list = list()
    review_list = list()
    
    # loop through the json file, first by app and then by reviews
    for idx, app in enumerate(islice(parse_all_json(), None)):
        
        a = App(app['id'], app['category'], app['company'], app['contentRating'], 
        app['description'], app.get('devmail'), app.get('devprivacyurl'), app.get('devurl'),
        app['install'], app['name'], calculateSingularRating(app['rating']), 
        app['screenCount'], app['size'], app['totalReviewers'], app['version'])
        app_list.append(a)
        for review in app['reviews']:
            r = Review(app['id'], review[0], review[1])
            review_list.append(r)

    # only commit all the review for every 10 apps
    if idx % 25 == 0:
        session.add_all(app_list)
        session.commit()
        app_list = list()
        session.add_all(review_list)
        session.commit()
        review_list = list()

    # commit the rest of the review from the rest of the apps
    session.add_all(app_list)
    session.commit()
    session.add_all(review_list)
    session.commit()
    session.close()

def _processInput(path):
    """ Process the input directory
    Process only djvu files that have not been transformed from directory path parameter.
    """

    # check if passed path is to a directory or to a file
    if os.path.isfile(path):
        # extract absolute path from user submitted path value
        abs_path = os.path.dirname(os.path.abspath(path))
        filename = os.path.basename(path)
        processFile(abs_path, filename)
    elif os.path.isdir(path):
        # extract absolute path from user submitted path value
        abs_path = os.path.abspath(path)
        # loop through and open/transform djvu files
        for filename in os.listdir(abs_path):
            processFile(abs_path, filename)
    else:
        print "An invalid directory or file was passed as input"

def _getInput():
    """ Command Line Input Parsing
        Parse the user input
    """
    
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='filepath', default='.')
    (option, args) = parser.parse_args()

    if not option.filepath:
        return parser.error('Input file or directory path not given, use --input="path.to.db.input"')

    return {'src': option.filepath}

def main():
    userInput - _getInput()
    processInput

if __name__ == '__main__':
    main
