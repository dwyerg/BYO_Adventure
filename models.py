from google.appengine.ext import ndb

class Story(ndb.Model):
    i=ndb.StringProperty(required=True)
    bottomLine=ndb.StringProperty(required=True)
    picture=ndb.StringProperty(required=True)
