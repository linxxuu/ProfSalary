import os, sys
import csv
import datetime
import jsonpickle
import pprint

from .data import IncomeInfo

class IncomeParser:

    TARGET_UNI = "Texas A&M University"
    TARGET_DEP = "ECONOMICS"
    TARGET_TIT = ["ASSOCIATE PROFESSOR", "PROFESSOR", "ASSISTANT PROFESSOR"]

    datapath = os.path.abspath(__file__ + "/../../../../data")

    result = []

    def __init__(self):
        self.incomeinfo = []

    def run(self):

        # parse data
        with open(os.path.join(self.datapath,"am2016.csv"), "rU") as csvfile:
            # read from csv
            incomereader = csv.reader(csvfile, delimiter=',')
            for row in incomereader:
                if row[0] == self.TARGET_UNI \
                    and row[5] == self.TARGET_DEP \
                    and row[4] in (self.TARGET_TIT):
                    info = IncomeInfo(row[0], row[1], row[2], row[3], row[4], row[7], row[8], row[11])
                    self.result.append(info)
            # log
            print "\t- collected {1} data from {0}".format(self.TARGET_UNI, len(self.result))

        # dump
        outputpath = os.path.join(self.datapath,"income_results.dat")
        with open(outputpath, "w+") as file:
            file.write(jsonpickle.encode(self.result))