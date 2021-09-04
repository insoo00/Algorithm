#include <stdio.h>

void selectionSort(int data[], int n)
{
    int i, j, index, tmp = 0;
    for (i = n - 1; i > 0; i--) {
        index = 0;
        for (j = 0; j <= i; j++) {
            if (data[j] > data[index])
                index = j;
        }
        if (i != index) {
            tmp = data[i];
            data[i] = data[index];
            data[index] = tmp;
            //check sorting
            // for (i = 0; i < 10; i++)
            //     printf("%d ", data[i]);
            // printf("\n");
        }
    }
}

// void bubbleSort(int data[], int n) {

// }

// void insertionSort(int data[], int n) {

// }

int main()
{
    int i;
    int data[10] = { 3, 31, 48, 73, 8, 11, 20, 29, 65, 15 };
    selectionSort(data, 10);
    printf("selectionSort\n");
    for (i = 0; i < 10; i++)
        printf("%d ", data[i]);
    printf("\n");
}
