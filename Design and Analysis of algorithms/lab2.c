/*
 * Program: Insertion Sort with RAM Model
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find time complexity of Insertion Sort using RAM operations count
 */

#include <stdio.h>

int main() {
    int a[100], n, i, j, key, count = 0;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n); 
    count += 3;

    printf("Enter elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        count++;
    }

    // Insertion Sort
    for(i = 1; i < n; i++) {
        key = a[i];
        j = i - 1;
        count += 2;

        while(j >= 0 && a[j] > key) {
            a[j+1] = a[j];
            j--;
            count += 2;
        }
        a[j+1] = key;
        count++;
    }

    printf("Sorted array:\n");
    for(i = 0; i < n; i++) {
        printf("%d ", a[i]);
        count++;
    }

    printf("\nTotal RAM operations = %d\n", count);
    printf("Time Complexity = O(n^2)\n");

    return 0;
}
