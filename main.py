bigtext = "ComputerScience"
keyword = "mabc"
cipher = ""
for i in range(len(bigtext)):
    cipher += keyword[i % len(keyword)]

print(cipher)