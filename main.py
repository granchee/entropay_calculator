#!/usr/bin/python

# @todo Fee as arg?
# @todo Proper validation of args?
# @todo Updating .ini?

import sys
import ConfigParser

def ValidateArg():
    # Continue iff one proper arg supplied (assumed to be amount to be received).
    if len(sys.argv) == 2:
        is_valid = True
    else:
        print "Need numerical argument for amount to be received!"
        is_valid = False
    return is_valid

def PrintUsage():
    print "----------------------------------------------------------------------"
    print "Usage: entropay_calculator.py amount-to-be-received"

if __name__ == '__main__':
    if False == ValidateArg():
        PrintUsage()
        sys.exit()
    else:
        amount_to_be_received = float(sys.argv[1])
        Config = ConfigParser.ConfigParser()
        Config.read("entropay_calculator.ini")
        percentage_fee = Config.getfloat("Config", "percentage_fee")
        amount_to_be_sent = amount_to_be_received * 100.0 / (100.0 - percentage_fee)
        print "Amount to be sent=%.2f (more exactly=%.3f)" % (amount_to_be_sent, amount_to_be_sent)
        print "Using configured fee=%.2f%%" % (percentage_fee)
