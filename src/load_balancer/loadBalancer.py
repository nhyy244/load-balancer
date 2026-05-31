class Server:
    def __init__(self, base_url: str, received_requests=0):
        self.base_url = base_url  # includes port - http://localhost:8000 for example
        self.received_requests = received_requests


class LoadBalancer:
    def __init__(self, server_list: list[Server]):
        self.server_list = server_list
        self.server_chosen_index = 0

    def roundRobin(self) -> str:
        chosen_server = self.server_list[self.server_chosen_index]
        chosen_server.received_requests = chosen_server.received_requests + 1

        self.server_chosen_index = (self.server_chosen_index + 1) % len(
            self.server_list
        )
        return chosen_server.base_url
