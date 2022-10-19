#include<iostream>
#include<stdlib.h>
using namespace std;

struct node
{
    int data;
    struct node *next;
    struct node *prev;
};

void print(struct node *head)
{
    struct node *ptr = head;
    while (ptr != NULL)
    {
        cout<<ptr->data<<"->";
        ptr = ptr->next;
    }
    cout<<"NULL"<<endl;    
}

// IT CAN BE USED TO INSERT NODE AT AN EMPTY LIST ONLY
struct node *insert_at_empty(struct node *&head, int data)
{
    struct node *temp = new struct node();
    temp->next = NULL;
    temp->prev = NULL;
    temp->data = data;

    head = temp;
    return head;
    
}

// INSERT AT THE BEGINNING
void insert_begin(struct node *&head, int data)
{
    struct node *ptr = new struct node();
    ptr->data = data;
    ptr->prev = NULL;
    ptr->next = head;

    head = ptr;
}

// INSERT AT THE END
void insert_end(struct node *&head, int data)
{
    struct node *ptr = new struct node(), *trav = head;
    while(trav->next != NULL)
    {
        trav = trav->next;
    }
    ptr->data = data;
    trav->next = ptr;
    ptr->prev = trav;
}

int main()
{
    struct node *head = NULL;

    cout<<"Enter the first value: ";
    int v;
    cin>>v;
    head = insert_at_empty(head, v);
    cout<<"After inserting in an empty list"<<endl;
    print(head);

    cout<<"Enter the value: ";
    int c;
    cin>>c;
    insert_begin(head, c);
    cout<<"After inserting at the beginning"<<endl;
    print(head);

    cout<<"Enter the values: ";
    int m;
    cin>>m;
    insert_end(head, m);
    cout<<"After inserting at the end"<<endl;
    print(head);

    return 0;
}