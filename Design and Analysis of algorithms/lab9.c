/*
 * Program: Matrix Chain Multiplication
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Find optimal multiplication cost of given matrices
 */
#include <stdio.h>
#include <limits.h>

int main(){
    int n,i,l,j,k,q,count=0;

    printf("Bibek Kumar Singh\nEnter number of matrices: ");
    scanf("%d",&n);

    int p[n+1];
    int m[n+1][n+1];

    printf("Enter dimensions:\n");
    for(i=0;i<=n;i++) scanf("%d",&p[i]);

    for(i=1;i<=n;i++) m[i][i]=0;

    for(l=2;l<=n;l++){
        for(i=1;i<=n-l+1;i++){
            j=i+l-1;
            m[i][j]=INT_MAX;
            for(k=i;k<j;k++){
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j];
                count++;
                if(q<m[i][j]) m[i][j]=q;
            }
        }
    }

    printf("Minimum multiplication cost = %d\n",m[1][n]);
    printf("Total RAM operations = %d\n",count);
    return 0;
}