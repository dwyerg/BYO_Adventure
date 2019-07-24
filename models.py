from google.appengine.ext import ndb

class BYOusers(ndb.Model):
    first_name = ndb.StringProperty()
    last_name= ndb.StringProperty()
    email = ndb.StringProperty()



class Story(ndb.Model):
    title=ndb.StringProperty(required=True)
#    picture=ndb.StringProperty(required=True)

class StoryPoint(ndb.Model):
    story_id = ndb.IntegerProperty(required=True)
    plot_id = ndb.StringProperty(required=True)
    plot_text=ndb.TextProperty(required=True)

class ChoicePoint(ndb.Model):
    choice_text = ndb.StringProperty(required=True)
    begin_plot_id = ndb.StringProperty(required=True)
    next_plot_id = ndb.StringProperty(required=True)
