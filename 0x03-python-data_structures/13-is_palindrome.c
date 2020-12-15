#include "lists.h"
/**
 * is_palindrome -  function in C that checks if a singly
 * linked list is a palindrome.
 * @head: Head.
 * Return: 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *palindrome;
	int count = 0, counter = 0;
	int buffer[4096];

	palindrome = *head;

	if (!*head || (*head)->next == NULL)
		return (1);

	while (palindrome)
	{
		buffer[counter] = palindrome->n;
		counter++;
		palindrome = palindrome->next;
	}
	counter--;
	while (counter > count)
	{
		if (buffer[counter] != buffer[count])
			return (0);
		counter--, count++;
	}
	return (1);
}
