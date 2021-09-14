#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int is_palindrome(listint_t **head)
{
    listint_t *tmp = NULL;
    int i = 0, j = 0, arr[999];

    if (!*head)
        return (1);
    tmp = *head;
    while (tmp)
    {
        arr[i] = tmp->n;
        tmp = tmp->next;
        i++;
    }
    i -= 1;
    for (; j <= i; j++, i--)
    {
        if (arr[j] != arr[i])
        {
            return (0);
        }
        else
            continue;
    }
    return (1);
}
