from google.appengine.ext import ndb

class BYOusers(ndb.Model):
    first_name = ndb.StringProperty()
    last_name= ndb.StringProperty()
    email = ndb.StringProperty()

class Story(ndb.Model):
    title = ndb.StringProperty(required=True)
    first_story_point_key = ndb.KeyProperty(required = False)
    author = ndb.StringProperty(required=False)

class StoryPoint(ndb.Model):
    story_key = ndb.KeyProperty(required=True)
    text = ndb.StringProperty(required=True)

class ChoicePoint(ndb.Model):
    text = ndb.StringProperty(required=True)
    begin_story_point_key = ndb.KeyProperty(required=True)
    end_story_point_key = ndb.KeyProperty(required=True)
