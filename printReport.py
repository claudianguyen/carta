#!/usr/bin/env python 

from src.integrations.sweet_bank import work
from src.integrations.acme_financials import process

from src.integrations.Transaction import Transaction
import sys
import os

ACME_BANK_DIRECTORY = "assets/acme_bank"
GRINGOTTS_BANK_DIRECTORY = "assets/gringotts_bank"
SWEET_BANK_DIRECTORY = "assets/sweet_bank"

def parse(bank_name):
    if bank_name == "acme_bank":
        b = 1

    elif bank_name == "sweet_bank":
        a = 1

    elif bank_name == "gringotts_bank":
        for filename in os.listdir(GRINGOTTS_BANK_DIRECTORY):
            f = os.path.join(GRINGOTTS_BANK_DIRECTORY, filename)
            if os.path.isfile(f):
                print(filename)



    else:
        a = 1


def generate_report(bank_name):

    # parse file
    parse(bank_name)










if __name__ == '__main__':
    nameOfBank = sys.argv[1]
    generate_report(nameOfBank)


    # if nameOfBank == "sweet_bank":
    #     for f in ["../../assets/sweet_bank_financials_1.csv", "../../assets/sweet_bank_financials_2.csv", "../../assets/sweet_bank_financials_3.csv"]:
    #         file_name = f.split('/')[-1]
    #         print(file_name)
    #         work(file_name)
    #         print()
    #         print()
    #
    # if nameOfBank == "acme_bank":
    #     for f in ["../../assets/acme_bank_financials_1.json"]:
    #         file_name = f.split('/')[-1]
    #         result = process(file_name)
    #         print(file_name)
    #         print(result)