/*
 * Program: Dijkstra's Algorithm
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find shortest path from a single source
 */

#include <stdio.h>
#define INF 9999

int main() {
    int n, i, j, src;

    printf("By Bibek Kumar Singh\nEnter number of vertices: ");
    scanf("%d", &n);

    int g[n][n], dist[n], vis[n];
    printf("Enter adjacency matrix:\n");
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++) scanf("%d", &g[i][j]);

    printf("Enter source vertex: ");
    scanf("%d", &src);

    for(i = 0; i < n; i++) { dist[i] = INF; vis[i] = 0; }
    dist[src] = 0;

    for(i = 0; i < n-1; i++) {
        int u = -1;
        for(j = 0; j < n; j++)
            if(!vis[j] && (u == -1 || dist[j] < dist[u])) u = j;

        vis[u] = 1;
        for(j = 0; j < n; j++)
            if(!vis[j] && g[u][j] && dist[u] + g[u][j] < dist[j])
                dist[j] = dist[u] + g[u][j];
    }

    printf("Shortest distances:\n");
    for(i = 0; i < n; i++) printf("%d -> %d\n", i, dist[i]);

    return 0;
}
