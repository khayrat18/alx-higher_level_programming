#include "lists.h"
/**
 * insert_node - function that inserts number in a list
 * @head: pointer to head node
 * @number: number to be inserted
 * Return: return new node, otherwise 0
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;

	new_node->next = (*head);

	(*head) = new_node;

	return (new_node);
}
