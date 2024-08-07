# -*- coding: utf-8 -*-

"""
    Python file to handle 1Source entity endpoints by id

"""

import logging
import requests
from requests import Response
from rich.pretty import pprint

from utils.logger import configure_logging
from utils.app_config import app_conf
from utils.net_error import NetError

# Set the file-level logger
logger = configure_logging(logging, app_conf.log_file, app_conf.log_format, "query_by_id")


def get_by_id(endpoint: str, entity_id: str, token: str, history: bool = False) -> str:
    """
        Get Entity item by id
    """
    headers: dict = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }

    # Get
    url: str = f"{endpoint}/{entity_id}"

    if history:
        url = f"{url}/history"

    resp: Response = requests.get(url=url, headers=headers)

    if resp.status_code == 200:
        return resp.json()
    else:
        net_err = NetError(resp.status_code, resp.reason, entity_id)
        logger.error(f"HTTP Get Error: {str(net_err)}")
        pprint(f"HTTP Get Error: {str(net_err)}")
        return ""
