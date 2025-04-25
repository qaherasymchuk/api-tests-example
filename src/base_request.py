import json
import os
from collections import namedtuple
from loguru import logger

from requests import Response, get, post, patch, put, delete

from constants import REQUEST_TIMEOUT


class BaseRequest:

    def __init__(self):
        self._base_url = os.environ['API_HOST']
        self._headers = {'Content-Type': 'application/json'}

    @staticmethod
    def log_pretty_json(res):
        content_type_rs = res.headers.get('content-type')
        if len(res.content) > 0 and (content_type_rs in {"application/json", "application/problem+json"}):
            pretty_json = json.dumps(res.json(), sort_keys=True, indent=4)
            logger.info(f"\nResponse:\n{pretty_json}")

    @staticmethod
    def custom_decoder(response_dict) -> tuple:
        return namedtuple('X', response_dict.keys())(*response_dict.values())

    def send_get(self, endpoint, params=None, headers=None) -> Response:
        if params is None:
            params = {}
        logger.info(f"Send GET request to: '{self._base_url + endpoint}' with param: '{params}' and headers: {headers}")
        response = get(self._base_url + endpoint, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
        self.log_pretty_json(response)
        return response

    def send_post(self, endpoint, payload=None, headers=None, data=None, params=None, auth=()) -> Response:
        if len(payload) > 0:
            logger.info(f"Send POST request to : \n"
                        f"headers: {headers}\n"
                        f"data: {data}\n"
                        f"params: {params}\n"
                        f"{self._base_url + endpoint} with payload: \n{json.dumps(payload, sort_keys=True, indent=4)}")
        response = post(
            self._base_url + endpoint,
            json=payload,
            data=data,
            headers=headers,
            params=params,
            auth=auth,
            timeout=REQUEST_TIMEOUT
        )
        self.log_pretty_json(response)
        return response

    def send_patch(self, endpoint, payload=None, headers=None) -> Response:
        if len(payload) > 0:
            logger.info(f"Send PATCH request to : {self._base_url + endpoint} with payload: \n{payload}")
        response = patch(self._base_url + endpoint, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        self.log_pretty_json(response)
        return response

    def send_delete(self, endpoint, payload=None, headers=None, params=None) -> Response:
        if len(payload) > 0:
            logger.info(f"Send DELETE request to : {self._base_url + endpoint} with payload: \n{payload}")
        response = delete(
            self._base_url + endpoint,
            json=payload,
            headers=headers,
            params=params,
            timeout=REQUEST_TIMEOUT
        )
        self.log_pretty_json(response)
        return response

    def send_put(self, endpoint, payload=None, headers=None, params=None) -> Response:
        if len(payload) > 0:
            logger.info(f"Send PUT request to : {self._base_url + endpoint} with payload: \n{payload}")
        response = put(self._base_url + endpoint, json=payload, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        self.log_pretty_json(response)
        return response