
f = open('wordlist.txt', 'r')
content = f.read()

for chara in content:
    words = []
    word = ""
    if chara.isalnum():
        word += chara
    else:
        words.append(word)
        word = ""
# print(content)

print(words)

f.close()