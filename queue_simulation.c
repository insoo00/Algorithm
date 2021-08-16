#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_QUEUE_SIZE 31 //대기실 크기: 30명
#define CUS_COME_TERM 15 //고객의 주문 간격:15초
#define CHE_BUR 0 //치즈버거 상수
#define BUL_BUR 1 //불고기버거 상수
#define DUB_BUR 2 //더블버거 상수
#define CHE_TERM 12 //치즈버거 제작 시간: 12초
#define BUL_TERM 15 //불고기버거 제작 시간: 15초
#define DUB_TERM 24 //더블버거 제작 시간: 24초

typedef int element; //큐에 햄버거 제작 시간 저장
typedef struct {
    int front;
    int rear;
    element data[MAX_QUEUE_SIZE];
} QueueType; //큐 구조체

void error(char* message)
{
    fprintf(stderr, "%s\n", message);
}

void init_queue(QueueType* q)
{
    q->front = 0;
    q->rear = 0;
}

int is_full(QueueType* q)
{
    return (q->front == (q->rear + 1) % MAX_QUEUE_SIZE);
}

int is_empty(QueueType* q)
{
    return (q->front == q->rear);
}

void enqueue(QueueType* q, element item)
{
    if (is_full(q)) {
        error("queue is full\n");
        return;
    }
    q->rear = (q->front + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = item;
}

element dequeue(QueueType* q)
{
    if (is_empty(q)) {
        error("queue is empty\n");
        return -1;
    }
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    return q->data[q->front];
}

int main()
{
    int makeProc = 0; //햄버거 제작 진행상황 (남은 시간)
    int cheOrder = 0, bulOrder = 0, dubOrder = 0; //치즈버거, 불고기버거, 더블버거 주문량
    int sec;
    QueueType q;
    init_queue(&q);
    srand(time(NULL));

    for (sec = 0; sec < 3600; sec++) {
        if (sec % CUS_COME_TERM == 0) {
            switch (rand() % 3) {
            case CHE_BUR:
                enqueue(&q, CHE_TERM);
                cheOrder++;
                break;
            case BUL_BUR:
                enqueue(&q, BUL_TERM);
                bulOrder++;
                break;
            case DUB_BUR:
                enqueue(&q, DUB_TERM);
                dubOrder++;
                break;
            }
        }
        if (makeProc <= 0 && !is_empty(&q))
            makeProc = dequeue(&q);
        makeProc--;
    }
    printf("Simulation Report! \n");
    printf(" - Cheese burger: %d \n", cheOrder);
    printf(" - Bulgogi burger: %d \n", bulOrder);
    printf(" - Double burger %d \n", dubOrder);
    printf(" - Waiting room size: %d \n", MAX_QUEUE_SIZE - 1);
}