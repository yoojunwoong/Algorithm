katok =['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position) :
    KLen = len(katok);
    katok[position] = None;

    for i in range(position+1, KLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[KLen-1]);

print(katok)
delete_data(1)
print(katok)
delete_data(3)
print(katok)
