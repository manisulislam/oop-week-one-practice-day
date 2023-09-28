s=input().split()
revers_words=[]
for word in s:
    single=word[: : -1]
    revers_words.append(single)
result= " ".join(revers_words)
print(result)