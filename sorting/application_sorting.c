#include <stdio.h>
#include <stdlib.h>

void print_sort(char* s, int A[], int n)
{
    int i;
    printf("%s:", s);
    for (i = 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\n");
}
// https://airsbigdata.tistory.com/167
void merge(int A[], int p, int q, int r)
{
    int B[r - p + 1];
    int i = p;
    int j = q + 1;
    int k = p;
    int x;

    printf("merge %d %d %d\n", p, q, r);
    printf("i: %d, j: %d\n", i, j);
    printf("A[i]: %d, A[j]: %d\n", A[i], A[j]);

    while (i <= q && j <= r) {
        if (A[i] <= A[j])
            B[k++] = A[i++];
        else
            B[k++] = A[j++];
    }
    if (i > q) {
        for (x = 0; x <= r; x++)
            B[k++] = A[x];
    } else {
        for (x = i; x <= r; x++)
            B[k++] = A[x];
    }

    // for (k = 0; k < r - p + 1; k++) {
    //     printf("for[k]: %d\n", k);

    //     if (A[i] < A[j]) {
    //         printf("if[k]: %d\n", k);
    //         B[k] = A[i++];
    //     } else if (A[i] > A[j]) {
    //         printf("k: %d\n", k);
    //         if (j > r)
    //             B[k] = A[i++];
    //         else
    //             B[k] = A[j++];
    //         printf("merge[%d]: %d\n", k, B[k]);
    //     }
    for (k = 0; k < r - p + 1; k++) {
        A[k] = B[k];
    }
}
void mergeSort(int A[], int p, int r)
{
    int q;
    if (p < r) {
        q = (p + r) / 2;
        mergeSort(A, p, q);
        mergeSort(A, q + 1, r);
        merge(A, p, q, r);
    }
}

int partition(int A[], int p, int r)
{
    //퀵 정렬의 partotion 함수 구현
}

void quickSort(int A[], int p, int r)
{
    //퀵 정렬 구현
}

int main()
{
    int i, x, mergeInput[100000], quickInput[100000];
    for (i = 0; i < 10; i++) {
        x = rand();
        mergeInput[i] = x;
        quickInput[i] = x;
    }
    print_sort("mergeInput", mergeInput, 10);
    // print_sort("quickInput", quickInput, 10);

    mergeSort(mergeInput, 0, 9);
    print_sort("mergeSort", mergeInput, 10);

    // quickSort(quickInput, 0, 9);
}
