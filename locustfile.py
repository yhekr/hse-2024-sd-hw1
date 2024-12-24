from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def assign_order(self):
        self.client.post("/assign-order/", json={
            "order_id": "order123",
            "executer_id": "executer456",
            "locale": "en-US"
        })

    @task
    def acquire_order(self):
        self.client.post("/acquire-order/", json={
            "executer_id": "executer456"
        })

    @task
    def cancel_order(self):
        self.client.post("/cancel-order/", json={
            "order_id": "order123"
        })
