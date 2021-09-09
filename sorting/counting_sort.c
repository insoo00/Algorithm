#include <stdio.h>

void print_sort(char* s, int data[], int n)
{
    int i;
    printf("%s:", s);
    for (i = 0; i < n; i++)
        printf("%d ", data[i]);
    printf("\n");
}

int find_max(int data[], int size)
{
    int max = data[0];
    for (int i = 1; i < size; i++) {
        if (data[i] > data[i - 1])
            max = data[i];
    }
    return max;
}

void countingSort(int data[], int sort_data[], int size, int max)
{
    int count[max+1];
    int i, j;
    for (i = 0; i <= max; i++)
        count[i] = 0;
    for (j = 0; j < size; j++) 
        count[data[j]]++;
    for (i = 1; i <= max; i++)
        count[i] = count[i] + count[i - 1];
    for (int j = size-1; j >= 0; j--) {
        sort_data[count[data[j]]-1] = data[j];
        count[data[j]]--;
    }
}

int main()
{
    int data[15] = { 1, 3, 2, 4, 1, 23, 12, 9, 18, 12, 3, 12, 3, 23, 23 };
    int sort_data[15];
    int max = find_max(data, 15);
    print_sort("Data: ", data, 15);

    countingSort(data, sort_data, 15, max);
    print_sort("counting sort ", sort_data, 15);
}
