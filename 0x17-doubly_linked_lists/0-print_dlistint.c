#include "lists.h"
#include <stddef.h>
#include <stdio.h>
/**
*/

size_t print_dlistint(const dlistint_t *h)
{
    size_t count;

    while (h != NULL)
    {
        printf("%u ", h->n);
        count++;
        h = h->next;
    }
    return (count);
}