#include "lists.h"
/**
 * insert_node - Inserts a number into linked list.
 * @head: Head.
 * @number: number.
 * Return: Node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *nodemove = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL || nodemove->n >= number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}

	while (nodemove->next != NULL && nodemove->next->n < number)
	{
		nodemove = nodemove->next;
	}
	new->n = number;
	new->next = nodemove->next;
	nodemove->next = new;

	return (new);
}
