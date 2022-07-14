'''
알파벳 대소문자로 입력이 주어질 때 가장 많은 문자를 출력하는 프로그램이다.
단 가장 많이 입력된 문자가 여러개일 때 ?를 출력한다.

입력 예)
EliceIsGoodAndNicePerson
출력 예)
E

입력 예)
aaabbbcdefghijklmnopqrstuvwxyz
출력 예)
?
'''
from string import ascii_lowercase
str_ = input().lower()
s_dict = {}
for a in ascii_lowercase:
    s_dict[a] = 0

for s in str_:
    s_dict[s] += 1

kv = s_dict.items()
max_ = max(kv, key = lambda x: x[1])
if list(s_dict.values()).count(max_[1]) >= 2:
    print('?')
else:
    print(max_[0].upper())