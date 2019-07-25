import webapp2
import jinja2
import os

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
    def post(self):
        result_template = jinjaEnv.get_template("result.html")
        self.response.write(result_template.render())

        rStory= Story(title= self.request.get("adventure_name"))
        rStory.put()

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

        rStory.first_story_point_key = storypoint1.key

        rStory.put()

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

        rStory.put()

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

class BrowseHandler(webapp2.RequestHandler):
    def get(self):
        allStories = Story.query().fetch()
        allStoryPoints = StoryPoint.query().fetch()
        allChoicePoints = ChoicePoint.query().fetch()
        all_dict = {
            "theStories" : allStories,
            #"theStoryPoints" : allStoryPoints,
            #"theChoicePoints" : allChoicePoints
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
        ('/result', ResultHandler),
        ('/browse', BrowseHandler)
    ],
    debug=True
    )
