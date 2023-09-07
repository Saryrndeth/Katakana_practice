from pprint import pprint
import random

Katakanas = [i for i in "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"]
Katakanas_roma = ['a', 'i', 'u', 'e', 'o']

for i in "kstnhmyrw" :
    for j in "aiueo" :
        word = i + j
        if word == 'yi' or word == 'ye' or word == 'wi' or word == 'we' or word == 'wu':
            continue
        if word == 'ti':
            word = 'chi'
        elif word == 'tu':
            word = 'tsu'

        Katakanas_roma.append(f"{word}")

Katakanas_roma.append('n')

user = None
corrected = []
while user != 'end':
    if len(corrected) == 46:
        break
    number = random.randint(0, len(Katakanas) - 1)
    while number in corrected:
        number = random.randint(0, len(Katakanas) - 1)
    print(f"다음 가타카나의 발음은? {Katakanas[number]}")
    user = input()
    if user == Katakanas_roma[number]:
        print("정답!")
        corrected.append(number)
    else:
        print(f"오답, {Katakanas[number]}의 발음은 {Katakanas_roma[number]}")

print("모든 발음 훈련을 완료하였습니다.")