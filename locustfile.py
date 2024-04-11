import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    host = 'https://makca3app.azurewebsites.net'
    wait_time = between(1, 2)

    @task
    def get_html(self):
        self.client.get("/")

    @task
    def post_prediction(self):
        self.client.post("/predict")