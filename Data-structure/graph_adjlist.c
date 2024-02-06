#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTEX_NUM 100

typedef struct node {
    int vertex;
    struct node *next;
} Node;

typedef struct {
    int vertexNum;
    Node *adjlist[MAX_VERTEX_NUM];
} Graph;

Graph* NewGraph(int vNum) {
    Graph *graph = (Graph*)malloc(sizeof(Graph));
    graph->vertexNum = vNum;
    for(int i=0; i<=vNum; i++)
        graph->adjlist[i] = NULL;

    return graph;
}

void AddEdge(Graph *g, int start, int end) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = end;
    newNode->next = g->adjlist[start];
    g->adjlist[start] = newNode;

    newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = start;
    newNode->next = g->adjlist[end];
    g->adjlist[end] = newNode;
}

void printGraph(Graph *graph) {
    Node *p;
    for(int i=1; i<=graph->vertexNum; i++) {
        p = graph->adjlist[i];
        printf("%d: ", i);
        while(p!=NULL) {
            printf("%d ", p->vertex);
            p = p->next;
        }
        printf("\n");
    }
}

int main() {
    Graph *g = NewGraph(6);

    AddEdge(g, 1, 2);
    AddEdge(g, 1, 3);
    AddEdge(g, 1, 4);
    AddEdge(g, 1, 6);
    AddEdge(g, 2, 3);
    AddEdge(g, 3, 5);
    AddEdge(g, 4, 6);
    AddEdge(g, 5, 6);

    printGraph(g);
}
