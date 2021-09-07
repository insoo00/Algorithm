#include <stdio.h>

void print_sort(int data[], int n) {
    for(int i=0; i<n; i++)
        printf("%d ",data[i]);
    printf("\n");
}

void swap(int data[], int a, int b)
{
    int tmp = 0;
    tmp = data[a];
    data[a] = data[b];
    data[b] = tmp;
}

void heapify(int data[], int root, int n) {
    int left = 2*root+1;
    int right = 2*root;
    int smaller;

    if(right <= n+1) {
        if(data[left] < data[right])
            smaller = left;
        else
            smaller = right;
    }
    else if(left <= n+1)
        smaller = left;
    else    
        return ;

    if(data[smaller] < data[root]) {
        swap(data, smaller, root);
        heapify(data, smaller, n);
    }
}

void buildHeap(int data[], int n) {
    for(int i=(n-1)/2; i>=0; i--) {
        printf("[IN BUILDHEAP]i: %d\n ", i);
        heapify(data, i, n);
        print_sort(data, 5);
    }
}

void heapSort(int data[], int n) {
    buildHeap(data, n);
    printf("buildHeap: ");
    print_sort(data, 5);

    for(int i=n-1; i>0; i--) {
        swap(data, 0, i);
        printf("%d: %d\n", i, data[i]);
        heapify(data, 0, i-1);
    }
}

int main() {
    int data[5] = {7, 9, 4, 8, 6};
    print_sort(data, 5);
    
    heapSort(data, 5);
    print_sort(data, 5);

}