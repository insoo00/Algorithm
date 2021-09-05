#include <stdio.h>

void init_sort(int data[])
{
    //{ 31, 3, 48, 73, 8, 11, 20, 29, 65, 15 };
    data[0] = 31;
    data[1] = 3;
    data[2] = 48;
    data[3] = 73;
    data[4] = 8;
    data[5] = 11;
    data[6] = 20;
    data[7] = 29;
    data[8] = 65;
    data[9] = 15;
}

void print_sort(int data[], int n)
{
    for (int i = 0; i < n; i++)
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

void selectionSort(int data[], int n)
{
    int i, j, index;
    for (i = n - 1; i > 0; i--) {
        index = 0;
        for (j = 0; j <= i; j++) {
            if (data[j] > data[index])
                index = j;
        }
        if (i != index) {
            swap(data, i, index);
            //check sorting
            // print_sort(data, 10);
        }
    }
}

void bubbleSort(int data[], int n)
{
    int i, j;
    for (i = n - 1; i > 0; i--) {
        for (j = 0; j < i; j++) {
            if (data[j] > data[j + 1]) {
                swap(data, j, j + 1);
                //check sorting
                // print_sort(data, 10);
            }
        }
    }
}

void insertionSort(int data[], int n)
{
    int i, j, key;
    for (i = 0; i < n - 1; i++) {
        key = data[i + 1];
        for (j = i; j >= 0 && data[j] > key; j--) {
            data[j + 1] = data[j];
        }
        data[j + 1] = key;
        //check sorting
        // print_sort(data, 10);
    }
}

int main()
{
    int data[10];

    init_sort(data);
    selectionSort(data, 10);
    printf("selectionSort\n");
    print_sort(data, 10);
    printf("\n");

    init_sort(data);
    bubbleSort(data, 10);
    printf("bubbleSort\n");
    print_sort(data, 10);
    printf("\n");

    init_sort(data);
    insertionSort(data, 10);
    printf("insertionSort\n");
    print_sort(data, 10);
    printf("\n");
}
