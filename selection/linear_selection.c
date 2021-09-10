#include <stdio.h>
#include <stdlib.h>

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
    int i = p - 1, j;
    for (j = p; j < r; j++) {
        if (data[j] <= pivot)
            swap(data, ++i, j);
    }
    swap(data, i + 1, r);
    return i + 1;
}

int avg_selction()
{
}

int worst_selection()
{
}

int main()
{

    int avg_data[10];
    int worst_data[10];
    int avg_res, worst_res;
    int i, x;
    for (i = 0; i < 10; i++) {
        x = rand();
        avg_data[i] = x;
        worst_data[i] = x;
    }
    x = (rand() % 10);
    avg_res = avg_selction(avg_data, x);
    worst_res = avg_selction(avg_data, x);
}