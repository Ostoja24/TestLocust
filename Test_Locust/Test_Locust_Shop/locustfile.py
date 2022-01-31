from locust import HttpUser, task, between, constant
from locust import User, TaskSet, constant
from requests.auth import HTTPBasicAuth
import math
from locust import LoadTestShape

class QuickstartUser(HttpUser):
    wait_time = constant(0.5)
    host = "https://www.demoblaze.com/index.html"

    @task
    class Tasks(TaskSet):
        @task
        def main_page(self):
            self.client.get("/")

        @task
        def product_page(self):
            self.client.get("prod.html?idp_=1")

        @task
        def cart(self):
            self.client.get("cart.html")

        @task
        def main_page(self):
            self.client.get("/")

        @task
        def stop(self):
            self.interrupt()

class StagesShape(LoadTestShape):
    stages = [
        {"duration": 30, "users": 20, "spawn_rate": 5},
        {"duration": 100, "users": 60, "spawn_rate": 15}]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

            return None
