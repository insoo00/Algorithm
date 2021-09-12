#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int data[], int a, int b)
{
    int tmp = 0;
    tmp = data[a];
    data[a] = data[b];
    data[b] = tmp;
}

int findPivot(int r)
{
    int index = 0;
    int pivot = 2;

    int x;
    if (r % 5 == 0)
        x = r / 5;
    else
        x = r / 5 + 1;

    int lange[x];

    while (pivot <= r) {
        lange[index] = pivot;
        pivot += 5;
        index++;
    }
    return lange[x / 2];
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

int worst_partition(int data[], int p, int r)
{
    int pivotIndex = findPivot(r);
    swap(data, pivotIndex, r);

    int pivot = data[r];
    int i = p - 1, j;
    for (j = p; j < r; j++) {
        if (data[j] <= pivot)
            swap(data, ++i, j);
    }
    swap(data, i + 1, r);
    return i + 1;
}

int avg_selection(int data[], int p, int r, int n)
{
    int q, k;
    if (p == r)
        return data[p];
    q = partition(data, p, r);
    k = q - p + 1;
    if (n < k)
        return avg_selection(data, p, q - 1, n);
    else if (n == k)
        return data[q];
    else
        return avg_selection(data, q + 1, r, n - k);
}

int worst_selection(int data[], int p, int r, int n)
{
    int i, q, k;
    if (p == r)
        return data[p];
    else if (r - p + 1 <= 5) {
        for (i = 0; i <= r - p + 1; i++) {
            if (i == n)
                return data[i];
        }
    }
    q = worst_partition(data, p, r);
    k = q - p + 1;
    if (n < k)
        return worst_selection(data, p, q - 1, n);
    else if (n == k)
        return data[q];
    else
        return worst_selection(data, q + 1, r, n - k);
}

int main()
{

    int avg_data[100000];
    int worst_data[100000];
    int avg_res, worst_res;
    int i, x;
    for (i = 0; i < 10; i++) {
        x = rand();
        avg_data[i] = x;
        worst_data[i] = x;
        printf("%d ", avg_data[i]);
    }
    printf("\n");

    x = (rand() % 10);
    printf("x: %d\n", x);
    avg_res = avg_selection(avg_data, 0, 9, x);
    printf("avg_res: %d\n", avg_res);
    worst_res = worst_selection(worst_data, 0, 9, x);
    printf("worst_res: %d\n", worst_res);

    double timeA, timeB;
    clock_t start, finish;
    for (int j = 0; j < 5; j++) {
        for (i = 0; i < 100000; i++) {
            x = rand();
            avg_data[i] = x;
            worst_data[i] = x;
        }
        x = (rand() % 10);
        start = clock();
        avg_res = avg_selection(avg_data, 0, 99999, x);
        finish = clock();
        timeA = ((double)(finish - start)) / CLOCKS_PER_SEC;

        start = clock();
        worst_res = worst_selection(worst_data, 0, 99999, x);
        finish = clock();
        timeB = ((double)(finish - start)) / CLOCKS_PER_SEC;

        printf("avg_selction: %lf\t worst_selction: %lf\n", timeA, timeB);
    }
}