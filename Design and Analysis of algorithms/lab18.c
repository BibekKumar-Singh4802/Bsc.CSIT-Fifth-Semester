/*
 * Program: Randomized Selection (Expected Linear Time)
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find ith smallest element using randomized selection
 */

#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

int part(int a[], int l, int h) {
    int p = a[h], i = l-1;
    for(int j = l; j < h; j++) if(a[j] <= p) swap(&a[++i], &a[j]);
    swap(&a[i+1], &a[h]);
    return i+1;
}

int randPart(int a[], int l, int h) {
    int r = l + rand() % (h-l+1);
    swap(&a[r], &a[h]);
    return part(a, l, h);
}

int selectK(int a[], int l, int h, int k) {
    if(l <= h) {
        int pi = randPart(a, l, h);
        if(pi == k) return a[pi];
        else if(pi > k) return selectK(a, l, pi-1, k);
        else return selectK(a, pi+1, h, k);
    }
    return -1;
}

int main() {
    int n, i, k;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n);

    int a[n];
    printf("Enter elements:\n");
    for(i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Enter i (position): ");
    scanf("%d", &k);

    int res = selectK(a, 0, n-1, k-1);
    printf("%dth smallest element = %d\n", k, res);

    return 0;
}
