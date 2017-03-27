import os, sys
import csv
import datetime
import jsonpickle
import pprint

class IncomeInfo:

    def __init__(self, uni, lastn, firstn, midn, title, sex, empd, salary):
        self.university = uni
        self.lastname = lastn
        self.firstname = firstn
        self.middleinitial = midn
        self.title = title
        self.sex = sex
        self.employdate = empd
        self.salary = salary

class IncomeParser:

    TARGET_UNI = "Texas A&M University"
    TARGET_DEP = "ECONOMICS"
    TARGET_TIT = ["ASSOCIATE PROFESSOR", "PROFESSOR", "ASSISTANT PROFESSOR"]

    result = []

    def __init__(self):
        self.incomeinfo = []

    def run(self):
        with open(os.path.abspath(os.path.join("in","am2016.csv")), "rU") as csvfile:
            incomereader = csv.reader(csvfile, delimiter=',')
            for row in incomereader:
                if row[0] == self.TARGET_UNI \
                    and row[5] == self.TARGET_DEP \
                    and row[4] in (self.TARGET_TIT):
                    info = IncomeInfo(row[0], row[1], row[2], row[3], row[4], row[7], row[8], row[11])
                    self.result.append(info)


# run
program = IncomeParser()
program.run()

# log
print "Collected {1} data from {0}".format(program.TARGET_UNI, len(program.result))

# dump
outputpath = os.path.abspath(os.path.join("out","income_{0}.dat".format(program.TARGET_UNI.replace(" ", "_")).lower()))

with open(outputpath, "w+") as file:
    file.write(jsonpickle.encode(program.result))