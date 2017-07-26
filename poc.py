import os
from ConfigParser import SafeConfigParser
import argparse
import logging
from collections import namedtuple
from twilio.rest import Client

logging.basicConfig(level=logging.DEBUG, format="%(lineno)d\t%(message)s")

def get_config(filepath="~/.twilio.cfg"):
    """Pull credentials. The file should look like this:
        [credentials]
        account=fake_account
        token=fake_token
        [sms]
        from_number=fake_from_number
        dest_number=fake_destination_number
    """
    expanded_path = os.path.expanduser(filepath)
    parser = SafeConfigParser()
    parser.read(expanded_path)

    TwilioConfig = namedtuple('TwilioConfig',
                              ['account',
                               'token',
                               'from_number',
                               'dest_number'],
                              verbose=False)

    return TwilioConfig(account=parser.get('credentials', 'account'),
                        token=parser.get('credentials', 'token'),
                        from_number=parser.get('sms', 'from_number'),
                        dest_number=parser.get('sms', 'dest_number'))

if __name__ == '__main__':
    DESCRIPTION = 'Takes a config file and runs proof-of-concept'
    cli_args = argparse.ArgumentParser(description=DESCRIPTION)

    cli_args.add_argument('--config',
                          action='store',
                          required=True,
                          help='config containing credentials')

    args = cli_args.parse_args()
    config = get_config(args.config)
    logging.debug("twilio config is {}".format(config))

    client = Client(config.account, config.token)

    message_body = "This is my first Twilio application"

    message = client.messages.create(to=config.dest_number,
                                     from_=config.from_number,
                                     body=message_body)
