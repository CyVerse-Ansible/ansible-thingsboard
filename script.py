import logging
import sys
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://localhost:9090"

# Default Tenant Administrator credentials
username = "sysadmin@thingsboard.org"
password = "sysadmin"


def main():
    # Creating the REST client object with context manager to get auto token refresh
    with RestClientCE(base_url=url) as rest_client:
        try:
            # Auth with credentials
            rest_client.login(username=username, password=password)
            # using sys argument 1 to get the new password
            new_password = sys.argv[1]
            change = ChangePasswordRequest(password, new_password)
            # Call change_password_using_post method
            rest_client.change_password(body=change)


        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    main()
