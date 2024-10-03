# 1Source-Python

Demonstration code which accesses the 1Source REST API in a command-line Python program

## Description

This project provides sample code and a template for accessing the 1Source REST API in [Python](https://www.python.org/). The code runs as a command-line program which utilizes switches to exercise the various 1Source REST API endpoints.

## License

This code is provided as-is, without warranty of any kind, express or implied. Please see the LICENSE.txt in the repository for more details.

## Getting Started

### Dependencies

- Download and install [Anaconda](https://www.anaconda.com/download) or [Miniconda] (https://docs.conda.io/projects/miniconda/en/latest/index.html) packages

### Installing

Clone the code repository locally from GitHub with the following command:

```
> git clone https://github.com/Equilend/1Source-Python
> cd 1Source-Python
```

Create and activate the Conda enviroment for 1Source-Python:

```
1Source-Python> conda create --name 1source-python python=3.11
1Source-Python> conda activate 1source-python

```

Install the required 3rd-party Python packages into the created conda environment by entering the following command:

```
(1Source-Python) 1Source-Python> pip install -r requirements.txt

```

### Executing program

The 1Source-Python application can be run directly from the command line in the terminal after it is successfully built. The following comman will run the application:

```
1Source-Python> python main.py -h

```

The output of that will show the command line options available:

````
(1Source-Python) C:\dev\1Source-Python>python main.py -h
usage: main.py [-h] [-g <Entity to query>] [-a <Trade Agreement Id>] [-e <Event Id>] [-c <Loan Id>]
               [-ch <Loan Id>] [-p <Party Id>]

1Source Python command line example

options:
  -h, --help            Show this help message and exit
  -g <Entity>           1Source API Endpoint to query [auth, agreements, loans, events, parties, returns, rerates, recalls, delegations, buyins]
  -a <Trade Agreement Id>
                        1Source API Endpoint to query Trade Agreements by agreement_id
  -e <Event Id>         1Source API Endpoint to query Events by event_id
  -c <Loan Id>          1Source API Endpoint to query Loans by loan_id
  -ch <Loan Id>         1Source API Endpoint to query Loan History by loan_id
  -p <Party Id>         1Source API Endpoint to query Parties by party_id
  -d <Delegation Id>    1Source API Endpoint to query Delegations by delegation_id```

````

The default TOML configuration file is called 'configuration.toml' and is included in the repository.

The 1Source REST API can return the following entities:

- auth
- events
- parties
- agreements
- loans
- rerates
- returns
- recalls
- buyins

#### Events

To retrieve all events which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g events
```

The output of the command to retrieve events will be a JSON response from the 1Source REST API similar to:

```
'1Source Events for TestLender1User:'
[
{
'eventId': '12201f69e056374d72ac60a0514375a2d0ba7d22b7f350a64cef8109c923e6caad65:12',
'eventType': 'LOAN_PROPOSED',
'eventDateTime': '2024-03-28T11:49:27.468193Z',
'resourceUri': '/v1/ledger/loans/492c7066-eabc-4030-bbc0-7bd7141e3545'
}
]
```

#### Auth

To view the Auth Response (in JSON) to the login procedure, including the auth token, refresh token, token timeouts, and other related parameters:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g auth
```

#### Parties

Similar to the Events call, to retrieve all parties which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g parties
```

The REST API can be queried for a particular party with a party_id

```
(1Source-Python) C:\dev\1Source-Python>python main.py -p <Party Id>
```

#### Trade Agreements

Similar to the Events call, to retrieve all trade agreements which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g agreements
```

The REST API can be queried for a particular agreement with an agreement_id

```
(1Source-Python) C:\dev\1Source-Python>python main.py -a <Trade Agreement Id>
```

#### Loans

Similar to the Events call, to retrieve all loans which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g loans
```

The REST API can be queried for a particular loan with a loan_id

```
(1Source-Python) C:\dev\1Source-Python>python main.py -c <Loan Id>
```

The REST API can be queried for the history of a particular loan with a loan_id

```
(1Source-Python) C:\dev\1Source-Python>python main.py -ch <Loan Id>
```

#### Rerates

Similar to the Events call, to retrieve all rerates which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g rerates
```

#### Returns

Similar to the Events call, to retrieve all returns which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g returns
```

#### Recalls

Similar to the Events call, to retrieve all recalls which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g recalls
```

#### Buyins

Similar to the Events call, to retrieve all buyins which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g buyins
```

#### Delegations

Similar to the Events call, to retrieve all delegations which the user is authorized to view, the following command will do so:

```
(1Source-Python) C:\dev\1Source-Python>python main.py -g delegations
```

### Notes

- The 1Source command line application logs output to a file called '1Source-Python.log'.
- The name of the output log file can be changed in the source, which will require the program to be recompiled as detailed above.

### Configuration TOML Specification

The 1source command-line application reads data from a configuration file in TOML format. The file contains information required for the application to connect to the 1Source REST API, the individual endpoints, and the authentication details. The TOML file reflects that by have 3 required sections

- general
- endpoints
- authentication

Of the 3 sections, only a few of the attributes in the authentication section should be changed by the user. The rest should be left as-is unless otherwise instructed.

#### General

This section contains details of the 1Source REST API "auth_url" and realm This endpoint is for user login authentication and retrieval of the auth token on successful login. That auth token is required on subsequent calls to the 1Source REST API.

These values should not be changed by the user unless otherwise instructed.

#### Endpoints

This section contains key/value pairs related to the 1Source REST API endpoints for events, parties, agreements, and loans. These values should not be changed by the user unless otherwise instructed.

#### Authentication

This section contains key/value pairs related to the 1Source REST API login authentication (username, password, etc.)

## Authors

Contributors names and contact info

[@Dharm Kapadia](dharm.kapadia@equilend.com)

## Version History

- 0.1

  - Initial Release

- 0.5
  - Update to 1Source REST API V1.1.0

```

```
