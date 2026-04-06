/*
 * Program: Merge Sort with Execution Time
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Sort numbers using Merge Sort and measure execution time
 */

#include <stdio.h>
#include <time.h>

// Merge two sorted halves
void merge(int a[], int l, int m, int r) {
    int n1 = m - l + 1;   // size of left subarray
    int n2 = r - m;       // size of right subarray
    int L[n1], R[n2];     // temporary arrays

    // Copy data into temporary arrays
    for(int i = 0; i < n1; i++) L[i] = a[l+i];
    for(int j = 0; j < n2; j++) R[j] = a[m+1+j];

    int i = 0, j = 0, k = l;

    // Merge back into original array
    while(i < n1 && j < n2) {
        if(L[i] <= R[j]) a[k++] = L[i++];
        else a[k++] = R[j++];
    }

    // Copy remaining elements
    while(i < n1) a[k++] = L[i++];
    while(j < n2) a[k++] = R[j++];
}

// Recursive Merge Sort
void mergeSort(int a[], int l, int r) {
    if(l < r) {
        int m = (l+r)/2;
        mergeSort(a, l, m);
        mergeSort(a, m+1, r);
        merge(a, l, m, r);
    }
}

int main() {
    int a[100], n;
    clock_t s, e;
    double t;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(int i = 0; i < n; i++) scanf("%d", &a[i]);

    // Start timer
    s = clock();
    mergeSort(a, 0, n-1);
    e = clock();

    // Print sorted array
    printf("Sorted array:\n");
    for(int i = 0; i < n; i++) printf("%d ", a[i]);

    // Calculate execution time
    t = (double)(e - s) / CLOCKS_PER_SEC;
    printf("\nExecution Time: %f seconds\n", t);

    return 0;
}
