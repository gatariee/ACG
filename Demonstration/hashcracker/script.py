import hashlib
def hashCracker(hash):
    """
    Args:
        hash (str): The hash to crack
        
    Presenter Notes:
        This function is a hash cracker. It takes a hash as an argument and tries to crack it.
        It uses a wordlist to crack the hash. The wordlist is a file that contains a list of words.
        Note that for the sake of example, the hash being cracked can only be of SHA2-256.
    """
    with open(wordlist, 'rb') as file:
        for line in file:
            for word in line.split():
                print(f"Input: {hash}\nWordlist: {hashlib.sha256(word).hexdigest()}\n") 
                if(hash == hashlib.sha256(word).hexdigest()):
                    print(f'Hash found! The unhashed string is: {word.decode()}')
                    return
        print("Not found. ")

wordlist = "wordlist.txt"

hash = input("Enter hash: ")
hashCracker(hash)