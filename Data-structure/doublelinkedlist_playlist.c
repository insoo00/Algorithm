#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <termio.h> //To use getch() instead of <conio.h> in Linux

int getch(void) {
    int ch;
    struct termios buf;
    struct termios save;

    tcgetattr(0, &save);
    buf = save;

    buf.c_lflag &=  ~(ICANON|ECHO);
    buf.c_cc[VMIN] = 1;
    buf.c_cc[VTIME] = 0;

    tcsetattr(0, TCSAFLUSH, &buf);
    ch = getchar();
    tcsetattr(0, TCSAFLUSH, &save);

    return ch;
}

typedef char element[100];
typedef struct DListNode {
    element data;
    struct DListNode *llink;
    struct DListNode *rlink;
} DListNode;

DListNode* current;

DListNode* dinsert(DListNode *head, DListNode *pre, element value) {
    DListNode *new = (DListNode*)malloc(sizeof(DListNode));
    strcpy(new->data, value);

    if(head == NULL) {
        head = new;
        new->llink = NULL;
        new->rlink = NULL;
    }else if(pre == NULL) {
        new->rlink = head;
        head = new;
        new->llink = NULL;
        new->rlink->llink = new;        
    }else {
        new->rlink = pre->rlink;
        pre->rlink = new;
        new->llink = pre;
        if(new->rlink != NULL)
            new->rlink->llink = new;
    }
    return head;
}

DListNode* ddelete(DListNode *head, DListNode *removed) {
    if(head == NULL)
        printf("empty list\n");
    else if(head == removed) {
        head = removed->rlink;
        if(removed->rlink != NULL)
            removed->rlink->llink = NULL;
        free(removed);
    }else {
        removed->llink->rlink = removed->rlink;
        if(removed->rlink != NULL)
            removed->rlink->llink = removed->llink;
        free(removed);
    }
    return head;
}

void print_dlist(DListNode *head) {
    DListNode *p;

    for(p = head; p!= NULL; p = p->rlink) {
        if(p==current)
            printf("<-| #%s# |->", p->data);
        else
            printf("<-| %s |->", p->data);
    }
    printf("\n");
}

int main() {
    DListNode *head = NULL;
    char filename[100];
    char ch;

    head = dinsert(head, NULL, "The Next Right Thing");
    head = dinsert(head, NULL, "Show Yoursellf");
    head = dinsert(head, NULL, "Into The Unknown");
    head = dinsert(head, NULL, "All Is Found");

    current = head;
    print_dlist(head);
    strcpy(filename, current->data);
    strcat(filename, ".wav");
    PlaySoundA(filename, NULL, SND_FILENAME | SND_ASYNC); //play "filename" song function
    do {
        printf("Enter the command(<, >, q): ");
        ch = getch();
        printf("\n\n\n");
        if(ch == '<') {
            if(current->llink != NULL) {
                current = current->llink;
                print_dlist(head);
                strcpy(filename, current->data);
                strcat(filename, ".wav");
                PlaySoundA(NULL, NULL, NULL);
                PlaySoundA(filename, NULL, SND_FILENAME | SND_ASYNC);
            } else {
                printf("First song\n");
            }
        }
        else if(ch == '>') {
            if(current->rlink != NULL) {
                current = current->rlink;
                print_dlist(head);
                strcpy(filename, current->data);
                strcat(filename, ".wav");
                PlaySoundA(NULL, NULL, NULL);
                PlaySoundA(filename, NULL, SND_FILENAME | SND_ASYNC);
            }
            else {
                printf("Last song\n");
            }
        }
    } while(ch != 'q');
}