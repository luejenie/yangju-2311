# 현재 날짜 구하기
from datetime import datetime
now = datetime.now()


print("---------------------------------------")
print("안녕하세요. 이은지입니다. 첫글이에요.")
print("pull -> commit -> push")
print("작성시간:", now.strftime('%Y-%m-%D %H:%M:%S'))
print("작성시간이 계속 바뀌네"))
print("---------------------------------------")




# 가영이를 위한 로또 번호 추출하기
import random

# 1부터 45까지의 숫자 중 6개를 무작위로 선택
lotto_numbers = random.sample(range(1, 46), 6)

print("오늘의 행운의 번호는.... ", lotto_numbers)

# 은지의 구성을 따라해 보았습니다
print("안녕하세요. 여러분!! 재미있는 git 수업 후 함께해서 좋아요♥")
print("작성시간:", now.strftime('%Y-%M-%D %H:%M:%S'))
print("-------------------------------------")






