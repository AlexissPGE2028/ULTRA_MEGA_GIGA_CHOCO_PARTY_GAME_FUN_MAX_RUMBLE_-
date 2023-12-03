/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-sokoban-alexis.seymour
** File description:
** all_input.c
*/

#include "../include/my.h"

int input_rigth(char **map_tab, char **map_tab_init, int *posX, int *posY)
{
    if (map_tab[*posY][*posX + 1] == 'X' &&
    (map_tab[*posY][*posX + 2] == ' ' ||
    map_tab[*posY][*posX + 2] == 'O')) {
        map_tab[*posY][*posX + 1] = 'P';
        map_tab[*posY][*posX + 2] = 'X';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab[*posY][*posX] == 'X' || map_tab[*posY][*posX] == 'P')
            map_tab[*posY][*posX] = ' ';
    }
    if (map_tab[*posY][*posX + 1] == ' ' ||
    map_tab[*posY][*posX + 1] == 'C') {
        map_tab[*posY][*posX + 1] = 'P';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab_init[*posY][*posX] == 'P' ||
        map_tab_init[*posY][*posX] == 'X')
            map_tab[*posY][*posX] = ' ';
    }
}

int input_left(char **map_tab, char **map_tab_init, int *posX, int *posY)
{
    if (map_tab[*posY][*posX - 1] == 'X' &&
    (map_tab[*posY][*posX - 2] == ' ' ||
    map_tab[*posY][*posX - 2] == 'O')) {
        map_tab[*posY][*posX - 1] = 'P';
        map_tab[*posY][*posX - 2] = 'X';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab[*posY][*posX] == 'X' || map_tab[*posY][*posX] == 'P')
            map_tab[*posY][*posX] = ' ';
    }
    if (map_tab[*posY][*posX - 1] == ' ' || map_tab[*posY][*posX - 1] == 'C') {
        map_tab[*posY][*posX - 1] = 'P';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab_init[*posY][*posX] == 'P' ||
        map_tab_init[*posY][*posX] == 'X')
            map_tab[*posY][*posX] = ' ';
    }
}

int input_down(char **map_tab, char **map_tab_init, int *posX, int *posY)
{
    if (map_tab[*posY + 1][*posX] == 'X' &&
    (map_tab[*posY + 2][*posX] == ' ' ||
    map_tab[*posY + 2][*posX] == 'O')) {
        map_tab[*posY + 1][*posX] = 'P';
        map_tab[*posY + 2][*posX] = 'X';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab[*posY][*posX] == 'X' || map_tab[*posY][*posX] == 'P')
            map_tab[*posY][*posX] = ' ';
    }
    if (map_tab[*posY + 1][*posX] == ' ' || map_tab[*posY + 1][*posX] == 'C') {
        map_tab[*posY + 1][*posX] = 'P';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab_init[*posY][*posX] == 'P' ||
        map_tab_init[*posY][*posX] == 'X')
            map_tab[*posY][*posX] = ' ';
    }
}

int input_up(char **map_tab, char **map_tab_init, int *posX, int *posY)
{
    if (map_tab[*posY - 1][*posX] == 'X' &&
    (map_tab[*posY - 2][*posX] == ' ' ||
    map_tab[*posY - 2][*posX] == 'O')) {
        map_tab[*posY - 1][*posX] = 'P';
        map_tab[*posY - 2][*posX] = 'X';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab[*posY][*posX] == 'X' || map_tab[*posY][*posX] == 'P')
            map_tab[*posY][*posX] = ' ';
    }
    if (map_tab[*posY - 1][*posX] == ' ' || map_tab[*posY - 1][*posX] == 'C') {
        map_tab[*posY - 1][*posX] = 'P';
        map_tab[*posY][*posX] = map_tab_init[*posY][*posX];
        if (map_tab_init[*posY][*posX] == 'P' ||
        map_tab_init[*posY][*posX] == 'X')
            map_tab[*posY][*posX] = ' ';
    }
}
