# -*- coding: utf-8 -*-

"""
    Python file to handle 1Source entity endpoints
    
"""

import logging
import requests
from requests import Response
from rich.pretty import pprint

from utils.logger import configure_logging
from utils.app_config import app_conf

# Set the file-level logger
logger = configure_logging(logging, app_conf.log_file, app_conf.log_format, "entities")


def get_entity(endpoint: str, token: str) -> str:
    """
        Call the 1Source API endpoint to get an entity,
        such as Parties, Loans, Events, etc.
    """
    headers: dict = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }

    resp: Response = requests.get(url=endpoint, headers=headers)

    if resp.status_code == 200:
        return resp.json()
    else:
        logger.error(f"Error code: {resp.status_code} with Reason: {resp.reason} received calling url: {endpoint}")
        pprint(f"Error code: {resp.status_code} with Reason: {resp.reason} received calling url: {endpoint}")
        return ""
