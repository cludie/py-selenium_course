#Reading accounts.txt
with open("accounts.txt", "r") as reader:
    content = [line.strip() for line in reader]

temporary = []
login = []
password = []

for i in range(len(content)):
    temporary.append(content[i].split(':'))
for i in range(len(temporary)):
    login.append(temporary[i][0])
    password.append(temporary[i][1])

acc_counter = len(login)