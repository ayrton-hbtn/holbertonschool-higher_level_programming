#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool isPalindromeUtil(listint_t **left, listint_t *right)
{
    bool isp, isp1;

    /* stop recursion when right becomes NULL */
    if (right == NULL)
        return (true);
 
    /* If sub-list is not palindrome then no need to
    check for current left and right, return false */
    isp = isPalindromeUtil(left, right->next);
    if (isp == false)
        return (false);
 
    /* Check values at current left and right */
    isp1 = (right->n == (*left)->n);
 
    /* Move left to next node */
    *left = (*left)->next;
 
    return (isp1);
}
 
// A wrapper over isPalindromeUtil()
int is_palindrome(listint_t **head)
{
    int check;

    if (isPalindromeUtil(head, *head))
        check = 1;
    else
        check = 0;
    return (check);
}
