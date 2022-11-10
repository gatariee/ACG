import hashlib
import binascii
def hashCracker(hash):
    with open(wordlist, 'r') as file:
        for line in file:
            for word in line.split():
                wordlist_hash = binascii.hexlify(hashlib.new('md4', word.encode('utf-16le')).digest())
                print(f"Input: {hash}\nWordlist: {wordlist_hash.decode()}\n") 
                if(hash == wordlist_hash.decode()):
                    print(f'Hash found! The unhashed string is: {word}')
                    return
        print("Not found. ")

wordlist = "wordlist.txt"

hash = input("Enter hash: ")
hashCracker(hash)