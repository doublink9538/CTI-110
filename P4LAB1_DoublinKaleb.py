user_text = input()
count = 0
for i in user_text:
    if (i=="," or i=="." or i=="!" or i==" "):
        pass
    else:
        count=count+1
print(count)
