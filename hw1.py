str=input()
score_An=0
score_Minh=0
for i in range(len(str)):
    if str[i]!='A' and str[i]!='O' and str[i]!='I' and str[i]!='U' and str[i]!='E':
        score_An+=len(str)-i
    else:
        score_Minh+=len(str)-i
if score_An>score_Minh:
    print(f"An {score_An}")
elif score_An<score_Minh:
    print(f"Minh {score_Minh}")
else:
    print("Draw")
    