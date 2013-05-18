#!/usr/bin/python
import os
import sys
import logging

# Config

config = {
    'log_path': '/var/log/smshandler.log',
    'log_format': '%(asctime)s %(levelname)s %(message)s',
    'log_level': logging.WARNING,
    'sms_storage_file': '/path/to/directory/where/to/store/messages.txt'
}

# Setting up logger

logger = logging.getLogger('smshandler')
hdlr = logging.FileHandler(config.get('log_path'))
formatter = logging.Formatter(config.get('log_format'))
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(config.get('log_level'))

messages = []

try:
    numparts = int(os.environ['DECODED_PARTS'])

    # Are there any decoded parts?

    if numparts == 0 and not os.environ.get("SMS_1_TEXT"):
        logger.warn('No decoded parts!')
        sys.exit(1)

    # Get all text parts
    if numparts > 0:
        text = ''
        for i in range(0, numparts):
            varname = 'DECODED_%d_TEXT' % i

            if varname in os.environ:
                text = text + os.environ[varname]

    else:
        text = os.environ.get("SMS_1_TEXT")

    with open(config.get('sms_storage_file'), 'a') as messages_file:
        messages_file.write("Number %s have sent text: %s" % (os.environ['SMS_1_NUMBER'], text))
        messages_file.write("\n")

except Exception as ex:
    logger.error(ex)
