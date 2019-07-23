import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

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
    email = ndb.StringProperty()
    age = ndb.IntegerProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            logout_button = '<a href="%s"> Log out</a>' % logout_url

            existing_user = CssiUser.query().filter(CssiUser.email == email_address).get()
            if existing_user:
                self.response.write('WELCOME BACK TO THE HOMEPAGE ' + existing_user.first_name + "<br>" +logout_button)
            else:
                self.response.write('''Please register!
                    <form method='post' action='/'>
                        Name: <input type='text' name='first_name'>
                        Age: <input type='text' name='age'>
                        <input type='submit'>
                    </form>
                    <br>
                    %s
                ''' % logout_button)
        else:
            login_url = users.create_login_url('/')
            login_button = '<a href="%s"> Sign In</a>' % login_url
            # login_button = '<a href="' + login_url + '"> Sign In</a>'
            self.response.write("Please log in!<br>" + login_button)
    def post(self):
        user = users.get_current_user()
        if user:
            cssi_user = CssiUser(
                first_name=self.request.get('first_name'),
                age = int(self.request.get('age')),
                email = user.nickname()
            )
            cssi_user.put()
            self.response.write('Thank you for registering <a href="/">Home</a>')


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
        ("/login", LoginPage),
        ('/', MainHandler)
    ],
    debug=True
    )
