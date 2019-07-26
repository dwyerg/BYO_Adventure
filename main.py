import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb
from models import BYOusers
from google.appengine.api import urlfetch
import json

#importing classes from our models sheet
from models import Story
from models import StoryPoint
from models import ChoicePoint
import time
# This initializes the jinja2 envrionment
# THIS IS THE SAME FOR EVERY APP YOU BUILD
# jinja2.Environment is a constructor

jinjaEnv = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True
)

# the handler section
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        print('user:' + str(user))
        if user:
            existing_user =BYOusers.query().filter(BYOusers.email == user.nickname()).get()
            print('existing_user: ' + str(existing_user))
            if existing_user:
                self.redirect("/")
            else:
                # this is the case where they are not registered
                self.redirect("/registration")

        login_dict={
            "login_url": users.create_login_url('/')
        }
        print('logindict:' +str(login_dict))

        main_template = jinjaEnv.get_template("login.html")
        self.response.write(main_template.render(login_dict))




class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            existing_user =BYOusers.query().filter(BYOusers.email == user.nickname()).get()
            if existing_user:
                pass
            else:
                # this is the case where they are not registered
                self.redirect("/registration")
        else:
            self.redirect("/login")
        main_template = jinjaEnv.get_template("main.html")
        self.response.write(main_template.render())


class OneFormHandler(webapp2.RequestHandler):
# creating the story as one form with a bunch of textboxes for the whole story
    def get(self):
        oneform_template = jinjaEnv.get_template("oneForm.html")
        self.response.write(oneform_template.render())

class registrationPage(webapp2.RequestHandler):
    def post(self):
        user=users.get_current_user()
        firstname = self.request.get("first-name")
        lastname = self.request.get("last-name")
        emailaddress= user.nickname()
        new_user=BYOusers(first_name=firstname,last_name=lastname,email=emailaddress)
        new_user.put()
        time.sleep(1) # I'm sorry. Waiting for datastore to store
        self.redirect("/")

    def get(self):
        user= users.get_current_user()
        if user:
            existing_user =BYOusers.query().filter(BYOusers.email == user.nickname()).get()
            if existing_user:
                self.redirect("/")


        else:
            self.redirect("/registration")
        main_template = jinjaEnv.get_template("registration.html")
        self.response.write(main_template.render())

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        email_address= user.nickname()
        existing_user= BYOusers.query().filter(BYOusers.email== email_address).get()


        logout_dict={
            "firstname": existing_user.first_name,
            "lastname": existing_user.last_name,
            "email": existing_user.email,
            "logout_url": users.create_logout_url('/login')
        }

        profile_template = jinjaEnv.get_template("profile.html")
        self.response.write(profile_template.render(logout_dict))


