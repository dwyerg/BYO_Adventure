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



('/create', CreateHandler),
('/firstStep', FirstStepHandler),
('/newStep', NewStepHandler),
('/addFork', AddForkHandler),
