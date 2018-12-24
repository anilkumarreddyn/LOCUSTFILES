from locust import Locust, TaskSet, task

class WebsiteTasks(TaskSet):
    # Do this before tasks start
    def on_start(self):
        # Set any required HTTP Headers
        self.client.headers['Accept-Language'] = "en-US,en;q=0.8"

        # POST some form data
        self.client.post("/home/login", {
            "UserName": "anilkumarreddy933@gmail.com",
            "Password": "anil@votary"
        })

    # Run this task with weighting 2 (twice as much as the one below)
    @task(2)
    def index(self):
        # GET the home page
        self.client.get("/")

    @task(1)
    def contact(self):
        # GET the Contact page
        self.client.get("/contact/")

class WebsiteUser(Locust):
    # What task class are we running?  (the one above!)
    task_set = WebsiteTasks

    # What's the minimum wait time between requests?
    min_wait = 1000

    # And the maximum?
    max_wait = 3000

    # What is our base host for testing (prepended to GETs/POSTs above)?
    host = "http://www.google.com"
