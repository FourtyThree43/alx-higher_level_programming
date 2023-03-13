#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to a pointer to the first node of the list.
 *
 * Return: Pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;

    return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *middle, *second_half;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (palindrome);

    slow = *head;
    fast = *head;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev_slow->next = NULL;
    reverse_listint(&second_half);

    while (second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            palindrome = 0;
            break;
        }

        *head = (*head)->next;
        second_half = second_half->next;
    }

    reverse_listint(&second_half);

    if (middle != NULL)
    {
        prev_slow->next = middle;
        middle->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return (palindrome);
}
