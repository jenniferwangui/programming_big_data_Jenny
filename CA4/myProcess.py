import csv
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.
#my_file = open(changes_file, 'r')
#data = my_file.readlines()
data = [line.strip() for line in open(changes_file, 'r')]
# print the number of lines read
# print the number of lines read
print(len(data))
sep = 72*'-'

class Changes:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, time = None, day = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.day = day
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
    def get_commit_changes(self):
        return self.day+"  .  "+ self.time+"  .  "+ self.date+ "  .  "+"  .  "  + self.author+ "  .  " + "  .  ".join(self.revision) 
        
changes = []
current_changes = None
index = 0


author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_changes = Changes()
        details = data[index + 1].split('|')
        #print (details)
  #current_commit.revision = details[0].strip()
        current_changes.revision = int(details[0].strip().strip('r'))
        current_changes.author = details[1].strip()
        current_changes.date = details[2].strip().split(' ')[0]
        current_changes.day = details[2].strip().split(' ')[3][1:4]
        current_changes.time = details[2].strip().split(' ') [1]
        current_changes.comment_line_count = int(details[3].strip().split(' ')[0])
        current_changes.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_changes.changes = data[index-current_changes.comment_line_count:index]
        changes.append(current_changes)
    except IndexError:
        break
        
print (details)
print(len(changes))
changes.reverse()
#for index, changes in enumerate(changes):
    #print(changes.get_commit_changes())
    
textFileCsv = []
for index, commit in enumerate(changes):
    testFile = []
    testFile.append(commit.get_commit_changes())
    #listaInterna.append(len(commits))
    textFileCsv.append(testFile)

with open("testFile2.csv", 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([len(changes)])
    for line in textFileCsv:
        spamwriter.writerow(line)    
