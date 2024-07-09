answer = '''❍●●●
●◯●●
●●◯●
●●●◯
'''
print(answer)

w = '○'
b = '●'
ansewer1 = w + b*3 + '\n' + b*2 + w + b +'\n' + b*3 + w
print(ansewer1)


answer2 = ''
for i in range(4):
    for j in range(4):
        if i == j:
            answer2 += w
        else:
            answer2 += b
    answer2 += '\n'
print(answer2)
