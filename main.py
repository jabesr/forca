import requests
from random import randrange
res = requests.get("https://raw.githubusercontent.com/fserb/pt-br/refs/heads/master/verbos")

words = res.text.split("\n")
index = randrange(0, len(words))

word = words[index].lower()

revealed = ["_" for i in range(len(word))]
print("".join(revealed))

kill_status = 0
#  o
# /|\
#  |
# / \

def print_kill_status(status):
    match status:
        case 0:
            return
        case 1:
            print("  o")

        case 2:
            print("  o")
            print("  |")
            print("  |")

        case 3:
            print("  o")
            print(" /|")
            print("  |")

        case 4:
            print("  o")
            print(" /|\\")
            print("  |")

        case 5:
            print("  o")
            print(" /|\\")
            print("  |")
            print(" /")

        case 6:
            print("  o")
            print(" /|\\")
            print("  |")
            print(" / \\")
            print("Você perdeu!")
            print(f"A palavra era: {word}")
            print("MUAHAHAHAHAHAHAHA!")
            exit()

while True:
    letter = input("Digite uma letra: ")[0]
    letter = letter.lower()

    if not letter.isalpha() or len(letter) > 1:
        print("Digite APENAS uma letra, ANIMAAAAAAAAL!!!")
        continue


    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                revealed[i] = letter

    else:
        kill_status += 1

    print("".join(revealed))

    if "_" not in revealed:
        print("Você ganhou!")
        exit()
    else:
        print_kill_status(kill_status)


# IyBwZWRyYSA9IGlucHV0KCJOb21lIGRhIFBSRURBIChwb2RlIHNlciBjcmFjaykiKQojIG1hdGNoIHBlZHJhOgojICAgICBjYXNlICJjcmFjayI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgY3JhY2siKQojICAgICBjYXNlICJtYWNvbmhhIjoKIyAgICAgICAgIHByaW50KCJQZWRyYSDDqSBtYWNvbmhhIikKIyAgICAgY2FzZSAiY29jYWluYSI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgY29jYWluYSIpCiMgICAgIGNhc2UgImxzZCI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgbHNkIikKIyAgICAgY2FzZSAibWRtYSI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgbWRtYSIpCiMgICAgIGNhc2UgImVjc3Rhc3kiOgojICAgICAgICAgcHJpbnQoIlBlZHJhIMOpIGVjc3Rhc3kiKQojICAgICBjYXNlICJkbXQiOgojICAgICAgICAgcHJpbnQoIlBlZHJhIMOpIGRtdCIpCiMgICAgIGNhc2UgImF5YWh1YXNjYSI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgYXlhaHVhc2NhIikKIyAgICAgY2FzZSAibWVzY2FsaW5hIjoKIyAgICAgICAgIHByaW50KCJQZWRyYSDDqSBtZXNjYWxpbmEiKQojICAgICBjYXNlICJwc2lsb2NpYmluYSI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgcHNpbG9jaWJpbmEiKQojICAgICBjYXNlICJwZXlvdGUiOgojICAgICAgICAgcHJpbnQoIlBlZHJhIMOpIHBleW90ZSIpCiMgICAgIGNhc2UgInNhbHZpYSI6CiMgICAgICAgICBwcmludCgiUGVkcmEgw6kgc2FsdmlhIik=