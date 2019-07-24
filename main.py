import webapp2
import jinja2
import os

from models import Story
from models import StoryPoint
from models import ChoicePoint

from google.appengine.api import users
from google.appengine.ext import ndb
from models import BYOusers
from google.appengine.api import urlfetch
import json
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


# the app configuration section

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        title= self.request.get("adventure_name")
        create_template = jinjaEnv.get_template("create.html")
        self.response.write(create_template.render())


class FirstStepHandler(webapp2.RequestHandler):
    def post(self):
        step_template = jinjaEnv.get_template("newStep.html")
        self.response.write(step_template.render())

        tStory= Story(title= self.request.get("adventure_name"))
        print("THE TITLE OF THE STORY IS" + tStory.title)
        tStory.put()


class AddForkHandler(webapp2.RequestHandler):
    def post(self):
        fork_template = jinjaEnv.get_template("fork.html")
        self.response.write(fork_template.render())
        tStoryPoint=StoryPoint(story_key= 8, story_point_id = "ehbeej" , plot_text = self.request.get("story_text_box"))
        #tStoryPoint=StoryPoint(story_key= "", story_point_id = "" , plot_text = self.request.get("story_text_box"))
        #story_key=The ID of the story it belongs to, story_point_id is the random thing appengine generates
        print("HERE IS HOW THE STORY BEGINS:" + "\n" + tStoryPoint.plot_text)
        tStoryPoint.put()


class NewStepHandler(webapp2.RequestHandler):
    def post(self):
        fork_template = jinjaEnv.get_template("firstStep.html")
        self.response.write(fork_template.render())

class ProfileHandler(webapp2.RequestHandler):
    def get(self):

        user=users.get_current_user()
        logout_dict={
            "logout_url": users.create_logout_url('/login')
        }

        profile_template = jinjaEnv.get_template("profile.html")
        self.response.write(profile_template.render(logout_dict))


class BrowseHandler(webapp2.RequestHandler):
    def get(self):
        allStories = Story.query().fetch()
        allStoryPoints = StoryPoint.query().fetch()
        allChoicePoints = ChoicePoint.query().fetch()
        all_dict = {
            "theStories" = allStories,
            "theStoryPoints" = allStoryPoints,
            "theChoicePoints" = allChoicePoints
        }
        all_stories_template = jinjaEnv.get_template("browse.html")
        self.response.write(all_stories_template.render(all_dict))


app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
        ('/login', LoginHandler),
        ("/registration",registrationPage),
        ('/create', CreateHandler),
        ('/firstStep', FirstStepHandler),
        ('/newStep', NewStepHandler),
        ('/addFork', AddForkHandler),
        ('/profile',ProfileHandler),
        ('/oneform', OneFormHandler),
        ('/browse'), BrowseHandler)
    ],
    debug=True
    )
