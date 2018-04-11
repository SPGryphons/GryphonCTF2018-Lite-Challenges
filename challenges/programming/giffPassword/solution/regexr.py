import re

def main():
    
    #open file
    with open("password.txt", "r") as openFile:

        #read openFile contents
        wordList = []
        for line in openFile:
            wordList.append(line)
        words = "".join(wordList)
        
        #match all passwords
        resultTuple = re.findall(r"^(?!.*[\ ])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[~!@#$%^&*_\-+=`|\(){}\[\]:;\"'<>,.?/]).{15,20}$", words, flags=re.M)
        #write passwords to file
        with open("results.txt", "w") as writeFile:
            for i in resultTuple:
                print(i)
                writeFile.write(i+"\n")

if __name__ == "__main__":
    main()
