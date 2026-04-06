/*
 * Program: Subset Sum using Backtracking
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find subsets that sum to a given value
 */

#include <stdio.h>

int w[50], x[50], n, sum;

void subset(int s, int k, int r) {
    if(s == sum) {
        printf("{ ");
        for(int i = 0; i < k; i++) if(x[i]) printf("%d ", w[i]);
        printf("}\n");
        return;
    }
    if(k < n && s + w[k] <= sum) {
        x[k] = 1;
        subset(s + w[k], k+1, r - w[k]);
    }
    if(k < n && s + r - w[k] >= sum && s + w[k] <= sum) {
        x[k] = 0;
        subset(s, k+1, r - w[k]);
    }
}

int main() {
    int i, total = 0;

    printf("By Bibek Kumar Singh\nEnter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++) { scanf("%d", &w[i]); total += w[i]; }

    printf("Enter required sum: ");
    scanf("%d", &sum);

    subset(0, 0, total);

    return 0;
}
