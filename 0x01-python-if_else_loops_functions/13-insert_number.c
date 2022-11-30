#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = (listint_t*)malloc(sizeof(listint_t));

	new_node -> n = number;
	new_node -> next = NULL;
	if (temp -> next == NULL)
		temp -> next = new_node;
	else
	{
		while(temp -> next != NULL)
		{
			if (temp -> n < new_node -> n && temp -> next -> n > new_node -> n)
			{
				new_node -> next = temp -> next;
				temp -> next = new_node;
				return new_node;
			}
			temp = temp -> next;
		}
		temp -> next = new_node;
		new_node -> next = NULL;
	}
	return new_node;
}
