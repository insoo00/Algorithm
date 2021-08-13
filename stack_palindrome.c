#include <stdio.h>
#include <stdlib.h>

typedef char element; 
typedef struct StackNode {
    element data;
    struct StackNode *link;
} StackNode;
typedef struct {
    StackNode *top;
} LinkedStackType;

void init_stack(LinkedStackType *s) {
    s->top = NULL;
}

int is_empty(LinkedStackType *s) {
    return (s->top == NULL);
}

void push(LinkedStackType *s, element item) {
    StackNode *temp = (StackNode*)malloc(sizeof(StackNode));
    temp->data = item;
    temp->link = s->top;
    s->top = temp;
}

element pop(LinkedStackType *s) {
    if(is_empty(s))
        exit(1);
    else {
        StackNode *removed = (StackNode*)malloc(sizeof(StackNode));
        removed = s->top;
        element ret = removed->data;
        s->top = s->top->link;
        free(removed);
        return ret;
    }
}

element peek(LinkedStackType *s) {
    if(is_empty(s))
        exit(1);
    else 
        return s->top->data;
}

int checkPalindrome(char str[]) {
    int i = 0;
    LinkedStackType s;
    init_stack(&s);

    while(str[i] != '\0') 
        push(&s, str[i++]);
    
    i=0;
    // while(str[i] != '\0') {
    while(!is_empty(&s)) {
        if(str[i++] != pop(&s))
            return 0;
    }
    return 1;
}

int main() {
    char str[100];
    int ret;

    while(1) {
        printf("Enter the string: ");
        scanf("%s", str);

        ret = checkPalindrome(str);
        if(ret == 1)
            printf("It's palindrome\n");
        else
            printf("It's not palindrome\n");
    }
}



