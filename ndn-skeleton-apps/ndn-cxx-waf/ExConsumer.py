import time, threading
import os

InterestArray = [ [0 for i in range(10)] for j in range(5)]
while True:
    if os.path.exists('InterestArray.txt'):
        fileobj = open("InterestArray.txt", "r", encoding = "utf_8")
        while True:
            line = fileobj.readline()
            if line:
                fc = line.split(',')
                FuncName = fc[0]
                #print(FuncName)
                con = fc[1].split('/')
                ConName = con[len(con)-2]
                #print(ConName)
                
                sum = 0
                for num in range(10):
                    if InterestArray[0][num] == ConName and InterestArray[1][num] == FuncName :
                        sum = 1
                        break
                
                if not sum == 1:
                    for num in range(10):
                        if InterestArray[0][num] == 0:
                            InterestArray[0][num] = ConName
                            InterestArray[1][num] = FuncName
                            InterestArray[2][num] = time.time()
                            print("New Interest")
                            rm = "sudo rm InterestArray.txt"
                            os.system(rm)
                            break
                        
                        #print(InterestArray[0][num])
                        #print(InterestArray[1][num])
            else:
                break
                            
                        
    for num in range(10):
        if not InterestArray[2][num] == 0:
            test_time = time.time() - InterestArray[2][num]
            if test_time >= 5:
                #print(test_time)
                InterestArray[2][num] =time.time()
                output = "sudo ./consumer " + InterestArray[1][num] + " " + InterestArray[0][num]
                os.system(output)
        