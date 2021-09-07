#include "lists.h"

/**
  * check_cycle - checks for a cycle in a linked list
  * @list: list
  * Return: 1 if cycle is found, 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	if (!list)
		return (0);

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
