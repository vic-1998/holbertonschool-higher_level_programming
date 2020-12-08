#include "lists.h"
/**
 * check_cycle - function check list
 * @list: list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	while (temp1 != NULL && temp2 != NULL && temp2->next != NULL)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;
		if (temp1 == temp2)
		{
			return (1);
		}
	}
	return (0);

}
