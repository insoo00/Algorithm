#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EXPR_SIZE 100

typedef int element;
typedef struct {
    element data[EXPR_SIZE];
    int top;
} StackType;

void init_stack(StackType *s) {
    s->top = -1;
}

int is_full(StackType *s) {
    return (s->top == (EXPR_SIZE -1));
}

int is_empty(StackType *s) {
    return (s->top == -1);
}

void push(StackType *s, element item) {
    if(is_full(s)) {
        fprintf(stderr, "stack full error\n");
        return ;
    }
    else
        s->data[++(s->top)] = item;
}

element pop(StackType *s) {
    if(is_empty(s)) {
        fprintf(stderr, "stack empty error\n");
        exit(1);
    }
    else
        return s->data[(s->top)--];
}

element peek(StackType *s) {
    if(is_empty(s)) {
        fprintf(stderr, "stack empty error\n");
        exit(1);
    }
    else
        return s->data[s->top];
}

int check_matching(const char *in) {
    StackType s;
    char ch, open_ch;
    int i, n = strlen(in);
    init_stack(&s);

    for(i=0; i<n; i++) {
        ch = in[i];
        switch(ch) {
            case '(':
            case '{':
            case '[':
                push(&s, ch);
                break;
            case ')':
            case '}':
            case ']':
                if(is_empty(&s))
                    return 0;
                else {
                    open_ch = pop(&s);
                    if((open_ch == '(' && ch != ')') || (open_ch == '{' && ch != '}') || (open_ch == '[' && ch != ']'))
                        return 0;
                }
                break;
        }
    }
    if(!is_empty(&s))
        return 0;

    return 1;
}

int prec(char op) {
    switch(op) {
        case '(':
        case ')':
            return 0;
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;                        
    }
    return -1;
}

void infix_to_postfix(char exp[], char postfix[]) {
    int i = 0;
    char ch, top_op;
    int pos = 0;
    int len = strlen(exp);
    StackType s;

    init_stack(&s);
    for(i=0; i<len; i++) {
        ch = exp[i];
        switch (ch) {
            case '+':
            case '-':
            case '*':
            case '/':
                while (!is_empty(&s) && (prec(ch) <= prec(peek(&s)))) 
                    postfix[pos++] = pop(&s);
                push(&s, ch);
                break;
            case '(':
                push(&s, ch);
                break;
            case ')':
                top_op = pop(&s);
                while(top_op != '(') {
                    postfix[pos++] = top_op;                    
                    top_op = pop(&s);
                }
                break;
            default:
                do {
                    postfix[pos++] = ch;
                    ch = exp[++i];
                } while (ch >= '0' && ch <= '9');
                postfix[pos++] = ' ';
                i--;
                break;
        }
    }
    while (!is_empty(&s))
        postfix[pos++] = pop(&s);
    postfix[pos] = '\0';
}

int eval(char exp[]) {
    int op1, op2, value, pos, i = 0;
    int len = strlen(exp);
    char ch;
    char temp[100];
    StackType s;
    init_stack(&s);

    for(i=0; i<len; i++) {
        ch = exp[i];
        if(ch == ' ')
            continue;
        else if(ch != '+' && ch != '-' && ch != '*' && ch != '/') {
            for(pos=0; exp[i] != ' ';)
                temp[pos++] = exp[i++];
            temp[pos] = '\0';
            value = atoi(temp);
            push(&s, value);
        } else {
            op2 = pop(&s);
            op1 = pop(&s);
            switch (ch) {
                case '+':
                    push(&s, op1 + op2);
                    break;
                case '-':
                    push(&s, op1 - op2);
                    break;
                case '*':
                    push(&s, op1 * op2);
                    break;    
                case '/':
                    push(&s, op1 / op2);
                    break;
            }
        }
    }
    return pop(&s);
}

int main() {
    int result;
    char input[EXPR_SIZE];
    char postfix[EXPR_SIZE];

    while(1) {
        printf("Enter a infix to calculate: ");
        fgets(input, EXPR_SIZE-1, stdin);
        input[strlen(input) - 1] = '\0';

        if(check_matching(input) != 1) {
            printf("bracket error\n");
            continue;
        }
        
        infix_to_postfix(input, postfix);
        printf("postfix: %s\n", postfix);

        result = eval(postfix);
        printf("result => %d\n", result);
    }
}
