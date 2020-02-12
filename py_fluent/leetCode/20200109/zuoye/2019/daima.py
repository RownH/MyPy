import collections
import re
 
patt = re.compile("\w+")
counter = collections.Counter(patt.findall(
    open('data.text','rt').read()
    ))
counter1 = collections.Counter(patt.findall(
    open('data2.text','rt').read()
    ))
#print(counter)
with open('result.text', 'w') as file_object:
    for i,j in counter.items():
        file_object.write(str(i)+":"+str(j)+'\n')
with open('result1.text', 'w') as file_object:
    for i,j in counter1.items():
        file_object.write(str(i)+":"+str(j)+'\n')
counter2=set(counter.elements())&set(counter1.elements())
with open('result2.text', 'w') as file_object:
    for i in counter2:
        file_object.write(str(i)+'\n')
# print(set(counter.elements()) &set(counter1.elements()))
# for word, times in counter.most_common(10):
#     print(word,times)
