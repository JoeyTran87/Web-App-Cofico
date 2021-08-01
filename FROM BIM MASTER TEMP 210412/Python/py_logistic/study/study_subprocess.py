import subprocess




# filePath = r"C:\Users\tvpduy\py_logistic\ipconfig.txt"
# with open(filePath,'w') as f:
#     ipconfig = test = subprocess.run('ipconfig /all',stdout=f, text=True) #stdout = subprocess.PIPE


test = subprocess.run('ipconfig /all',shell=True, capture_output=True,text =True, check = True) # text = True thì không dùng stdout.decode()
print(test.returncode)
print(test.stdout)
# print(test.stdout.decode())
print(test.stderr) # ERRORS


test2 = subprocess.run('ipconfig /all',shell=True, capture_output=True,text =True, input = test.stdout) # input là lấy đầu ra của Tiến trình khác đem vào tiến trình này