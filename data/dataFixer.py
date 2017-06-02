
# geen diploma laatste bachelor
# anders diploma
# informatica, informatiekunde en KI bachelors tellen niet mee

# Gemaakt door je boy Tim op 15 mei 2017 & 18 mei 2017

import csv
import json
from datetime import datetime

bachelorFile = "bachelor.csv"
masterFile = "master.csv"
resultFile = "results.json"

bachelorStudents = []
masterNummers = []
tab = "\t"
fouteStudies = ["B Kunstmatige Intelligentie", "B Informatica", "B Informatiekunde"]
fouteStudiesCounter = 0

class bachelorStudent:
	#ID, Oms. Studieprog., Faculteit, Ingangsd.dipl.
	def __init__(self, id, studieProg, faculteit, diplomaDatum, geslacht):
		self.id = id
		self.bachelor = studieProg
		self.faculteit = faculteit
		if diplomaDatum:
			self.diplomaDatum = diplomaDatum
		else:
			self.diplomaDatum = -1
		self.geslacht = geslacht
		self.master = None

	def addMaster(self, master):
		self.master = master

	def hasDiploma(self):
		if self.diplomaDatum == -1:
			return False
		else:
			return True

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

	def __str__(self):
		return str(str(self.id) + tab + str(self.bachelor) + tab + str(self.faculteit) + tab + str(self.diplomaDatum) + tab + str(self.master))

with open(bachelorFile, 'r') as infileBachelor:
	readerBachelor = csv.DictReader(infileBachelor)
	for line in readerBachelor:
		if not line["Oms. Studieprog."] in fouteStudies:
			studentje = bachelorStudent(line["ID"], line["Oms. Studieprog."], line["Faculteit"], line["Ingangsd.dipl."], line["Geslacht"])
			#print studentje
			bachelorStudents.append(studentje)
		else:
			fouteStudiesCounter += 1
		# studentID = line[0]
		# if studentID not in bachelorNummers:

		# 	bachelorNummers.append(studentID)



	# readerMaster = csv.reader(infileMaster)
	# masterFields = readerMaster.next()

bachelorStudents2 = []

# matchCounter = 0
# for student in bachelorStudents:
# 	for student2 in bachelorStudents2:
# 		if student.id == student2.id:
# 			print "Match foudn motherfucker"
# 			matchCounter+= 1
# print matchCounter

alleStudenten = {}

for student in bachelorStudents:
	# print student.id, student.diplomaDatum
	if student.id not in alleStudenten:
		alleStudenten[student.id] = student
	else:
		if student.diplomaDatum != -1:
			org = alleStudenten[student.id]
			# print "shit is -1 g"
			# print student
			# print org
			if org.diplomaDatum == -1:
				alleStudenten[student.id] = student
			else:
				studentDate = datetime.strptime(student.diplomaDatum, "%d-%m-%Y")
				studentDate2 = datetime.strptime(org.diplomaDatum, "%d-%m-%Y")
				if studentDate > studentDate2:
					alleStudenten[student.id] = student
				# print "hoi"
				# print student.diplomaDatum
				# print org.diplomaDatum
				# studentDate = datetime.strptime(student.diplomaDatum, "%d-%m-%Y")
				# studentDate2 = datetime.strptime(org.diplomaDatum, "%d-%m-%Y")
				# if studentDate < studentDate2:
					

		
# print alleStudenten

print "testerino"
print alleStudenten["10002850"].diplomaDatum

congruentieCounter = 0


with open(masterFile, "r",) as infileMaster:
	# print infileMaster
	readerMaster = csv.DictReader(infileMaster)
	for masterStudent in readerMaster:
		masterID = masterStudent["ID"]
		if masterID in alleStudenten:
			congruentieCounter += 1
			alleStudenten[masterID].master = masterStudent["Oms. Studieprog."]
			# print alleStudenten[masterID]
		# else:
		# 	print masterID
		
# print alleStudenten["10003145"].master

# bachelorDicts = {
# 	"FNWI": [],
# 	"FMG": [],
# 	"FEB: "
# }

bachelorFaculteiten = []
bachelorStudies = []

uberDict = {}

for studenteren in alleStudenten:
	if alleStudenten[studenteren].faculteit not in bachelorFaculteiten:
		bachelorFaculteiten.append(alleStudenten[studenteren].faculteit)
	if alleStudenten[studenteren].bachelor not in bachelorStudies:
		bachelorStudies.append(alleStudenten[studenteren].bachelor)

print bachelorFaculteiten
print bachelorStudies

for s in alleStudenten:
	for k in bachelorFaculteiten:
		if alleStudenten[s].faculteit == k:
			if k not in uberDict:
				uberDict[k] = []
				uberDict[k].append(alleStudenten[s])
			else:
				uberDict[k].append(alleStudenten[s])

print uberDict


with open(resultFile, 'w') as outfile:
	print alleStudenten["10003145"]

matrixArray = []
for bachelor in bachelorStudies:
	matrixArray.append([])
print matrixArray

# for bachelor in bachelorStudies:
# 	for student 

for student in alleStudenten:
	print alleStudenten[student]
# for student in bachelorStudents:
# 	bachelorStudents2.append(student)
# 	for student2 in bachelorStudents2:
# 		if student.id == student2.id:
# 			print student.diplomaDatum
# 			print student2.diplomaDatum
			# studentDate = datetime.strptime(student.diplomaDatum, "%d-%m-%Y")
			# studentDate2 = datetime.strptime(student2.diplomaDatum, "%d-%m-%Y")
# 			print studentDate
# 			if studentDate < studentDate2:
# 				bachelorStudents2.remove(student)
# 				bachelorStudents2.append(student2)
# 		# else:
# 		# 	bachelorStudents2.append(student)

# print (bachelorStudents2)






# for s in bachelorStudents:
# 	print s
# print fouteStudiesCounter


