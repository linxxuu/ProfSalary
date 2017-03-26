import csv
import datetime
import cPickle as pickle

class IncomeInfo:

    UniversityName = ""
    LastName = ""
    FirstName = ""
    MiddleInitial = ""
    Title = ""
    Sex = ""
    EmploymentDate = datetime.date.min
    Salary = .0

    def __init__(self, uni, lastn, firstn, midn, title, sex, empd, salary):
        self.UniversityName = uni
        self.LastName = lastn
        self.FirstName = firstn
        self.MiddleInitial = midn
        self.Title = title
        self.Sex = sex
        self.EmploymentDate = empd
        self.Salary = salary

class IncomeParser:

    TARGET_UNI = "Texas A&M University"
    TARGET_DEP = "ECONOMICS"
    TARGET_TIT = ["ASSOCIATE PROFESSOR", "PROFESSOR", "ASSISTANT PROFESSOR"]

    result = []

    def __init__(self):
        self.incomeinfo = []

    def run(self):
        with open("../../in/am2016.csv", "rU") as csvfile:
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
with open("../../out/income_{0}.dat".format(program.TARGET_UNI.replace(" ", "_")).lower(), "w+") as file:
    pickle.dump(program.result, file)