#include "lists.h"

/**
* reversed_listint- a function that reverses a linked list
 * @head: address of the head node
 * Return: address of the head node of the reversed list
 */

listint_t *reversed_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - a function that checks if a given list is a palindrome
 * @head: adress of the head node
 * Return: 0 if the list is not a palindrome, otherwise 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *holder, *rev, *mid;
	size_t size = 0;
	size_t i;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	holder = *head;

	while (holder)
	{
		size++;
		holder = holder->next;
	}

	holder = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		holder = holder->next;
	if ((size % 2) == 0 && holder->n != holder->next->n)
		return (0);

	holder = holder->next->next;
	rev = reversed_listint(&holder);
	mid =  rev;

	holder = *head;

	while (rev)
	{
	if (holder->n != rev->n)
		return (0);
	holder = holder->next;
	rev = rev->next;
	}
	reversed_listint(&mid);
	return (i);

}
