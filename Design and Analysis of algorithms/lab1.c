/*
 * Program: Bubble Sort with RAM Model
 * Course: Design and Analysis of Algorithms 
 * Objective: Find time complexity of Bubble Sort using RAM operations count
 */

#include <stdio.h>

int main() {
    int a[100], n, i, j, temp, count = 0;

    // Input size of array
    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n); 
    count += 6; // RAM operations for input

    // Input array elements
    printf("Enter elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        count++; // RAM operation for each input
    }

    // Bubble Sort algorithm
    for(i = 0; i < n-1; i++) {
        count++; // loop operation
        for(j = 0; j < n-i-1; j++) {
            count++; // inner loop operation
            if(a[j] > a[j+1]) {
                // Swap elements
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                count += 3; // swap operations
            }
        }
    }

    // Print sorted array
    printf("Sorted array:\n");
    for(i = 0; i < n; i++) {
        printf("%d ", a[i]);
        count++; // print operation
    }

    // Display RAM operations and complexity
    printf("\nTotal RAM operations = %d\n", count);
    printf("Time Complexity = O(n^2)\n");

    return 0;
}
