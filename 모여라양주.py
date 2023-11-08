# 현재 날짜 구하기
from datetime import datetime
now = datetime.now()



print("안녕하세요. 이은지입니다. 첫글이에요.")
print("모여라 양주인")
print("작성시간:", now.strftime('%Y-%m-%D %H:%M:%S'))
