import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.api import urlfetch
import json


def checkUser():
    
