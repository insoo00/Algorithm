#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node {
    char name[20];
    int id;
    struct node *link;
} Node;

Node *head = NULL;

void print_list() {
    Node *p;
    p = head;

    while(p != NULL) {
        printf("(%s, %d) ", p->name, p->id);
        p = p->link;
    }
    printf("\n");
}

Node* search_list_by_name(char *name) {
    Node *p = head;
    while(p != NULL) {
        if(strcmp(p->name, name) == 0)
            return p;
        p = p->link;            
    }
    return NULL;
}

Node* search_list_by_id(int id) {
    Node *p = head;
    while(p != NULL) {
        if(p->id == id)
            return p;
        p = p->link;            
    }
    return NULL;
}

void insert(Node *pre, char *name, int id) {
    Node *new;
    new = (Node *)malloc(sizeof(Node));
    strcpy(new->name, name);
    new->id = id;
    new->link = NULL;

    if(pre == NULL) {
        new->link = head;
        head = new;
    }
    else {
        new->link = pre->link;
        pre->link = new;
    }
}

void delete(char *name, int id) {
    Node *pre;
    Node *del;

    if(head == NULL) {
        printf("Empty list\n");
        return ;
    }
    if(strcmp(head->name, name) == 0 && head->id == id) {
        del = head;
        head = del->link;
        free(del);
    }
    else {
        pre = head;
        while(pre->link != NULL) {
            if(strcmp(pre->link->name, name) == 0 && pre->link->id == id) {
                del = pre->link;
                pre->link = del->link;
                free(del);
                return ;   
            }
            pre = pre->link;
        }
        printf("No items\n");
        return ;
    }
}
int main() {
    Node *new;
    Node *pre;

    new = (Node *)malloc(sizeof(Node));
    strcpy(new->name, "SEO");
    new->id = 1000;
    new->link = NULL;
    head = new;

    new = (Node *)malloc(sizeof(Node));
    strcpy(new->name, "YUN");
    new->id = 2000;
    new->link = NULL;
    head->link = new;

    new = (Node *)malloc(sizeof(Node));
    strcpy(new->name, "KIM");
    new->id = 3000;
    new->link = NULL;
    head->link->link = new;

    print_list();

    new = search_list_by_name("YUN");
    if(new != NULL)
        printf("name: %s    id: %d\n", new->name, new->id);

    new = search_list_by_id(1000);
    if(new != NULL)
        printf("name: %s    id: %d\n", new->name, new->id);

    new = search_list_by_name("LEE");
    if(new != NULL)
        printf("name: %s    id: %d\n", new->name, new->id);

    new = search_list_by_id(3000);
    if(new != NULL)
        printf("name: %s    id: %d\n", new->name, new->id);

    insert(NULL, "LEE", 3000);
    pre = search_list_by_name("LEE");
    if(pre != NULL)
        insert(pre, "PARK", 4000);
    pre = search_list_by_id(2000);
    if(pre != NULL)
        insert(pre, "MOON", 5000);
    
    print_list();

    delete("LEE", 3000);
    delete("SEO", 1000);
    delete("KIM", 3000);

    print_list();

}
