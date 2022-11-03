from passlib.hash import sha256_crypt
wordlist = "wordlist.txt"
def shadowCrack(hash):
    with open(wordlist, "rb") as file:
        print(f"Salt: {s_split[1]}")
        for line in file:
            for word in line.split():
                a = sha256_crypt.hash(word, rounds=5000, salt=s_split[1])
                if hash == a.split("$")[3]:
                    print(f"Password found! The password for {name} is: {word.decode()}")
                    return
        print("Not found. ")
    
def main():
    with open("shadow.txt", "r") as file:
        for line in file:
            global name
            global s_split
            name = line.split(":")[0]
            s_split = line.split(":")[1].split("$")[1:]
            shadowCrack(s_split[2])

if __name__ == "__main__":
    main()