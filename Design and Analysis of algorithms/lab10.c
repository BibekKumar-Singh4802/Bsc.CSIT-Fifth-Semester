/*
 * Program: Job Sequencing with Deadline
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Sequence jobs to maximize profit using deadlines
 */

#include <stdio.h>

int main() {
    int n, i, j, maxd = 0;

    printf("By Bibek Kumar Singh\nEnter number of jobs: ");
    scanf("%d", &n);

    int p[n], d[n], slot[n];

    printf("Enter profits:\n");
    for(i = 0; i < n; i++) scanf("%d", &p[i]);

    printf("Enter deadlines:\n");
    for(i = 0; i < n; i++) { scanf("%d", &d[i]); if(d[i] > maxd) maxd = d[i]; }

    for(i = 0; i < maxd; i++) slot[i] = -1;

    // Sort jobs by profit (descending)
    for(i = 0; i < n; i++)
        for(j = i+1; j < n; j++)
            if(p[i] < p[j]) {
                int t = p[i]; p[i] = p[j]; p[j] = t;
                t = d[i]; d[i] = d[j]; d[j] = t;
            }

    int profit = 0;
    for(i = 0; i < n; i++)
        for(j = d[i]-1; j >= 0; j--)
            if(slot[j] == -1) { slot[j] = i; profit += p[i]; break; }

    printf("Job sequence:\n");
    for(i = 0; i < maxd; i++) if(slot[i] != -1) printf("J%d ", slot[i]+1);

    printf("\nTotal Profit = %d\n", profit);

    return 0;
}
