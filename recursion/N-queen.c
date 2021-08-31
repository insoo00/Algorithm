#include <stdio.h>
#include <stdlib.h> //abs()

#define N   8

int cols[N+1];

int promising(int h) {
    for(int i=1; i<h; i++) {
        if(cols[i] == cols[h])
            return 0;
        if(h-i == abs(cols[h]-cols[i]))
            return 0;
    }
    return 1;
}

int queens(int h) {
    if(!promising(h))
        return 0;
    if(h == N) {
        for(h=1; h<=N; h++) {
            printf("(%d, %d)\n", h, cols[h]);
        }
        return 1;
    }
    for(int i=1; i<=N; i++) {
        cols[h+1] = i;
        if(queens(h+1))
            return 1;
    }
    return 0;    
}

int main() {
    if(queens(0) == 1)
        printf("success\n");
}

