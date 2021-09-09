#include<stdio.h>
#include<stdlib.h>
#define SWAP(x, y, t) ((t)=(x), (x)=(y), (y)=(t))
#define BASE 10		// 10진법 -> Counting Sort할 때 사용
 
 
void Radix_Sort(int[], int, int);
int BaseMaxNumber(int[], int, int, int);
void Counting_Sort(int[], int, int, int, int);
 
int main()
{
	int i;
	int length;
	int arr[10] = { 10, 28, 30, 2, 15, 8, 67, 45, 3, 100, };
 
	length = sizeof(arr) / sizeof(int);	
 
	Radix_Sort(arr, length, BASE);
 
	for (i = 0; i < length; i++)
		printf("%d ", arr[i]);
    printf("\n");
}
 
//Radix_Sort 함수
void Radix_Sort(int arr[], int length, int base) {
 
	int i, ex, k = 0, max;
 
	for (i = 0; i < length; i++) {         // 최대 값 구함.   
		if (k < arr[i])
			k = arr[i];
	}
 
	for (ex = 1; ex <= k; ex *= base) {
		max = BaseMaxNumber(arr, length, ex, base);
		Counting_Sort(arr, max, length, ex, base);
	}
}
 
// MaxNumber(자리 수 기준으로 최대 값 구하는 함수) --> int형(year)
int BaseMaxNumber(int arr[], int length, int ex, int base) {
	
	int i, max = 0;
	
	for (i = 0; i < length; i++) {
		if (max<(arr[i] / ex) % base) {
			max = arr[i];
		}
	}
	return max;
}
 
// Countin_Sort 함수
// A : 배열, k : 제일 큰 값(자리 수 기준), n : 배열 원소의 개수, ex : 자리수(1, 10, 100..), base : 진법(10진수)
void Counting_Sort(int A[], int k, int n, int ex, int base) {
 
	int i, j;
	int *C;
	int *B;
 
	B = (int*)malloc(sizeof(int)*n);		// 임시 배열 B
	C = (int*)malloc(sizeof(int)*(k + 1));		// 누적 합 배열 C
 
	for (i = 0; i <= k; i++)			// C배열 0으로 초기화.
		C[i] = 0;
	for (i = 0; i < n; i++)				// C배열에 A배열 자리 수 기준으로 카운트. 
		C[(A[i] / ex) % base]++;
	for (i = 1; i <= k; i++)			// C배열 누적 합.
		C[i] += C[i - 1];
	for (i = n - 1; i >= 0; i--) {			// C배열을 통해 B배열에 A배열의 값 매칭.
		j = (A[i] / ex) % base;
		B[C[j] - 1] = A[i];
		C[(A[i] / ex) % base]--;
	}
 
	for (i = 0; i < n; i++)				// B배열(정렬된 배열)을 A배열로 옮기기.
		A[i] = B[i];
 
	free(B);
	free(C);
}