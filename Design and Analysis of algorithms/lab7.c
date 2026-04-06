*
 * Program: Heap Sort with Execution Time
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Sort numbers using Heap Sort and measure execution time
 */

#include <stdio.h>
#include <stdlib.h>
int parent[100];
int find(int i){
while(parent[i]!=i) i=parent[i];
return i;
}
void uni(int i,int j){
int a=find(i),b=find(j);
parent[a]=b;
}
int main(){
int n,e,i,j,u,v,w,min,total=0,count=0;
printf("By  Bibek Kumar Singh\nEnter vertices and edges: ");
scanf("%d %d",&n,&e);
int a[100][3];
printf("Enter edges (u v w):\n");
for(i=0;i<e;i++) scanf("%d %d %d",&a[i][0],&a[i][1],&a[i][2]);
for(i=0;i<n;i++) parent[i]=i;
while(count<n-1){
min=9999;
for(i=0;i<e;i++)
if(a[i][2]<min){
min=a[i][2];
u=a[i][0];v=a[i][1];w=a[i][2];
j=i;
}
a[j][2]=9999;
if(find(u)!=find(v)){
uni(u,v);
printf("%d - %d : %d\n",u,v,w);
total+=w;
count++;
}
}
printf("Total Cost = %d\n",total);
return 0;
}
