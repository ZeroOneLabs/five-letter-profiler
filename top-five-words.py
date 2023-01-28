'''
When "Wordle" came out in 2020, I got an idea in my head to figure out which
5-letter words in the English language were the most "popular", with the
simple criteria of the words consisting of letters with the highest count
in each index position. So, if a word began with more As than Bs, then it 
would rank higher.

Throw some RegEx magic on top of that, and BAM, you got yourself a quick
and dirty 5-letter word list.

This project is in no way directly associated with the intellectual property
of "wordle". However, I was inspired by the game to write this.
'''
import re
from string import ascii_lowercase
letters = ascii_lowercase
zeros = "0" * len(letters)

master_dict = {}
for pos in range(0,5):
    master_dict[pos] = {}
    for item, key in zip(letters, zeros):
        master_dict[pos][item] = int(key)

with open('five-word-list.txt', 'r') as f:
    wordfile = f.read()
    master_word_list = wordfile.splitlines()

for word in master_word_list:
    letter_list = list(word.strip())
    
    for i, letter in enumerate(letter_list):
        master_dict[i][letter] += 1


top_letters_dict = {
    "0": [], "1": [], "2": [], "3": [], "4": []
}
top_numbers_dict = {
    "0": [], "1": [], "2": [], "3": [], "4": []
}
def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

print("Top 5 Letters for each character position (pos):")
print("Pos")
for i, letters in enumerate(master_dict):
    sorted_dict = sorted(master_dict[i].items(), key=lambda item: item[1], reverse=True)
    pop_letter1 = sorted_dict[0][0]
    pop_letter2 = sorted_dict[1][0]
    pop_letter3 = sorted_dict[2][0]
    pop_letter4 = sorted_dict[3][0]
    pop_letter5 = sorted_dict[4][0]
    pop_number1 = sorted_dict[0][1]
    pop_number2 = sorted_dict[1][1]
    pop_number3 = sorted_dict[2][1]
    pop_number4 = sorted_dict[3][1]
    pop_number5 = sorted_dict[4][1]

    top_letters_dict[str(i)] = [pop_letter1, pop_letter2, pop_letter3, pop_letter4, pop_letter5]
    top_numbers_dict[str(i)] = [f"{pop_number1:,}", f"{pop_number2:,}", f"{pop_number3:,}", f"{pop_number4:,}", f"{pop_number5:,}" ]

    print("#" + str(i + 1) + "\t" + "\t".join(top_letters_dict[str(i)]))
    print("  " + "\t" + "\t".join(top_numbers_dict[str(i)]))
    print()

w1g = "".join(top_letters_dict["0"])
w2g = "".join(top_letters_dict["1"])
w3g = "".join(top_letters_dict["2"])
w4g = "".join(top_letters_dict["3"])
w5g = "".join(top_letters_dict["4"])
regex_search = fr"^[{w1g}][{w2g}][{w3g}][{w4g}][{w5g}]"
pop_word_list = []
pop_words_list = []

matches = re.finditer(regex_search, wordfile, re.MULTILINE)

for match in matches:
    word = match[0]
    
    if not word.endswith("s"):
        pop_word_list.append(word)

print()
print("Top words:")
prev_first_letter = ""
word_list = []
for word in pop_word_list:
    first_letter = word[0]
    l1, l2, l3, l4, l5 = list(word)
    if l1 == l2 or l1 == l3 or l1 == l4 or l1 == l5:
        continue
    if l2 == l3 or l2 == l4 or l2 == l5:
        continue
    if l3 == l4 or l3 == l5:
        continue
    if l4 == l5:
        continue
    
    if first_letter == prev_first_letter:
        if word.startswith(first_letter):
            word_list.append(word)
    else:
        if prev_first_letter != "":
            print(", ".join(word_list))
        word_list = []
        first_letter = word[0]
        word_list.append(word)
    prev_first_letter = first_letter
print(", ".join(word_list))