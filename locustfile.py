from locust import HttpUser, between, task
import random
import json

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    host = "https://nd082-marten.azurewebsites.net:443"

    @task
    def index(self):
        self.client.get("/")

    @task
    def prediction(self):

        """
        Documentation from: https://www.kaggle.com/c/boston-housing

        CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
        RM: average number of rooms per dwelling.
        TAX: full-value property-tax rate per \$10,000.
        PTRATIO: pupil-teacher ratio by town.
        B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.
        LSTAT: lower status of the population (percent).
        """
        payload={
            "CHAS": {"0": random.randint(0,1)},
            "RM":{"0": random.uniform(1.0, 10.0)},
            "TAX":{"0": random.uniform(50.0, 1000.0)},
            "PTRATIO":{"0": random.uniform(3.0, 50.0)},
            "B":{"0": random.uniform(5.0, 1000.0)},
            "LSTAT":{"0": random.uniform(1.0, 9.5)}
        }

        response = self.client.post("/predict", json=payload)
