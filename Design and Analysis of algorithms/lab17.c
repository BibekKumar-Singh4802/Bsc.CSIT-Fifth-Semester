/*
 * Program: Min-Max Algorithm
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find minimum and maximum values from a dataset
 */

#include <stdio.h>

int main() {
    int n, i, min, max;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n);

    int a[n];
    printf("Enter elements:\n");
    for(i = 0; i < n; i++) scanf("%d", &a[i]);

    min = max = a[0];

    for(i = 1; i < n; i++) {
        if(a[i] < min) min = a[i];
        if(a[i] > max) max = a[i];
    }

    printf("Minimum = %d\n", min);
    printf("Maximum = %d\n", max);

    return 0;
}
