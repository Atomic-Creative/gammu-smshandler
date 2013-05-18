#!/usr/bin/python
import os
import sys
import logging

from datetime import datetime

messages = []


log = open("/home/satchitananda/Development/python/sms_handler/log.txt", 'a')
log.write(str(datetime.now()) + "\n")

try:
    """log.write(str(sys.argv))
    log.write("\n")
    messages = os.environ['SMS_MESSAGES']
    log.write(str(messages))
    log.write("\n")

    log.write("OS ENVIRON variable:")
    log.write(str(os.environ))
    log.write("\n")

    with open("/home/satchitananda/Development/python/sms_handler/messages.txt", 'a') as messages_file:
        counter = 1
        for message in messages:
            text = os.environ['SMS_%d_TEXT' % counter]
            number = os.environ['SMS_%d_NUMBER' % counter]
            log.write('SMS NUMBER: %s, SMS TEXT: %s' % (number, text))
            log.write("\n")
            messages_file.write(message)
            counter+=1"""

    log.write("OS ENVIRON variable:")
    log.write(str(os.environ))
    log.write("\n")

    numparts = int(os.environ['DECODED_PARTS'])
    # Are there any decoded parts?
    if numparts == 0 and not os.environ.get("SMS_1_TEXT"):
        log.write('No decoded parts!\n')
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

    with open("/home/satchitananda/Development/python/sms_handler/messages.txt", 'a') as messages_file:
        messages_file.write("Number %s have sent text: %s" % (os.environ['SMS_1_NUMBER'], text))
        messages_file.write("\n")

except Exception as ex:
    log.write(str(ex))

log.close()
