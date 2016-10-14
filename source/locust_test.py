from locust import TaskSet, task, HttpLocust


class SessionTasks(TaskSet):

    @task(6)
    def home(self):
        self.client.get('/')

    @task(6)
    def ecnpj(self):
        self.client.get('/e-cnpj')

    @task(1)
    def ecpf(self):
        self.client.get('/e-cpf')

    @task(3)
    def nfe(self):
        self.client.get('/nf-e')


class WebsiteUser(HttpLocust):
    task_set = SessionTasks
    min_wai = 1000
    max_wait = 3000
