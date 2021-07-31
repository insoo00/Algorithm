#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int sumAlgorithmA(int n)
{
    return (n * (n + 1) / 2);
}

int sumAlgorithmB(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
        sum += i;
    return sum;
}

int sumAlgorithmC(int n)
{
    int sum = 0;
    int i, j = 1;
    for (i = 1; i <= n; i++)
        for (j = 1; j <= i; j++)
            sum++;
    return sum;
}

int main()
{
    double timeA, timeB, timeC;
    clock_t start, finish;
    int sumA, sumB, sumC;

    start = clock();
    sumA = sumAlgorithmA(1000000);
    finish = clock();
    timeA = ((double)(finish - start)) / CLOCKS_PER_SEC;

    start = clock();
    sumB = sumAlgorithmB(1000000);
    finish = clock();
    timeB = ((double)(finish - start)) / CLOCKS_PER_SEC;

    start = clock();
    sumC = sumAlgorithmC(1000000);
    finish = clock();
    timeC = ((double)(finish - start)) / CLOCKS_PER_SEC;

    printf("sum_A: %d\t Time_A: %lf\nsum_B: %d\t Time_B: %lf\nsum_C: %d\t Time_C: %lf\n", sumA, timeA, sumB, timeB, sumC, timeC);
}