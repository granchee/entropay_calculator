#!/usr/bin/python

# @todo Fee as arg?
# @todo Updating .ini?

import sys
import ConfigParser

def PrintUsage():
    print "----------------------------------------------------------------------"
    print "Usage: entropay_calculator.py amount-to-be-received"

def GetAmountFromArg(arg):
    try:
        amount = float(arg)
    except ValueError:
        print "Need numerical argument for amount to be received!"
        return 0.0
    else:
        return amount

if __name__ == '__main__':
    if 2 != len(sys.argv):
        PrintUsage()
        sys.exit()
    else:
        amount_to_be_received = GetAmountFromArg(sys.argv[1])
        if 0.0 == amount_to_be_received:
            PrintUsage()
            sys.exit()
        else:
            Config = ConfigParser.ConfigParser()
            try:
                Config.read("entropay_calculator.ini")
                percentage_fee = Config.getfloat("Config", "percentage_fee")
                amount_to_be_sent = amount_to_be_received * 100.0 / (100.0 - percentage_fee)
            except ConfigParser.Error:
                print "Config problem?!"
            except ZeroDivisionError:
                print "Fee problem leading to divide-by-zero?!"
            else:
                print "Amount to be sent=%.2f (more exactly=%.3f)" % (amount_to_be_sent, amount_to_be_sent)
                print "Using configured fee=%.2f%%" % (percentage_fee)
