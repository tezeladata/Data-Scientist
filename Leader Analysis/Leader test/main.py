import json

arr = []
with open("test.json") as file:
    data = json.load(file)
    for i in data: arr.append(i)

no_post = [i for i in arr if i["post"] == False]
post = [i for i in arr if i["post"] == True]

good_comment = [i for i in arr if i["good_message_like"] == True]
bad_comment = [i for i in arr if i["bad_message_like"] == True]


'''
Correlation 1: no_post and bad_comment
'''
cor1 = [i for i in no_post if i in bad_comment]
print("\nBad comment like + no post on fb:")
for i in cor1: print(i)
print("The end\n")


'''
Correlation 2: good_comment and post
'''
cor2 = [i for i in good_comment if i in post]
print("\nGood comment like + post on fb:")
for i in cor2: print(i)
print("The end\n")


'''
Correlation 3: bad_comment and good_comment
'''
cor3 = [i for i in bad_comment if i in good_comment]
print("\nGood comment like + bad comment like:")
for i in cor3: print(i)
print("The end\n")