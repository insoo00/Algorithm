#include <stdio.h>

#define MAX_N 100000

int price[MAX_N+1];
int N = 0;
int result = 0;
int total = 0;
int sale = 0;

void swap(int data[], int a, int b)
{
    int tmp = 0;
    tmp = data[a];
    data[a] = data[b];
    data[b] = tmp;
}

int partition(int data[], int p, int r)
{
    int pivot = data[r];
    int i = p-1, j;
    for(j=p; j<r; j++) {
        if(data[j] <= pivot)
            swap(data, ++i, j);
    }
    swap(data, i+1, r);
    return i+1;
}

void quickSort(int data[], int p, int r)
{
    int pivot;
    if(p < r) {
        pivot = partition(data, p , r);
        quickSort(data, p ,pivot-1);
        quickSort(data, pivot+1, r);
    }
}

void setsale(int data[]) {
    int i = 0;
    if(N%3 == 0)
        i = 1;
    else if(N%3 == 1)
        i = 2;
    else
        i = 3;
    while(i<N) {
        sale += price[i];
        i += 3;
    }
}

void settotal(int data[]) {
    for(int i=1; i<=N; i++)
        total += price[i];
}


int main() {
    int T;

    freopen("input.txt", "r", stdin);
    scanf("%d", &T);

    for(int i=0; i<T; i++) {
        scanf("%d", &N);

        for(int j=1; j<=N; j++)
            scanf("%d", &price[j]);

        quickSort(price, 1, N);
        settotal(price);
		setsale(price);

        result = total - sale;
        printf("%d\n", result);
		result = total = sale = 0;
    }
}