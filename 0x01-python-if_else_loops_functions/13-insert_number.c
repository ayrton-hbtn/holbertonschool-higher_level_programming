#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - inserts a node into a sorted linked list
  * @head: pointer to first node of list
  * @number: new number to insert
  * Return: address of new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *tmp = NULL, *prev = NULL;

	if (!head)
		return (NULL);
	tmp = *head;
	while (tmp)
	{
		if (number > tmp->n)
		{
			prev = tmp;
			tmp = tmp->next;
		}
		else
			break;
	}
	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = number;
		new->next = tmp;
	}
	if (prev)
		prev->next = new;
	return (new);
}
