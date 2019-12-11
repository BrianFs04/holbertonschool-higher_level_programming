#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list's head
 * @number: number we get
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *tmp = *head;
	listint_t *tmp2;

	if (node == NULL)
		return (NULL);

	while (tmp->next != NULL)
	{
		if (tmp->n > number)
		{
			tmp2->next = node;
			node->n = number;
			node->next = tmp;
			return (node);
		}
		tmp2 = tmp;
		tmp = tmp->next;
	}
	return (NULL);
}
