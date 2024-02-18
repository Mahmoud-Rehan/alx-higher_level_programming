#include "lists.h"


/**
 * is_palindrome - checks if a linked list is a palindrome.
 * @head: pointer to the linked list
 * Return: 1 if successand  0 if not.
 */


int is_palindrome(listint_t **head)
{
	listint_t *first = *head, listint_t *second = *head, listint_t *tmp = *head;
	listint_t *second_head = NULL;


	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		first = first->next->next;
		if (first == NULL)
		{
			second_head = second->next;
			break;
		}
		if (first->next == NULL)
		{
			second_head = second->next->next;
			break;
		}
		second = second->next;
	}

	reverse(&second_head);

	while (tmp != NULL && second_head != NULL)
	{
		if (tmp->n == second_head->n)
		{
			second_head = second_head->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (second_head == NULL)
		return (1);
	else
		return (0);
}


/**
 * reverse - reverse a linked list.
 * @head: pointer to the linked list.
 */


void reverse(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
