try:
    file1 = open('output.txt','w')
    writing_file = file1.write('Hello!, python \n')
    # print(writing_file)
    file1.close()

    file1 = open('output.txt','a')
    appending_file = file1.write('Learning filehandling in python')
    # print(appending_file)
    file1.close()

    file1 = open('output.txt','r')
    reading_file =  file1.read()
    print(reading_file)
    file1.close()
except  FileNotFoundError:
    print("File not found")