/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-bsmyls-alexis.seymour
** File description:
** my_len_array.c
*/
#include <stdio.h>

int my_len_array(char **tab)
{
    int i = 0;

    while (tab[i] != NULL) {
        i++;
    }
    return i - 1;
}
