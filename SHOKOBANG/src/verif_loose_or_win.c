/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-sokoban-alexis.seymour
** File description:
** verif_loose_or_win.c
*/

#include "../include/my.h"


int check_h(int argc, char **argv)
{
    if (argc == 2 && argv[1][0] == '-' && argv[1][1] == 'h' &&
    argv[1][2] == '\0') {
        my_printf("USAGE\n");
        my_printf("     ./my_sokoban map\n");
        my_printf("DESCRIPTION\n");
        my_printf("      map file representing the warehous map, ");
        my_printf("containing '#' for walls,\n");
        my_printf("          'P' for the player, 'X' for boxes ");
        my_printf("and 'O' for storage locations.\n");
        exit(0);
    }
}

static int check_win_next(char **map_tab, char **map_tab_init, int i)
{
    int j = 0;
    int wincheck = 1;

    while (map_tab[i][j] != '\0') {
        if (map_tab[i][j] == 'P' && map_tab_init[i][j] != 'C')
            wincheck = 0;
        j++;
    }
    return wincheck;
}

int check_win(char **map_tab, char **map_tab_init, char *str)
{
    int i = 0;
    int wincheck = 1;

    while (map_tab[i] != NULL) {
        wincheck = check_win_next(map_tab, map_tab_init, i);
        if (wincheck == 0)
            return 0;
        i++;
    }    
    endwin();
    if (strcmp("./map/Level_1", str) == 0) {
        in_game("./map/Level_2");
    }
    if (str == "./map/Level_2")
        in_game("./map/Level_3");
    if (str == "./map/Level_3")
        display_endwin();
    exit(0);
}

static int check_loose_next_next(char **map_tab, char **map_tab_init,
    int i, int j)
{
    if (map_tab_init[i + 1][j] == '#' && map_tab_init[i][j + 1] == '#' ||
    map_tab_init[i][j + 1] == '#' && map_tab_init[i - 1][j] == '#' ||
    map_tab_init[i - 1][j] == '#' && map_tab_init[i][j - 1] == '#' ||
    map_tab_init[i][j - 1] == '#' && map_tab_init[i + 1][j] == '#') {
        return 1;
    }
    return 0;
}

static int check_loose_next(char **map_tab, char **map_tab_init, int i)
{
    int j = 0;
    int wincheck = 1;

    while (map_tab[i][j] != '\0') {
        if (map_tab[i][j] == 'X') {
            wincheck = check_loose_next_next(map_tab, map_tab_init, i, j);
        }
        if (wincheck == 0)
            return 0;
        j++;
    }
    return wincheck;
}

int check_loose(char **map_tab, char **map_tab_init)
{
    int i = 0;
    int wincheck = 1;

    while (map_tab[i] != NULL) {
        wincheck = check_loose_next(map_tab, map_tab_init, i);
        if (wincheck == 0)
            return 0;
        i++;
    }
    endwin();
    my_show_array(map_tab);
    exit(1);
}
