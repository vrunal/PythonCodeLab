appendMe = '\n Hello World, i am learning Python' + str(3)
appendFile = open('testFile.txt'  , 'a')  # 'w' / 'a' are the modes for Writing or appending to a file
appendFile.write(appendMe)
appendFile.close()