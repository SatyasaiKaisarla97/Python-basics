try:
    file1 =  open('sample.txt','r' )
    content = file1.read()
    print(content)
    file1.close()
except  FileNotFoundError :
    print("file not found")
    
