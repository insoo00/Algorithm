#include <stdio.h>
#include <string.h>

#define MAX_IOT_LIST_SIZE 45

typedef struct {
    char name[20];
    int id;
} Namecard;

Namecard iot_list[MAX_IOT_LIST_SIZE];
int length;

Namecard make_Namecard(char name[], int id)
{
    Namecard newCard;

    strcpy(newCard.name, name);
    newCard.id = id;

    return newCard;
}

void print_list(char* key)
{
    int i;
    printf("%s: ", key);
    for (i = 0; i < length; i++)
        printf("( %s, %d) ", iot_list[i].name, iot_list[i].id);
    printf("\n");
}

int size()
{
    return length;
}

void init()
{
    length = 0;
    for (int i = 0; i < MAX_IOT_LIST_SIZE; i++) {
        iot_list[i].id = 0;
        strcpy(iot_list[i].name, " ");
    }
}

void insert(int pos, Namecard temp)
{
    int i;
    if (pos > length || pos < 0 || pos > MAX_IOT_LIST_SIZE) {
        printf("INSERT ERROR\n");
        return;
    }
    for (i = length; i > pos; i--) {
        iot_list[i].id = iot_list[i - 1].id;
        strcpy(iot_list[i].name, iot_list[i - 1].name);
    }
    iot_list[pos].id = temp.id;
    strcpy(iot_list[pos].name, temp.name);

    length++;
}

void replace(int pos, Namecard temp)
{
    if (pos > length || pos < 0 || pos > MAX_IOT_LIST_SIZE) {
        printf("REPLACE ERROR\n");
        return;
    }
    iot_list[pos].id = temp.id;
    strcpy(iot_list[pos].name, temp.name);
}

void delete (int pos)
{
    int i;
    if (pos > length || pos < 0 || pos > MAX_IOT_LIST_SIZE) {
        printf("DELETE ERROR\n");
        return;
    }
    for (i = pos; i < length; i++) {
        iot_list[i].id = iot_list[i + 1].id;
        strcpy(iot_list[i].name, iot_list[i + 1].name);
    }
    length--;
}

void sort_list(void)
{
    int i, j;
    Namecard A;
    for (i = 0; i < length; i++) {
        A = iot_list[i];
        for (j = i + 1; j < length; j++)
            if (A.id > iot_list[j].id) {
                A = iot_list[j];
                iot_list[j] = iot_list[i];
                iot_list[i] = A;
            }
    }
}

int find(Namecard src)
{
    int i;
    for (i = 0; i < length; i++) {
        if (iot_list[i].id == src.id && !strcmp(iot_list[i].name, src.name))
            return i;
    }
    return -1;
}
int main()
{
    init();
    print_list("Init");
    insert(0, make_Namecard("LEE", 20191524));
    insert(0, make_Namecard("KIM", 20191520));
    insert(1, make_Namecard("LIM", 20191507));
    insert(size(), make_Namecard("PARK", 20191546));
    insert(3, make_Namecard("AN", 20191528));
    insert(size(), make_Namecard("YOU", 20191513));
    insert(10, make_Namecard("GO", 20191518));
    print_list("Insert");

    replace(size() - 1, make_Namecard("GANG", 20191544));
    replace(4, make_Namecard("HEO", 20191539));
    replace(20, make_Namecard("SEONG", 20191530));
    print_list("Replace");

    delete (3);
    delete (size() - 1);
    delete (0);
    delete (30);
    print_list("Delete");

    sort_list();
    print_list("Sort");

    printf("%s is found at %d\n", "HEO", find(make_Namecard("HEO", 20191539)));
    printf("%s is found at %d\n", "OH", find(make_Namecard("OH", 20191545)));
}