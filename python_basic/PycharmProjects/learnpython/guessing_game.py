import re
prediction = input("Guess the word: ").lower()

secret = "secret"
start = secret[0]
end = secret[-1]
word_length = secret.__len__()


# y = 0
# prel = prediction.__len__()
# while y <= prel -1:
#     psingle = prediction[y]
#     pposition = prediction.index(psingle)
#     y += 1
#     print(psingle)
#
# x = 0
# while x <= word_length -1:
#     single = secret[x]
#     position = secret.index(single)
#     x += 1


# y = 0
# prel = prediction.__len__()
# while y <= prel -1:
#     desire = secret
#     user = prediction
#
#     psingle = prediction[y]
#     pposition = prediction.index(psingle)
#     words = re.search(psingle, desire)
#     y += 1
#     print(words)

# tt = "s"
# words = re.search(tt, "secret")
# print(words)

if prediction == secret:
    print("Yes !!! You got the right one.")
elif prediction.isnumeric():
    print("Secret word is not numeric")
elif prediction.__len__()>word_length:
    print("Word is not more than five characters")
elif prediction.startswith(start) and prediction.endswith(end):
    print("Very Close !! Word starts with '" + start + "' and ends with '" + end + "'")
elif prediction.startswith(start):
    print("Close ! It's start with '" + start + "'")
elif prediction.endswith(end):
    print("Close! Word ends with '" + end + "'")
# elif re.search('[secret],the_string'):
#     print("Close! The word contains '" + single + "'")
else:
    print("Please try another one")