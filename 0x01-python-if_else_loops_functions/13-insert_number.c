#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: The head of the list.
 * @number: The inserted number.
 * Return: The list or NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = (listint_t *)malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (head == NULL || number < head->n)
	{
		new->next = head;
		head = new;
	}
	else
	{
		current = head;
		prev = NULL;

		while (current != NULL && number > current->n)
		{
			prev = current;
			current = current->next;
		}

		prev->next = new;
		new->next = current;
	}

	return (&new);
}
