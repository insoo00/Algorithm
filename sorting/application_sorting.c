#include <stdio.h>
#include <stdlib.h>

void print_sort(char* s, int data[], int n)
{
    int i;
    printf("%s:", s);
    for (i = 0; i < n; i++)
        printf("%d ", data[i]);
    printf("\n");
}

void swap(int data[], int a, int b)
{
    int tmp = 0;
    tmp = data[a];
    data[a] = data[b];
    data[b] = tmp;
}

void merge(int data[], int p, int q, int r, int size)
{
    int tmp[size];
    int i = p;
    int j = q + 1;
    int k = p;

    while(i<=q && j<=r) {
        if(data[i] <= data[j]) 
            tmp[k++] = data[i++];
        else 
            tmp[k++] = data[j++];
    }
    while(i<=q) 
        tmp[k++] = data[i++];
    while(j<=r) 
        tmp[k++] = data[j++];
      
    for (int x = p; x <= r; x++) 
        data[x] = tmp[x];
}

void mergeSort(int data[], int p, int r, int size)
{
    int q;
    if (p < r) {
        q = (p + r) / 2;
        mergeSort(data, p, q, size);
        mergeSort(data, q + 1, r, size);
        merge(data, p, q, r, size);
    }
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
    //퀵 정렬 구현
    int pivot;
    if(p < r) {
        pivot = partition(data, p , r);
        quickSort(data, p ,pivot-1);
        quickSort(data, pivot+1, r);
    }
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
    print_sort("quickInput", quickInput, 10);

    mergeSort(mergeInput, 0, 9, 10);
    print_sort("mergeSort", mergeInput, 10);
    quickSort(quickInput, 0, 9);
    print_sort("quickSort", quickInput, 10);

}
