"""
このファイルに解答コードを書いてください
"""
# coding: utf-8
test_data = open("input.txt", "r")
number = [] #数入力
s = [] #文字
dic = {}
lines = test_data.readlines()

for line in range(0,len(lines)-1):
    i, j = lines[line].split(":")
    dic.setdefault(int(i), j.strip()) 


number2 = int(lines[len(lines)-1]) #注目する値

#結果出力
result = ""
for i, j in sorted(dic.items()):
    if(number2 % i == 0):
        result = result + j

if (result == ""):
    print(number2)
else:
    print(result)