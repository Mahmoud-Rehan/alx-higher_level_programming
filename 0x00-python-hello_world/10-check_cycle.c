#include "lists.h"

/**
 * check_cycle - Checks if a singly
 * linked list has a cycle.
 *
 * @list: The checked linked list.
 * Return: 1 (success) or 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}
