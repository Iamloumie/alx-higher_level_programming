#include "lists.h"
/**
 * check_cycle - checks if a singly list has cycle in it
 * @list: incoming list
 * Return: 0, always successful
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
