#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_QUEUE_SIZE 100

typedef struct
{
    int id;       //이벤트 ID, 처음 이벤트 1, 이후 이벤트마다 1씩 증가
    int tEvent;   //이벤트 발생 시간
    int tService; //이벤트 처리 시간
} Event;
typedef Event element; //큐에 이벤트 구조체를 저장
typedef struct
{
    int front;
    int rear;
    element data[MAX_QUEUE_SIZE];
} QueueType; //큐 구조체

int tSimulation;   //시뮬레이션 시간
double probEvent;  //단위시간(1초)에 이벤트가 발생활 확률
int tMaxServise;   //한 이벤트에 대한 최대 처리 시간
int totalWaitTime; //전체 대기 시간
int nEvents;       // 전체 이벤트의 수
int nServedEvents; //처리된 전체 이벤트 수

double unitRand()
{
    return (rand() / (double)RAND_MAX);
}
void error(char *message)
{
    fprintf(stderr, "%s\n", message);
}

void init_queue(QueueType *q)
{
    q->front = 0;
    q->rear = 0;
}

int is_full(QueueType *q)
{
    return (q->front == (q->rear + 1) % MAX_QUEUE_SIZE);
}

int is_empty(QueueType *q)
{
    return (q->front == q->rear);
}

void enqueue(QueueType *q, element item)
{
    if (is_full(q))
    {
        error("queue is full\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = item;
}

element dequeue(QueueType *q)
{
    if (is_empty(q))
    {
        error("queue is empty\n");
        exit(1);
    }
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    return q->data[q->front];
}

void insertEvent(QueueType *q, int eventTime)
{
    nEvents++;
    Event temp;
    temp.id = nEvents;
    temp.tEvent = eventTime;
    //wrong  +1
    temp.tService = rand() % (tMaxServise + 1);
    enqueue(q, temp);

    printf("\t Event %d 발생 (처리시간: %d초)\n", temp.id, temp.tService);
}

int main()
{
    QueueType q;
    init_queue(&q);
    Event temp;
    int serviceTime = 0; //현재 처리 중인 이벤트의 남은 처리 시간
    int sec;

    srand((unsigned int)time(NULL));

    totalWaitTime = 0;
    nEvents = 0;
    nServedEvents = 0;

    printf("시뮬레이션 할 최대 시간 (단위: 초) = ");
    scanf("%d", &tSimulation);
    printf("단위시간(1초)에 이벤트가 발생활 확률 (예: 0.1) =  ");
    scanf("%lf", &probEvent);
    printf("한 이벤트에 대한 최대 처리 시간 (단위: 초) = ");
    scanf("%d", &tMaxServise);
    printf("===========================\n");

    for (sec = 0; sec < tSimulation; sec++)
    {
        printf("현재 시간: %d\n", sec);

        //이벤트 발생 여부 확인
        if (unitRand() <= probEvent)
            insertEvent(&q, sec);

        //현재 처리 중인 이벤트가 없고, 처리할 이벤트가 큐에 있으면 해당 이벤트 처리 시작
        if (serviceTime <= 0 && !is_empty(&q))
        {
            temp = dequeue(&q);
            nServedEvents++;
            totalWaitTime += sec - temp.tEvent;
            serviceTime = temp.tService;
            printf("\t Event %d 처리 시작 (대기시간: %d)\n", temp.id, sec - temp.tEvent);
        }
        //serviceTime 1 감소
        serviceTime--;
    }
    //시뮬레이션 결과 출력
    printf("===========================\n");
    printf("Simulation Report! \n");
    printf("처리된 이벤트 수\t = %d \n", nServedEvents);
    printf("전체 대기 시간 \t = %d \n", totalWaitTime);
    printf("이벤트 당 평균대기시간\t = %lf \n", ((double)totalWaitTime / nServedEvents));
    printf("현재 대기 이벤트 수\t = %d \n", (nEvents - nServedEvents));
}