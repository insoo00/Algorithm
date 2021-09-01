#include <stdio.h>

#define MAX_N 15

int weight[MAX_N+1];
int result = 0;
int N = 0;

void countTeams(int h, int wA, int wB, int wC) {
    //base case
    if(h == N) {
        if((wA == wB) && (wA == wC))
            result++;
        return ;
    }

    countTeams(h+1, wA + weight[h+1], wB, wC);
    countTeams(h+1, wA , wB + weight[h+1], wC);
    countTeams(h+1, wA , wB, wC + weight[h+1]);
    countTeams(h+1, wA , wB, wC);
}

int main() {
    int T;

    freopen("input.txt", "r", stdin);
    scanf("%d", &T);

    for(int i=0; i<T; i++) {
        scanf("%d", &N);

        for(int j=1; j<=N; j++)
            scanf("%d", &weight[j]);

        countTeams(0, 0, 0, 0);
        printf("%d\n", result);
        result = 0;
    }
}