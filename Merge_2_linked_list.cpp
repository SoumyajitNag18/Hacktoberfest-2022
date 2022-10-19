// Merging of two differnet Linked List
#include<iostream>
using namespace std;

struct node
{
    int data;
    struct node *next;
};

void print(struct node *head)
{
    struct node *ptr = head;
    while(ptr != NULL)
    {
        cout<<ptr->data<<"->";
        ptr = ptr->next;
    }
    cout<<"NULL"<<endl;
}

struct node *insert_head(struct node *head, int data)
{
    struct node *ptr = new struct node();
    ptr->data = data;
    ptr->next = NULL;
    head = ptr;
    return head;
}

void insert_end(struct node *head, int data)
{
    struct node *ptr = new struct node(), *temp;
    temp = head;
    ptr->data = data;
    ptr->next = NULL;

    while(temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = ptr;
}

int length(struct node *head)
{
    int c = 0;
    struct node *ptr = head;
    while(ptr != NULL)
    {
        c++;
        ptr = ptr->next;
    }
    return c;
}

void intersect(struct node *head1, struct node *head2, int pos)
{
    struct node *temp1 = head1, *temp2 = head2;
    pos--;
    while(pos--)
        temp1 = temp1->next;
    
    while(temp2->next != NULL)
        temp2 = temp2->next;
    
    temp2->next = temp1;
}

int main()
{
    struct node *head1 = NULL, *head2 = NULL;
    head1 = insert_head(head1, 23);
    insert_end(head1, 11);
    insert_end(head1, 50);
    insert_end(head1, 25);

    head2 = insert_head(head2, 20);
    insert_end(head2, 70);
    print(head1);
    print(head2);

    cout<<"After merging of two linked lists"<<endl;
    intersect(head1, head2, 1);
    print(head2);

    return 0;
}