class ResultHandler(webapp2.RequestHandler):
#creates the result of whatever the user enters
    def post(self):

        rStory= Story(title= self.request.get("adventure_name"))

        #shooting the story up to the database
        rStory.put()

        #creating the storypoints based on each text they enter for what happens
        storypoint1 = StoryPoint(story_key = rStory.key, text = self.request.get("first_story_point"))
        storypoint2 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceA_story_point"))
        storypoint3 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceB_story_point"))
        storypoint4 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceC_story_point"))
        storypoint5 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceD_story_point"))
        storypoint6 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceE_story_point"))
        storypoint7 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceF_story_point"))
        storypoint8 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceG_story_point"))
        storypoint9 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceH_story_point"))
        storypoint10 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceI_story_point"))
        storypoint11 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceJ_story_point"))
        storypoint12 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceK_story_point"))
        storypoint13 = StoryPoint(story_key = rStory.key, text = self.request.get("choiceL_story_point"))

        #putting all of the storypoints into the database
        storypoint1.put()
        storypoint2.put()
        storypoint3.put()
        storypoint4.put()
        storypoint5.put()
        storypoint6.put()
        storypoint7.put()
        storypoint8.put()
        storypoint9.put()
        storypoint10.put()
        storypoint11.put()
        storypoint12.put()
        storypoint13.put()

        #assigning a first id
        rStory.first_story_point_key = storypoint1.key

        #putting / updating the story now that it has a first_id
        rStory.put()

        #creating all of the choice points
        choicepoint1 = ChoicePoint(begin_story_point_key = storypoint1.key, end_story_point_key = storypoint2.key, text = self.request.get("Choice_A"))
        choicepoint2 = ChoicePoint(begin_story_point_key = storypoint1.key, end_story_point_key = storypoint3.key, text = self.request.get("Choice_B"))
        choicepoint3 = ChoicePoint(begin_story_point_key = storypoint2.key, end_story_point_key = storypoint4.key, text = self.request.get("Choice_C"))
        choicepoint4 = ChoicePoint(begin_story_point_key = storypoint2.key, end_story_point_key = storypoint5.key, text = self.request.get("Choice_D"))
        choicepoint5 = ChoicePoint(begin_story_point_key = storypoint3.key, end_story_point_key = storypoint6.key, text = self.request.get("Choice_E"))
        choicepoint6 = ChoicePoint(begin_story_point_key = storypoint3.key, end_story_point_key = storypoint7.key, text = self.request.get("Choice_F"))
        choicepoint7 = ChoicePoint(begin_story_point_key = storypoint4.key, end_story_point_key = storypoint8.key, text = self.request.get("Choice_G"))
        choicepoint8 = ChoicePoint(begin_story_point_key = storypoint4.key, end_story_point_key = storypoint9.key, text = self.request.get("Choice_H"))
        choicepoint9 = ChoicePoint(begin_story_point_key = storypoint6.key, end_story_point_key = storypoint10.key, text = self.request.get("Choice_I"))
        choicepoint10 = ChoicePoint(begin_story_point_key = storypoint6.key, end_story_point_key = storypoint11.key, text = self.request.get("Choice_J"))
        choicepoint11 = ChoicePoint(begin_story_point_key = storypoint7.key, end_story_point_key = storypoint12.key, text = self.request.get("Choice_K"))
        choicepoint12 = ChoicePoint(begin_story_point_key = storypoint7.key, end_story_point_key = storypoint13.key, text = self.request.get("Choice_L"))

        #putting the story again
        rStory.put()

        #putting the storypoints now that they have corresponding choicepoints
        storypoint1.put()
        storypoint2.put()
        storypoint3.put()
        storypoint4.put()
        storypoint5.put()
        storypoint6.put()
        storypoint7.put()
        storypoint8.put()
        storypoint9.put()
        storypoint10.put()
        storypoint11.put()
        storypoint12.put()
        storypoint13.put()


        #putting the choicepoints
        choicepoint1.put()
        choicepoint2.put()
        choicepoint3.put()
        choicepoint4.put()
        choicepoint5.put()
        choicepoint6.put()
        choicepoint7.put()
        choicepoint8.put()
        choicepoint9.put()
        choicepoint10.put()
        choicepoint11.put()
        choicepoint12.put()

        display_dictionary = {

            "display_title": rStory.title,
            "display_sp_1" : storypoint1.text,
            "display_sp_2" : storypoint2.text,
            "display_sp_3" : storypoint3.text,
            "display_sp_4" : storypoint4.text,
            "display_sp_5" : storypoint5.text,
            "display_sp_6" : storypoint6.text,
            "display_sp_7" : storypoint7.text,
            "display_sp_8" : storypoint8.text,
            "display_sp_9" : storypoint9.text,
            "display_sp_10" : storypoint10.text,
            "display_sp_11" : storypoint11.text,
            "display_sp_12" : storypoint12.text,
            "display_sp_13" : storypoint13.text,

            "display_cp_1" : choicepoint1.text,
            "display_cp_2" : choicepoint2.text,
            "display_cp_3" : choicepoint3.text,
            "display_cp_4" : choicepoint4.text,
            "display_cp_5" : choicepoint5.text,
            "display_cp_6" : choicepoint6.text,
            "display_cp_7" : choicepoint7.text,
            "display_cp_8" : choicepoint8.text,
            "display_cp_9" : choicepoint9.text,
            "display_cp_10": choicepoint10.text,
            "display_cp_11": choicepoint11.text,
            "display_cp_12": choicepoint12.text,

        }

        result_template = jinjaEnv.get_template("result.html")
        #self.response.write(result_template.render())
        self.response.write(result_template.render(display_dictionary))
        print("displaying story!" + display_dictionary["display_sp_1"])
        #creating the story for what the user will input
        #with only a title for now bc we will make the first id later

    def get(self):
        
        pass


class BrowseHandler(webapp2.RequestHandler):
    def get(self):
        allStories = Story.query().fetch()
        allStoryPoints = StoryPoint.query().fetch()
        allChoicePoints = ChoicePoint.query().fetch()
        all_dict = {
            "theStories" : allStories,
        }
        all_stories_template = jinjaEnv.get_template("browse.html")
        self.response.write(all_stories_template.render(all_dict))

class ReadHandler(webapp2.RequestHandler):
    def get(self):
        read_template = jinjaEnv.get_template("read.html")
        self.response.write(read_template.render())
class StoryPointAPI(webapp2.RequestHandler):
    def get(self):
        id = self.request.get("id")
        simple_dict = {
            "story_text": ,
            "pear": "orange"
        }
        self.response.write(json.dumps(simple_dict))

app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
        ('/login', LoginHandler),
        ("/registration",registrationPage),
        ('/profile',ProfileHandler),
        ('/oneform', OneFormHandler),
        ('/result', ResultHandler),
        ('/browse', BrowseHandler),
        ('/read', ReadHandler),
        ('/api/story', StoryPointAPI)
    ],
    debug=True
    )
