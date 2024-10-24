# -*- coding: utf-8 -*-

"""
    <To Do>
    
    The program will log output to a log file called '1source-python.log'
"""

__author__ = "Dharm Kapadia"
__copyright__ = "© 2023 EquiLend"
__version__ = "0.5.0"
__email__ = "dharm.kapadia@equilend.com"


import argparse
import logging
from rich.pretty import pprint
from requests import Response

from net.query_by_id import get_by_id
from utils.logger import configure_logging
from utils.app_config import app_conf
from net.auth import get_auth_token
from net.entities import get_entity

# Create file specific logger
logger: logging.Logger = configure_logging(
    logging, app_conf.log_file, app_conf.log_format, "main"
)


def print_output(data_type: str, data: str) -> None:
    """
    Print output of received data to the console
    """
    pprint(f"1Source {data_type} for {app_conf.username}:")
    pprint(data)


def main():
    """
        Start of the application
    :return:
    """

    # Set up command line parser options
    parser = argparse.ArgumentParser(description="1Source Python command line example")
    parser.add_argument(
        "-g",
        metavar="<Entity>",
        help="1Source API Endpoint to query [auth, agreements, loans, events, parties, rerates, returns, recalls, delegations, buyins]",
        required=False,
        choices=[
            "auth",
            "agreements",
            "loans",
            "events",
            "parties",
            "rerates",
            "returns",
            "recalls",
            "delegations",
            "buyins",
        ],
    )

    parser.add_argument(
        "-a",
        metavar="<Trade Agreement Id>",
        required=False,
        help="1Source API Endpoint to query Trade Agreements by agreement_id",
    )

    parser.add_argument(
        "-e",
        metavar="<Event Id>",
        required=False,
        help="1Source API Endpoint to query Events by event_id",
    )

    parser.add_argument(
        "-l",
        metavar="<loan_id>",
        required=False,
        help="1Source API Endpoint to query Loans by loan_id",
    )

    parser.add_argument(
        "-lh",
        metavar="<loan_id>",
        required=False,
        help="1Source API Endpoint to query Loan History by loan_id",
    )

    parser.add_argument(
        "-p",
        metavar="<Party Id>",
        required=False,
        help="1Source API Endpoint to query Parties by party_id",
    )

    parser.add_argument(
        "-d",
        metavar="<Delegation Id>",
        required=False,
        help="1Source API Endpoint to query Privileged Venue delegations",
    )

    parser.add_argument(
        "-re",
        metavar="<Return Id>",
        required=False,
        help="1Source API Endpoint to query Returns by return_id",
    )

    parser.add_argument(
        "-rc",
        metavar="<Recall Id>",
        required=False,
        help="1Source API Endpoint to query Recalls by recall_id",
    )

    parser.add_argument(
        "-rr",
        metavar="<Rerate Id>",
        required=False,
        help="1Source API Endpoint to query Rerates by rerate_id",
    )

    # Parse command line arguments
    args = parser.parse_args()
    vargs: dict = vars(args)

    # Get an auth Response from 1Source
    resp: Response = get_auth_token()
    js = resp.json()

    # Extract the auth token from auth Response
    token: str = js["access_token"]

    if "g" in vargs and vargs["g"] is not None:
        entity = vargs["g"]

        match entity:
            case "auth":
                if token:
                    print_output("Auth Response", js)

            case "agreements":
                if token:
                    # Got an auth token, call the agreements endpoint to get the data
                    data = get_entity(app_conf.agreements, token)
                    print_output("Trade Agreements", data)

            case "loans":
                if token:
                    # Got an auth token, call the loans endpoint to get the data
                    data = get_entity(app_conf.loans, token)
                    print_output("Loans", data)

            case "events":
                # Got an auth token, call the events endpoint to get the data
                data = get_entity(app_conf.events, token)
                print_output("Events", data)

            case "parties":
                if token:
                    # Got an auth token, call the parties endpoint go get the data
                    data = get_entity(app_conf.parties, token)
                    print_output("Parties", data)

            case "returns":
                if token:
                    # Got an auth token, call the returns endpoint go get the data
                    data = get_entity(app_conf.returns, token)
                    print_output("Returns", data)

            case "recalls":
                if token:
                    # Got an auth token, call the recalls endpoint go get the data
                    data = get_entity(app_conf.recalls, token)
                    print_output("Recalls", data)

            case "rerates":
                if token:
                    # Got an auth token, call the rerates endpoint go get the data
                    data = get_entity(app_conf.rerates, token)
                    print_output("Rerates", data)

            case "delegations":
                if token:
                    # Got an auth token, call the delegations endpoint go get the data
                    data = get_entity(app_conf.delegations, token)
                    print_output("Delegations", data)

            case "buyins":
                if token:
                    # Got an auth token, call the buyins endpoint go get the data
                    data = get_entity(app_conf.buyins, token)
                    print_output("Buyins", data)

            case _:
                logger.error(f"Unsupported 1Source endpoint '{entity}'")
                pprint(f"Unsupported 1Source endpoint '{entity}'")
                exit(1)

    if "a" in vargs and vargs["a"] is not None:
        entity_id: str = vargs["a"]
        data = get_by_id(app_conf.agreements, entity_id, token)
        if data:
            print_output("Trade Agreement", data)
        exit(0)

    if "e" in vargs and vargs["e"] is not None:
        entity_id: str = vargs["e"]
        data = get_by_id(app_conf.events, entity_id, token)
        if data:
            print_output("Event", data)
        exit(0)

    if "l" in vargs and vargs["l"] is not None:
        entity_id: str = vargs["l"]
        data = get_by_id(app_conf.loans, entity_id, token)
        if data:
            print_output("Loan", data)
        exit(0)

    if "lh" in vargs and vargs["lh"] is not None:
        entity_id: str = vargs["lh"]
        data = get_by_id(app_conf.loans, entity_id, token, True)
        if data:
            print_output("Loan History", data)
        exit(0)

    if "p" in vargs and vargs["p"] is not None:
        entity_id: str = vargs["p"]
        data = get_by_id(app_conf.parties, entity_id, token)
        if data:
            print_output("Party", data)
        exit(0)

    if "d" in vargs and vargs["d"] is not None:
        entity_id: str = vargs["d"]
        data = get_by_id(app_conf.delegations, entity_id, token)
        if data:
            print_output("Delegation", data)
        exit(0)

    if "re" in vargs and vargs["re"] is not None:
        entity_id: str = vargs["re"]
        data = get_by_id(app_conf.returns, entity_id, token)
        if data:
            print_output("Returns", data)
        exit(0)

    if "rc" in vargs and vargs["rc"] is not None:
        entity_id: str = vargs["rc"]
        data = get_by_id(app_conf.recalls, entity_id, token)
        if data:
            print_output("Recalls", data)
        exit(0)

    if "rr" in vargs and vargs["rr"] is not None:
        entity_id: str = vargs["rr"]
        data = get_by_id(app_conf.rerates, entity_id, token)
        if data:
            print_output("Rerate", data)
        exit(0)


if __name__ == "__main__":
    main()
