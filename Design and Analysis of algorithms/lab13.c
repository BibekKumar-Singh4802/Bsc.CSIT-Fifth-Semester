/*
 * Program: Floyd Warshall Algorithm
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find shortest paths between all pairs of vertices
 */

#include <stdio.h>
#define INF 9999

int main() {
    int n, i, j, k;

    printf("By Bibek Kumar Singh\nEnter number of vertices: ");
    scanf("%d", &n);

    int d[n][n];
    printf("Enter adjacency matrix:\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++) scanf("%d", &d[i][j]);

    // Floyd Warshall
    for(k = 0; k < n; k++)
        for(i = 0; i < n; i++)
            for(j = 0; j < n; j++)
                if(d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];

    printf("Shortest path matrix:\n");
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) printf("%d ", d[i][j]);
        printf("\n");
    }

    return 0;
}
