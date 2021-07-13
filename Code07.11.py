##함수
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1)%SIZE == front):
        return False
    else :
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅!')
        return None
    front = (rear+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data


def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('queue max')
        return
    rear = (rear+1)%SIZE
    queue[rear] = data


def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('empty')
        return None
    return queue[front + 1]


##변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0, 0 #원형큐 초기화
