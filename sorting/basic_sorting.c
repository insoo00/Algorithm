#include <stdio.h>

void selectionSort(int data[], int n) {
    int i;
    for(i=n; i<2; i--) {
        if(data[n] < data[i])
            data[n] = data[i];
    }
}

// void bubbleSort(int data[], int n) {

// }

// void insertionSort(int data[], int n) {

// }

int main() {
    int i;
    int data[10] = {3, 31, 48, 73, 8, 11, 20, 29, 65, 15};
    selectionSort(data, 10);
    for(i=0; i<10; i++)
        printf("%d ", data[i]);
    printf("\n");
}