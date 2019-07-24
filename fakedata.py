from google.appengine.ext import ndb

class Story(ndb.Model):
  title = ndb.StringProperty(required=True)
  first_story_point_key = ndb.KeyProperty(required=False)

class StoryPoint(ndb.Model):
  story_key = ndb.KeyProperty(required=True)
  text = ndb.StringProperty(required=True)

class ChoicePoint(ndb.Model):
  begin_story_point_key = ndb.KeyProperty(required=True)
  end_story_point_key = ndb.KeyProperty(required=True)
  text = ndb.StringProperty(required=True)

cars1_story = Story(title = "Cars 1")

cars1_story.put()

cars1_storypoint1 = StoryPoint(story_key = cars1_story.key, text = "Life is a highway")
cars1_storypoint2 = StoryPoint(story_key = cars1_story.key, text = "meets mater")
cars1_storypoint3 = StoryPoint(story_key = cars1_story.key, text = "dies")

cars1_storypoint1.put()
cars1_storypoint2.put()
cars1_storypoint3.put()

cars1_story.first_story_point_key = cars1_storypoint1.key

cars1_story.put()

cars1_choicepoint1 = ChoicePoint(begin_story_point_key = cars1_storypoint1.key, end_story_point_key = cars1_storypoint2.key, text = "go to radiator springs?")
cars1_choicepoint1 = ChoicePoint(begin_story_point_key = cars1_storypoint1.key, end_story_point_key = cars1_storypoint3.key, text = "race again?")

cars1_story.put()

cars1_storypoint1.put()
cars1_storypoint2.put()
cars1_storypoint3.put()
cars1_choicepoint1.put()
cars1_choicepoint2.put()
