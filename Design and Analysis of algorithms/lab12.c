/*
 * Program: Huffman Coding
 * Course: Design and Analysis of Algorithms 
 * Author: Bibek Kumar Singh
 * Objective: Generate Huffman codes for text compression
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

struct node { char d; int f; struct node *l, *r; };

struct node* newN(char d, int f) {
    struct node* t = malloc(sizeof(struct node));
    t->d = d; t->f = f; t->l = t->r = NULL;
    return t;
}

void print(struct node* r, char c[], int top) {
    if(r->l) { c[top] = '0'; print(r->l, c, top+1); }
    if(r->r) { c[top] = '1'; print(r->r, c, top+1); }
    if(!r->l && !r->r) { c[top] = '\0'; printf("%c : %s\n", r->d, c); }
}

int main() {
    char text[1000]; int freq[256] = {0}, i = 0;

    printf("By Bibek Kumar Singh\nEnter text: ");
    scanf("%s", text);

    while(text[i]) freq[text[i++]]++;

    struct node* arr[MAX]; int n = 0;
    for(i = 0; i < 256; i++) if(freq[i]) arr[n++] = newN(i, freq[i]);

    while(n > 1) {
        int m1 = 0, m2 = 1;
        if(arr[m1]->f > arr[m2]->f) { int t = m1; m1 = m2; m2 = t; }
        for(i = 2; i < n; i++) {
            if(arr[i]->f < arr[m1]->f) { m2 = m1; m1 = i; }
            else if(arr[i]->f < arr[m2]->f) m2 = i;
        }
        struct node* t = newN('$', arr[m1]->f + arr[m2]->f);
        t->l = arr[m1]; t->r = arr[m2];
        if(m1 > m2) { int x = m1; m1 = m2; m2 = x; }
        for(i = m2+1; i < n; i++) arr[i-1] = arr[i]; n--;
        for(i = m1+1; i < n; i++) arr[i-1] = arr[i]; n--;
        arr[n++] = t;
    }

    char code[100];
    printf("Huffman Codes:\n");
    print(arr[0], code, 0);

    return 0;
}
