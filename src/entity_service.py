from src.base_request import BaseRequest


class EntityService(BaseRequest):
    def __init__(self, resource_url: str):
        super().__init__()
        self.resource_url = resource_url

    def get_all(self):
        return self.send_get(self.resource_url)

    def get_contains(self, filter_param: str, fields: list[str] = None):
        url = f"{self.resource_url}/{filter_param}"
        if fields:
            fields = ",".join(fields)
            url += f"/{fields}"
        return self.send_get(url)

    def get_exact_match(self, filter_param: str, fields: list[str] = None):
        url = f"{self.resource_url}/{filter_param}:abs"
        if fields:
            fields = ",".join(fields)
            url += f"/{fields}"
        return self.send_get(url)
