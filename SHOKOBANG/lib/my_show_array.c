/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-myls-alexis.seymour
** File description:
** my_show_array.c
*/
#include "../include/my.h"

int my_show_array(char **tab)
{
    int i = 0;

    while (tab[i] != NULL) {
        write(1, tab[i], my_strlen(tab[i]));
        my_putchar('\n');
        i++;
    }
}
