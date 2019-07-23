from google.appengine.ext import ndb

class Story(ndb.Model):
    =ndb.StringProperty(required=True)
    bottomLine=ndb.StringProperty(required=True)
    picture=ndb.StringProperty(required=True)
