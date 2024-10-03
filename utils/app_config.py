# -*- coding: utf-8 -*-

"""
    Python class to hold the values from the configuration TOML file
    
"""

__author__ = "Dharm Kapadia"
__copyright__ = "© 2023 EquiLend"
__version__ = "1.0.0"
__email__ = "dharm.kapadia@equilend.com"

from dataclasses import dataclass
import logging
import tomllib                      # New in Python 3.11

from utils.logger import configure_logging

general: str = "general"
endpoints: str = "endpoints"
authentication: str = "authentication"

toml_file: str = "./configuration.toml"


@dataclass
class AppConfig:
    log_file: str
    log_format: str
    auth_url: str
    realm_name: str

    base: str
    parties: str
    events: str
    agreements: str 
    loans: str
    rerates: str
    returns: str
    recalls: str
    delegations: str
    buyins: str

    auth_type: str
    grant_type: str
    client_id: str
    username: str
    password: str
    client_secret: str

    vals: dict
    
    def read_app_config(self):
        with open(toml_file, "rb") as f:
            config_vals = tomllib.load(f)
            
            self.log_file = config_vals[general]["log_file"]
            self.log_format = config_vals[general]["log_format"]
            self.auth_url = config_vals[general]["auth_url"]
            self.realm_name = config_vals[general]["realm_name"]

            self.base = config_vals[endpoints]["base"]
            self.parties = config_vals[endpoints]["parties"]
            self.events = config_vals[endpoints]["events"]
            self.agreements = config_vals[endpoints]["agreements"]
            self.loans = config_vals[endpoints]["loans"]
            self.rerates = config_vals[endpoints]["rerates"]
            self.returns = config_vals[endpoints]["returns"]
            self.recalls = config_vals[endpoints]["recalls"]
            self.delegations = config_vals[endpoints]["delegations"]
            self.buyins = config_vals[endpoints]["buyins"]

            self.auth_type = config_vals[authentication]["auth_type"]
            self.grant_type = config_vals[authentication]["grant_type"]
            self.client_id = config_vals[authentication]["client_id"]
            self.username = config_vals[authentication]["username"]
            self.password = config_vals[authentication]["password"]
            self.client_secret = config_vals[authentication]["client_secret"]


# Instantiate an AppConfig object
app_conf: AppConfig = AppConfig(
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    {})

# Read in values from the configuration TOML file
app_conf.read_app_config()

# Set the file-level logger
logger = configure_logging(logging, app_conf.log_file, app_conf.log_format, "app_config")
