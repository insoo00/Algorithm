#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define MAX_VERTEX_NUM 100

typedef struct {
    int vertexNum;
    int adjMatrix[MAX_VERTEX_NUM][MAX_VERTEX_NUM];
} Graph;

/* 
    int vertexNum;
    int **adjMatrix;
*/

Graph* NewGraph(int vNum) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->vertexNum = vNum;
    //Reset: graph->adjMatrix  
    memset(graph->adjMatrix, 0, sizeof(int)*MAX_VERTEX_NUM*MAX_VERTEX_NUM);

    return graph;
}

void AddEdge(Graph *graph, int start, int end) {
    graph->adjMatrix[start][end] = 1;
    graph->adjMatrix[end][start] = 1;
}

void printGraph(Graph *graph) {
    for(int i=1; i<=graph->vertexNum; i++) {
        for(int j=1; j<=graph->vertexNum; j++)
            printf("%d ", graph->adjMatrix[i][j]);

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
