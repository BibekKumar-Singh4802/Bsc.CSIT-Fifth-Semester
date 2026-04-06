/*
 * Program: Selection Sort with RAM Model
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find time complexity of Selection Sort using RAM operations count
 */

#include <stdio.h>

int main() {
    int a[100], n, i, j, min, temp, count = 0;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n); 
    count += 3;

    printf("Enter elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        count++;
    }

    // Selection Sort
    for(i = 0; i < n-1; i++) {
        min = i;
        count++;
        for(j = i+1; j < n; j++) {
            count++;
            if(a[j] < a[min]) {
                min = j;
                count++;
            }
        }
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
        count += 3;
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
