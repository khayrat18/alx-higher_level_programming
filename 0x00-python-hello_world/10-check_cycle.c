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

	while (list == current->next)
	{
		current = current->next;
		prev = prev->next->next;
		if (current == prev)
			return (0);
	}
	return (0);



}
