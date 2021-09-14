#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int isPalindromeUtil(listint_t **left, listint_t *right)
{
    int isp, isp1;

    /* stop recursion when right becomes NULL */
    if (right == NULL)
        return (1);
 
    /* If sub-list is not palindrome then no need to
    check for current left and right, return false */
    if (isPalindromeUtil(left, right->next))
        isp = 1;
    else
        isp = 0;
    if (!isp)
        return (0);
 
    /* Check values at current left and right */
    if (right->n == (*left)->n)
        isp1 = 1;
    else
        isp1 = 0;
 
    /* Move left to next node */
    *left = (*left)->next;
 
    return (isp1);
}
 
// A wrapper over isPalindromeUtil()
int is_palindrome(listint_t **head)
{
    int check;

    check = isPalindromeUtil(head, *head);
    return (check);
}
