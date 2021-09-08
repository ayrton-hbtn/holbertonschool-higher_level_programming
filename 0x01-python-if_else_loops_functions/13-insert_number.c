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
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	tmp = *head;
	if (!tmp || number <= tmp->n)
	{
		new->next = tmp;
		*head = new;
	}
	while (tmp->next && number > tmp->next->n)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	if (prev)
		prev->next = new;
	new->next = tmp;
	return (new);
}
