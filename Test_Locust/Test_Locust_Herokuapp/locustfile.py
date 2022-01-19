from locust import HttpUser, task, between
from locust import User, TaskSet, constant
from requests.auth import HTTPBasicAuth


class QuickstartUser(HttpUser):
    wait_time = between(0.5, 3)
    host = "https://the-internet.herokuapp.com/"

    @task
    class Tasks(TaskSet):
        @task
        def main_page(self):
            self.client.get("/")

        @task
        def auth_page(self):
            self.client.get("basic_auth", auth=("admin", "admin"))

        @task
        def broken_images(self):
            self.client.get("/broken_images")

        @task
        def key_presses(self):
            self.client.get("https://the-internet.herokuapp.com/key_presses")

        @task
        def stop(self):
            self.interrupt()
