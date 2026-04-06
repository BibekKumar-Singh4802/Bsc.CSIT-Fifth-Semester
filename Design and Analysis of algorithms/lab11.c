/*
 * Program: 0/1 Knapsack Problem
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find maximum profit using dynamic programming
 */

#include <stdio.h>

int max(int a, int b) { return a > b ? a : b; }

int main() {
    int n, i, w;

    printf("By Bibek Kumar Singh\nEnter number of items: ");
    scanf("%d", &n);

    int p[n], wt[n];

    printf("Enter profits:\n");
    for(i = 0; i < n; i++) scanf("%d", &p[i]);

    printf("Enter weights:\n");
    for(i = 0; i < n; i++) scanf("%d", &wt[i]);

    printf("Enter capacity: ");
    scanf("%d", &w);

    int k[n+1][w+1];

    // DP table filling
    for(i = 0; i <= n; i++)
        for(int j = 0; j <= w; j++)
            if(i == 0 || j == 0) k[i][j] = 0;
            else if(wt[i-1] <= j) 
                k[i][j] = max(p[i-1] + k[i-1][j-wt[i-1]], k[i-1][j]);
            else k[i][j] = k[i-1][j];

    printf("Maximum Profit = %d\n", k[n][w]);

    return 0;
}
