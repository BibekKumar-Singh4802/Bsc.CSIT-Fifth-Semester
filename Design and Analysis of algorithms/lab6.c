/*
 * Program: Randomized Quick Sort with Execution Time
 * Course: Design and Analysis of Algorithms (CSC314)
 * Author: Bibek Kumar Singh
 * Objective: Sort numbers using Randomized Quick Sort and measure execution time
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

int partition(int a[], int l, int h) {
    int p = a[h], i = l-1;
    for(int j = l; j < h; j++) if(a[j] < p) swap(&a[++i], &a[j]);
    swap(&a[i+1], &a[h]);
    return i+1;
}

int randPart(int a[], int l, int h) {
    int r = l + rand() % (h-l+1);
    swap(&a[r], &a[h]);
    return partition(a, l, h);
}

void rqSort(int a[], int l, int h) {
    if(l < h) {
        int pi = randPart(a, l, h);
        rqSort(a, l, pi-1);
        rqSort(a, pi+1, h);
    }
}

int main() {
    int a[100], n, i;
    clock_t s, e;
    double t;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++) scanf("%d", &a[i]);

    s = clock();
    rqSort(a, 0, n-1);
    e = clock();

    printf("Sorted array:\n");
    for(i = 0; i < n; i++) printf("%d ", a[i]);

    t = (double)(e-s)/CLOCKS_PER_SEC;
    printf("\nExecution Time: %f seconds\n", t);

    return 0;
}
