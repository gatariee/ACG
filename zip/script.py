import zipfile
wordlist = "wordlist.txt"
zip_file = "locked.zip" 
obj = zipfile.ZipFile(zip_file)
def crack_password(wordlist, obj):
    with open(wordlist, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    print("Trying password: ", word.decode())
                    obj.extractall(pwd=word) # Tries to unzip the file with pwd = word, where word is every word in wordlist.             
                    print("Success, password is:", word.decode())
                    return True
                except:
                    continue
    return False
if crack_password(wordlist, obj) == False:
    print("Password not found. Perhaps try another wordlist?")