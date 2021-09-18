import hashlib
import os
test_file_input = input("바이러스 검사하실 파일을 입력하세요!:")
test_file = open(test_file_input, 'rb')
test_file_data = test_file.read()
test_file.close()
with open('virus.db', 'r') as f:
    virus_md5_list = []
    for line in f:
        virus_md5_list.append(line)
test_file_md5 = hashlib.md5(test_file_data).hexdigest() + "\n"
if test_file_md5 in virus_md5_list:
    print("이거 바이러스에요!")
    os.remove(test_file_input)
else:
    print("매우 정상적인 파일입니다")
print("Copyright 2021. Junseop Whang all rights reserved")
os.system("pause")
