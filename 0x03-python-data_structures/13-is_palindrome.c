#include "lists.h"
/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Double pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *last = *head;
	listint_t *tmp = *head;
	size_t len = 0;
	size_t cont;

	if (!head && !*head)
		return (1);

	while (first != NULL)
	{
		first = first->next;
		len++;
	}
	while (len--)
	{
		cont = 0;
		last = *head;
		while (last != NULL)
		{
			if (cont == len)
				break;
			cont++;
			last = last->next;
		}
		if (last->n != last->n)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}
