#include "lists.h"

/**
 * free_dlistint - frees a doubly linked list
 * @head: pointer to head node
 */


void free_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	dlistint_t *next;

	while (current != NULL)
	{
		next = current->next;
		free(current);
		current = next;
	}


}
