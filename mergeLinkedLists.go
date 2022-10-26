package main

import (
	"fmt"
)

type Node struct {
	data int
	next *Node
}

func NewNode(val int, next *Node) *Node {
	var n Node
	n.data = val
	n.next = next

	return &n
}

func TraverseLL(head *Node) {
	temp := head
	for temp != nil {
		if temp.next != nil {
			fmt.Printf("%d -> ", temp.data)
		} else {
			fmt.Print(temp.data)
		}
		temp = temp.next
	}
}

func mergeTwoLL(head1, head2 *Node) *Node {
	temp1 := head1
	for temp1.next != nil {
		temp1 = temp1.next
	}

	temp1.next = head2
	return head1
}

func main() {
	head1 := NewNode(30, NewNode(40, NewNode(50, NewNode(60, nil))))
	head2 := NewNode(70, NewNode(80, NewNode(90, nil)))
	head := mergeTwoLL(head1, head2)
	TraverseLL(head)
}
