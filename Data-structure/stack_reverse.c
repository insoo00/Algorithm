#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100

typedef char element;
typedef struct {
    element data[MAX_STACK_SIZE];
    int top;
} StackType;

void init_stack(StackType *s) {
    s->top = -1;
}

int is_empty(StackType *s) {
    return (s->top == -1);
}

int is_full(StackType *s) {
    return (s->top == (MAX_STACK_SIZE -1));
}

void push(StackType *s, element item) {
    if(is_full(s)) {
        fprintf(stderr, "stack is full\n");
        return ;
    }
    else
        s->data[++(s->top)] = item;
}

element pop(StackType *s) {
    if(is_empty(s)) {
        fprintf(stderr, "stack is empty\n");
        exit(1);
    }
    else
        return s->data[(s->top)--];
}

element peek(StackType *s) {
    if(is_empty(s)) {
        fprintf(stderr, "stack is empty\n");
        exit(1);
    }
    else
        return s->data[(s->top)];
}

void reverse(char a[], char b[]) {
   int i = 0, j = 0;
    StackType s;
    init_stack(&s);
    
    while(a[i] != '\0') 
        push(&s, a[i++]);
    
    while(!is_empty(&s)) 
        b[j++] = pop(&s);

    b[j] = '\0';
}

int main() {
    char str[100];
    char rev[100];

    while(1) {
        printf("Enter the string: ");
        scanf("%s", str);
        reverse(str, rev);
        printf("Original: %s\t Reverse: %s\n", str, rev);
    }
}