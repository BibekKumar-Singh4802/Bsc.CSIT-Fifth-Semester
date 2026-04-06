/*
 * Program: GCD of Two Numbers
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find GCD using Euclidean Algorithm and RAM operations count
 */

#include <stdio.h>

int main() {
    int a, b, temp, count = 0;

    printf("By Bibek Kumar Singh\nEnter two numbers: ");
    scanf("%d %d", &a, &b); 
    count += 3;

    // Euclidean Algorithm
    while(b != 0) {
        count++;
        temp = b;
        b = a % b;
        a = temp;
        count += 3;
    }

    count++;
    printf("GCD = %d\n", a);
    printf("Total RAM operations = %d\n", count);

    return 0;
}
