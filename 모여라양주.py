# 현재 날짜 구하기
from datetime import datetime
now = datetime.now()


print("---------------------------------------")
print("안녕하세요. 이은지입니다. 첫글이에요.")
print("pull -> commit -> push")
print("작성시간:", now.strftime('%Y-%m-%D %H:%M:%S'))
print("---------------------------------------")
