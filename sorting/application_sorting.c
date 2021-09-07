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

void merge(int A[], int p, int q, int r, int size)
{
    int B[size];
    int i = p;
    int j = q + 1;
    int k = p;

    while(i<=q && j<=r) {
        if(A[i] <= A[j]) 
            B[k++] = A[i++];
        else 
            B[k++] = A[j++];
    }
    while(i<=q) 
        B[k++] = A[i++];
    while(j<=r) 
        B[k++] = A[j++];
      
    for (int x = p; x <= r; x++) 
        A[x] = B[x];
}

void mergeSort(int A[], int p, int r, int size)
{
    int q;
    if (p < r) {
        q = (p + r) / 2;
        mergeSort(A, p, q, size);
        mergeSort(A, q + 1, r, size);
        merge(A, p, q, r, size);
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

    mergeSort(mergeInput, 0, 9, 10);
    print_sort("mergeSort", mergeInput, 10);

    // quickSort(quickInput, 0, 9);
}
