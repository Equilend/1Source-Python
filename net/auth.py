# -*- coding: utf-8 -*-

"""
    Python file to get an auth token for 1Source
    
"""

import logging
import requests
from requests import Response
from rich.pretty import pprint

from utils.logger import configure_logging
from utils.app_config import app_conf

# Set the file-level logger
logger = configure_logging(logging, app_conf.log_file, app_conf.log_format, "auth")


def get_auth_token() -> Response:
    """
        Get an auth token from 1Source
    """
    # data to be sent to api
    payload: dict = {
        'client_id': app_conf.client_id,
        'client_secret': app_conf.client_secret,
        'grant_type': app_conf.grant_type,
        'username': app_conf.username,
        'password': app_conf.password
    }

    # sending post request and saving response as response object
    resp: Response = requests.post(url=app_conf.auth_url, data=payload)

    if resp.status_code == 200:
        # extracting response text
        return resp
    else:
        logger.error(f"Received HTTP Error code: {resp.status_code} with Reason {resp.reason}")
        pprint(f"Received HTTP Error code: {resp.status_code} with Reason {resp.reason}")
        return None
