import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb
from models import BYOusers
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


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            existing_user =BYOusers.query().filter(BYOusers.email == user.nickname()).get()
            if existing_user:
                self.redirect("/")
            else:
                # this is the case where they are not registered
                self.redirect("/registration")




        login_dict={
            "login_url": users.create_login_url('/')
        }

        main_template = jinjaEnv.get_template("login.html")
        self.response.write(main_template.render(login_dict))




class MainPage(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
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



class registrationPage(webapp2.RequestHandler):
    def post(self):
        user=users.get_current_user()
        firstname = self.request.get("first-name")
        lastname = self.request.get("last-name")
        emailaddress= user.nickname()
        new_user=BYOusers(first_name=firstname,last_name=lastname,email=emailaddress)
        new_user.put()
        self.redirect("/")
    def get(self):
        user= users.get_current_user()
        if user:
            existing_user =BYOusers.query().filter(BYOusers.email == user.nickname()).get()
            if existing_user:
                self.redirect("/")

        else:
            self.redirect("/login")
        main_template = jinjaEnv.get_template("registration.html")
        self.response.write(main_template.render())


# the app configuration section

app = webapp2.WSGIApplication(
    [
        ("/", MainPage),
        ('/login', LoginHandler),
        ("/registration",registrationPage)

    ],
    debug=True
    )
