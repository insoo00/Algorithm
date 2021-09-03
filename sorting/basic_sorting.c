#include <stdio.h>

void selectionSort(int data[], int n) {
    int i, j, tmp1, tmp2, index;
    for(i=n; i>2; i--) {
        tmp1 = 0;
        index = 0;
        for(j=0; j<n; j++) {
            if(data[j] > tmp1)
                tmp1 = data[j];
                index = j;
        }
        tmp2 = data[n];
        data[n] = data[index];
        data[index] = tmp2;
    }
}

void selectionSort(int data[], int n) {
    int i, j;
    for(i=n; i>2; i--) {
        for(j=0; j<n; j++) {

        }
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