#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * head: head reference
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head){
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;
	bool res = true;
	if (*head != NULL && *head->next != NULL) {
		while (fast_ptr != NULL && fast_ptr->next != NULL) {
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL) {
			midnode = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);
		reverse(&second_half);
		if (midnode != NULL) {
			prev_of_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow_ptr->next = second_half;
	}
	return res;
}

/**
 * reverse - reverses a linked list
 * head_ref: head reference
 * Return: void
 */
void reverse(listint_t** head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next;

	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

/**
 * compareLists - checks if two halves are equal
 * head1: head of first half
 * head2: head of second half
 * Return: 0 or 1
 */
bool compareLists(listint_t* head1, listint_t* head2)
{
	listint_t* temp1 = head1;
	listint_t* temp2 = head2;

	while (temp1 && temp2) {
		if (temp1->data == temp2->data) {
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return 0;
	}
	if (temp1 == NULL && temp2 == NULL)
		return 1;
	return 0;
}
