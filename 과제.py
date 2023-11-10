import random

lotto_numbers = random.sample(range(1, 46), 6)
lotto_numbers.sort()

lotto_string = ", ".join(map(str, lotto_numbers))
print("생성된 로또 번호는 " + lotto_string + " 입니다.")
