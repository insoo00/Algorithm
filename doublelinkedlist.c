#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct DListNode {
  element data;
  struct DListNode *rlink;
  struct DListNode *llink;
} DListNode;

DListNode *dinsert(DListNode *head, DListNode *pre, element value) {
  DListNode *new = (DListNode *)malloc(sizeof(DListNode));
  new->data = value;

  if (head == NULL) {
    head = new;
    new->llink = NULL;
    new->rlink = NULL;
  } else if (pre == NULL) {
    new->rlink = head;
    head = new;
    new->llink = NULL;
    new->rlink->llink = new;
  } else {
    new->rlink = pre->rlink;
    pre->rlink = new;
    new->llink = pre;
    if (new->rlink != NULL)
      new->rlink->llink = new;
  }
  return head;
}

DListNode *ddelete(DListNode *head, DListNode *removed) {
  if (head == NULL) {
    printf("ddelete() error\n");
  } else if (head == removed) {
    head = removed->rlink;
    if (removed->rlink != NULL)
      removed->rlink->llink = NULL;
    free(removed);
  } else {
    removed->llink->rlink = removed->rlink;
    if (removed->rlink != NULL)
      removed->rlink->llink = removed->llink;
    free(removed);
  }
  return head;
}

void print_dlist(DListNode *head) {
  DListNode *p;

  for (p = head; p != NULL; p = p->rlink)
    printf("<-| |%d| |->", p->data);

  printf("\n");
}

int main() {
  DListNode *head = NULL;
  DListNode *pre = NULL;
  DListNode *removed = NULL;

  for (int i = 0; i < 5; i++) {
    head = dinsert(head, NULL, i);
    print_dlist(head);
  }
  pre = head->rlink->rlink->llink;
  head = dinsert(head, pre, 6);
  print_dlist(head);

  pre = head;
  while (pre->rlink != NULL)
    pre = pre->rlink;
  head = dinsert(head, pre, 7);
  print_dlist(head);

  pre = pre->rlink;
  printf("\n");

  while (pre != NULL) {
    printf("<-| |%d| |->", pre->data);
    pre = pre->llink;
  }

  head = ddelete(head, head); 
  print_dlist(head);

  head = ddelete(head, head->rlink); 
  print_dlist(head);

  removed = head;
  while (removed->rlink != NULL) 
    removed = removed->rlink;
  pre = removed->llink;          
  head = ddelete(head, removed); 
  print_dlist(head);

  printf("\n");
  while (pre != NULL) { 
    printf("<-| |%d| |->", pre->data);
    pre = pre->llink;
  }
  printf("\n");
  
}