/*
 * Program: N-Queen Problem using Backtracking
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Place N queens on a chessboard such that no two queens attack each other
 */

#include <stdio.h>
#include <stdlib.h>

int x[20], n;

int place(int k, int i) {
    for(int j = 1; j < k; j++)
        if(x[j] == i || abs(x[j] - i) == abs(j - k)) return 0;
    return 1;
}

void nqueen(int k) {
    for(int i = 1; i <= n; i++) {
        if(place(k, i)) {
            x[k] = i;
            if(k == n) {
                for(int j = 1; j <= n; j++) printf("%d ", x[j]);
                printf("\n");
            } else nqueen(k+1);
        }
    }
}

int main() {
    printf("By Bibek Kumar Singh\nEnter number of queens: ");
    scanf("%d", &n);

    nqueen(1);

    return 0;
}
