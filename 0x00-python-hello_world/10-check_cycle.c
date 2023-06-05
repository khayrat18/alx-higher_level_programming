#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to struct
 * Return: return 1, otherwise zero
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *prev = list;

	if (list == NULL)
	{
		return (0);
	}

	while (current != NULL && current->next != NULL)
	{
		current = current->next;
		prev = prev->next;
		if (current == prev)
			return (1);
	}
	return (0);



}
