fileName = input('Input file Name :') # eg: myFile.txt
f = open('D:\\pycharm\\input\\'+fileName,'w')
datatofile = input('Write data to file :')
f.write(datatofile)
f.close()