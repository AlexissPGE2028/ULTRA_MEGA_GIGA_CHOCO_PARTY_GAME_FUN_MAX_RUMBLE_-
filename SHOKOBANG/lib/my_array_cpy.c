/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-sokoban-alexis.seymour
** File description:
** my_array_cpy.c
*/

#include "../include/my.h"

char **my_arraycpy(char **tab)
{
    int i = 0;
    char **tabcpy = malloc(sizeof(char *) * my_len_array(tab) + 1);

    while (tab[i] != NULL) {
        tabcpy[i] = malloc(sizeof(char) * my_strlen(tab[i]));
        my_strcpy(tabcpy[i], tab[i]);
        i++;
    }
    tabcpy[i] = NULL;
    return tabcpy;
}
