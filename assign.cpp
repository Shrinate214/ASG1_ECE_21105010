/*                                                       ASSIGNMENT-01
To Create a doubly linked list with your family members as elements; include the following details as node values:
Name and Age                       \
 SUBMITTED BY:  AKSHAT SHRINATE
 SID         :  21105010
 BRNACH      :  ECE
*/
#include <iostream>
using namespace std;
class Node{                                                           //CREATING NODE CLASS
    public:
    string name;                                                      //Creating class objects
    int age;                                                          //Creating class objects
    Node*next;                                                        //A node pointer for next node
    Node*prev;                                                        //A node pointer for previous node
    Node(string name,int age){                                        //Calling The Constructor
        this->name=name;
        this->age=age;
        next=NULL;                                                    //initialising next as NULL
        prev=NULL;                                                    //initialising previous as NULL
    }
};                                                                    // Semicolon needed after class defintion
void append(Node* &head,string name,int age){                         //Function to insert data at ending of Linked List
                                                                      //Creating a node pointer and storing address of head in temp
    Node*temp=head;
    Node*new_node=new Node(name,age);                                 //Creating a new node and storing name and age in it
    if(temp==NULL){                                                   //Inserting node in empty list
        head=new_node;
    }
    else{                                                             //Inserting node in non empty list
        while(temp->next!=NULL){temp=temp->next;}
        temp->next=new_node;
        new_node->prev=temp;
    }
}
void insert_at_head(Node*&head,string name,int age){                  //Function to insert data at starting point of linked list
    Node*new_node=new Node(name,age);                                 //Creating a Node pointer and storing address of new node in that
    new_node->next=head;                                              //Inserting new node at head node
    head->prev=new_node;
    head=new_node;
}
void display_from_start(Node*head){                                  //Function to DISPLAY data from starting point of linked list
    Node*temp=head;
    while(temp!=NULL){cout<<"[Name:"<<temp->name<<" Age:"<<temp->age<<"]"<<"<==>";temp=temp->next;}
    cout<<endl;
}
void display_from_end(Node*head){                                    //Function to display data from end of Linked List
    Node*temp=head;
    while(temp->next!=NULL){temp=temp->next;}
    while(temp!=NULL){cout<<"[Name:"<<temp->name<<" Age:"<<temp->age<<"]"<<"<==>";temp=temp->prev;}
    cout<<endl;
}
void delete_ind(Node*&head,int i){                                   //function to delete any index (0,n-1) and excluding last element
    if(i==0){
        Node*temp=head;
        head=temp->next;
        head->prev=NULL;
        delete temp;
    }
    else{
        Node*temp=head;
        for(int j=0;j<i;j++){temp=temp->next;}
        temp->prev->next=temp->next;
        temp->next->prev=temp->prev;
        delete temp;
    }
}
void pop(Node*&head){                                                 //Function to POP last element
    Node*temp=head;
    while(temp->next!=NULL){temp=temp->next;}
    temp->prev->next=NULL;
    delete temp;
}
int main(){
    Node*head=NULL;                                                   //Initialisation of a double link list
	int no_of_family_members;
	cout<<"Enter Number Of Family Members:";cin>>no_of_family_members;//Taking number of family members as INPUT
	for(int j=1;j<=no_of_family_members;j++){                    //loop created to add family members details in doubly linked list
		string name;
		int age;
		cout<<"Enter Family Member "<<j<<" Name:";
		cin>>name;
		cout<<"Enter Family Member "<<j<<" Age:";
		cin>>age;
		append(head,name,age);                              //to append data name and age in doubly linked list
	}
cout<<"-------------------------------------------------------------"<<endl;
cout<<endl;                                                        // to leave a line between input and output
    cout<<"Doubly Linked list create using my family members is:"<<endl;
    display_from_start(head);
}
/********************************************************************************************************
                                            ***ASSIGNMENT OVER***
*********************************************************************************************************/
