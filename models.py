from google.appengine.ext import ndb

class BYOusers(ndb.Model):
    first_name = ndb.StringProperty()
    last_name= ndb.StringProperty()
    email = ndb.StringProperty()

class Story(ndb.Model):
    title=ndb.StringProperty(required=True)
#    picture=ndb.StringProperty(required=True)
    start_id = ndb.TextProperty(required = True)

class StoryPoint(ndb.Model):
    story_key = ndb.IntegerProperty(required=True)
    story_point_id = ndb.StringProperty(required=True)
    plot_text=ndb.TextProperty(required=True)

class ChoicePoint(ndb.Model):
    choice_text = ndb.StringProperty(required=True)
    begin_story_point_id = ndb.StringProperty(required=True)
    next_story_point_id = ndb.StringProperty(required=True)
