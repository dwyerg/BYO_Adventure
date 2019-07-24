import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb
from models import Story
from models import StoryPoint
from models import ChoicePoint

from google.appengine.api import urlfetch
import json
# This initializes the jinja2 envrionment
# THIS IS THE SAME FOR EVERY APP YOU BUILD
# jinja2.Environment is a constructor

jinjaEnv = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True
)

# the handler section

class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    age = ndb.IntegerProperty()


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        loginDict = {

        }
        user = users.get_current_user()
        if user:
            email_address = user.nickname
            logout_url = users.create_logout_url('/')

        else:
            login_url = users.create_login_url('/')



class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        main_template = jinjaEnv.get_template("main.html")
        self.response.write(main_template.render())
        myStory = Story(title="The Lion, The Witch, And The Wardrobe")
        myStory.put()
        self.response.write(myStory.key)

# the app configuration section

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        title= self.request.get("adventure_name")
        create_template = jinjaEnv.get_template("create.html")
        self.response.write(create_template.render())


class NewStepHandler(webapp2.RequestHandler):
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

app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
        ('/login', LoginHandler),
        ('/create', CreateHandler),
        ('/newStep', NewStepHandler),
        ('/addFork', AddForkHandler)
    ],
    debug=True
    )
