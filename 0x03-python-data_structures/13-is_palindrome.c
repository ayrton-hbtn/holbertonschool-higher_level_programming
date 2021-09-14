#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * isPalindromeUtil - asdasd
 * @left: asdasd
 * @right: asdasd
 * Return: 1 if palindrome, 0 otherwise
 */
int isPalindromeUtil(listint_t **left, listint_t *right)
{
	int isp, isp1;

	if (right == NULL)
		return (1);

	if (isPalindromeUtil(left, right->next))
		isp = 1;
	else
		isp = 0;
	if (!isp)
		return (0);

	if (right->n == (*left)->n)
		isp1 = 1;
	else
		isp1 = 0;

	*left = (*left)->next;

	return (isp1);
}

/**
 * is_palindrome - asdasd
 * @head: asdasd
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int check;

	check = isPalindromeUtil(head, *head);
	return (check);
}
