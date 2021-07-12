#함수 선언부
def add_data(friend):

    katok.append(None);
    KLen = len(katok)
    katok[KLen-1] = friend

def insert_data(position, friend) :
    katok.append(None);
    KLen = len(katok);

    for i in range(KLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend;

def delete_data(position) :
    KLen = len(katok);
    katok[position] = None;

#전역 변수부
katok = []
select = -1 # 1.추가 2.삽입 3.삭제 4.종류
#메인 코드부
if __name__ == '__main__':
    while (select !=4) :
        select = int(input('1. 추가 2. 삽입 3.삭제 4.종류-->'))

        if (select == 1):
            data = input("추가할 데이터-->")
            add_data(data);
            print(katok)
        elif(select == 2):
            pos = int(input("삽입할 데이터-->"))
            data = input("추가할 데이터-->")
            insert_data(pos,data)
            print(katok)
        elif (select == 3):
            pos = int(input("삭제할 위치-->"));
            delete_data(pos)
            print(katok)
        elif (select ==4 ):
            print(katok)
            exit()
        else :
            print("1~4중 하나를 입력하세요.")
            continue;


