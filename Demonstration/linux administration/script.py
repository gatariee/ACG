from passlib.hash import sha256_crypt
import argparse

parser = argparse.ArgumentParser(description="script")
parser.add_argument("-v", "--verbose", action="store_true")
s = input("Enter shadow line: ")
s_split = s.split(":")[1].split("$")[1:]
wordlist = "wordlist.txt"
def shadowCrack(hash):
    """
    Args:
        hash (str): A line from /etc/shadow that contains a hashed password

    Presenter Notes:
        This function takes a line from /etc/shadow as an argument and tries to crack it.
        It uses a wordlist to crack the hash. 
        Each word from the wordlist is first appended with the salt.
        Then, the word is hashed using the same hashing algorithm as the one used to hash the password.
        For the sake of example, the hash being cracked is assumed to be of SHA-256crypt with 5000 rounds.
        Linux uses SHA-256crypt with 5000 rounds to hash passwords. 

    """
    with open(wordlist, "rb") as file:
        print(f"Salt: {s_split[1]}")
        for line in file:
            for word in line.split():
                a = sha256_crypt.hash(word, rounds=5000, salt=s_split[1])  # Hashing every word in wordlist
                if vars(parser.parse_args())["verbose"]:
                    print(f"Trying password: {word.decode()}")
                    print(f"Comparing input 1: {hash}")
                    print(f'Comparing input 2: {a.split("$")[3]}')
                if hash == a.split("$")[3]:  # Comparing input hash with wordlist
                    print(f"Password found! The password is: {word.decode()}")
                    return
        print("Not found. ")


shadowCrack(s_split[2])
