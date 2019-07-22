import webapp2
import jinja2
import os

from models import MemeInfo
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

class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = jinjaEnv.get_template("main.html")
        self.response.write(main_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = jinjaEnv.get_template("login.html")
        self.response.write(Login_template.render())

# the app configuration section

app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
        ("/login", LoginPage)
    ],
    debug=True
    )
