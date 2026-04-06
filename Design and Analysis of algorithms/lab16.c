/*
 * Program: Prim's Algorithm
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find minimum spanning tree of a graph
 */

#include <stdio.h>
#define INF 9999

int main() {
    int n, i, j, k, u, v, min, total = 0;

    printf("By Bibek Kumar Singh\nEnter number of vertices: ");
    scanf("%d", &n);

    int g[n][n], vis[n], cost[n][n];
    printf("Enter adjacency matrix:\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++) scanf("%d", &g[i][j]);

    for(i = 0; i < n; i++) { vis[i] = 0; for(j = 0; j < n; j++) cost[i][j] = g[i][j]; }
    vis[0] = 1;

    for(k = 0; k < n-1; k++) {
        min = INF;
        for(i = 0; i < n; i++) {
            if(vis[i]) {
                for(j = 0; j < n; j++) {
                    if(!vis[j] && cost[i][j] < min) {
                        min = cost[i][j];
                        u = i; v = j;
                    }
                }
            }
        }
        printf("%d - %d : %d\n", u, v, min);
        total += min;
        vis[v] = 1;
    }

    printf("Total Cost = %d\n", total);

    return 0;
}
