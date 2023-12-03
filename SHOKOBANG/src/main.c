/*
** EPITECH PROJECT, 2023
** B-PSU-100-TLS-1-1-sokoban-alexis.seymour
** File description:
** main.c
*/

#include "../include/my.h"
#include <stdio.h>
#include <stdlib.h>

char **make_tab_of_map(char *argv)
{
    int i = 0;
    char **tab_of_map = NULL;
    char *str = malloc(sizeof(char) * 1000000);
    int fd = open(argv, O_RDONLY);
    int char_read = read(fd, str, 10999);

    if (fd == -1)
        exit(84);
    str[char_read] = '\0';
    tab_of_map = my_str_to_word_array(str);
    return tab_of_map;
}

int my_show_map(char **tab, int row, int col, TAILLE_MAP_T *t_map, char *argv)
{
    int i = 0;
    char *str = "please enlarge the window";

    if (row < t_map->length || col < t_map->width) {
        mvprintw(row / 2, ((col - my_strlen(str)) / 2), "%s", argv);
        return 0;
    }
    mvaddstr((row - my_len_array(tab)) / 2 + i - 1, (col - strlen(tab[0])) / 2, argv + 6);
    while (tab[i] != NULL) {
        mvaddstr((row - my_len_array(tab)) / 2 + i, (col - strlen(tab[0])) / 2, tab[i]);
        i++;
    }
}

static int get_position_next(char **map_tab, int *posX, int *posY, int i)
{
    int j = 0;

    while (map_tab[i][j] != '\0') {
        if (map_tab[i][j] == 'P') {
            *posX = j;
            *posY = i;
        }
        j++;
    }
}

static int get_position(char **map_tab, int *posX, int *posY)
{
    int i = 0;

    while (map_tab[i] != NULL) {
        get_position_next(map_tab, posX, posY, i);
        i++;
    }
}

char **reset_map(char **map_tab, char **map_tab_init, int input)
{
    char **new_map;

    if (input == 32) {
        new_map = my_arraycpy(map_tab_init);
        return new_map;
    }
    return map_tab;
}

static char **make_mouvement(char **map_tab, int input, char **map_tab_init)
{
    int posX = 0;
    int posY = 0;

    get_position(map_tab, &posX, &posY);
    if (input == 261) {
        input_rigth(map_tab, map_tab_init, &posX, &posY);
    }
    if (input == 260) {
        input_left(map_tab, map_tab_init, &posX, &posY);
    }
    if (input == 258) {
        input_down(map_tab, map_tab_init, &posX, &posY);
    }
    if (input == 259){
        input_up(map_tab, map_tab_init, &posX, &posY);
    }
    map_tab = reset_map(map_tab, map_tab_init, input);
}

static void get_taille_map(TAILLE_MAP_T *t_map, char **map_tab)
{
    int i = 0;
    int len1 = 0;
    int len2 = 0;

    while (map_tab[i] != NULL) {
        len1 = my_strlen(map_tab[i]);
        if (len2 > len1) {
            t_map->width = len2 + 1;
        }
        i++;
    }
    t_map->length = i;
}

static int inside_loop(char **map_tab, char **map_tab_init, char *argv)
{
    WINDOW *boite;
    int row = 0;
    int col = 0;
    int input = 0;
    TAILLE_MAP_T t_map;

    get_taille_map(&t_map, map_tab);
    initscr();
    getmaxyx(stdscr, row, col);
    while (1) {
        getmaxyx(stdscr, row, col);
        erase();
        refresh();
        map_tab = make_mouvement(map_tab, input, map_tab_init);
        my_show_map(map_tab, row, col, &t_map, argv);
        check_win(map_tab, map_tab_init, argv);
        input = getch();
    }
    endwin();
}

int in_game(char *argv)
{
    char **map_tab = make_tab_of_map(argv);
    char **map_tab_init = my_arraycpy(map_tab);

    inside_loop(map_tab, map_tab_init, argv);
    return 0;
}

int main(int argc, char **argv) {
    // Initialize ncurses
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    // Create a window for the menu
    WINDOW *menuwin = newwin(10, 40, 5, 10);
    box(menuwin, 0, 0);
    refresh();
    wrefresh(menuwin);

    // Define menu items
    char *choices[] = {
        "Start Game",
        "Options",
        "Exit"
    };
    int n_choices = sizeof(choices) / sizeof(char *);
    int choice;
    int highlight = 0;

    while (1) {
        // Display menu items
        for (int i = 0; i < n_choices; i++) {
            if (i == highlight) {
                wattron(menuwin, A_REVERSE);
            }
            mvwprintw(menuwin, i + 1, 1, choices[i]);
            wattroff(menuwin, A_REVERSE);
        }

        // Get user input
        choice = wgetch(menuwin);
        int real_choice = getch();

        switch (real_choice) {
            case 259:
                highlight--;
                if (highlight < 0) {
                    highlight = 0;
                }
                break;
            case 258:
                highlight++;
                if (highlight >= n_choices) {
                    highlight = n_choices - 1;
                }
                break;
            case 10:
                if (highlight == n_choices - 1) {
                    endwin();
                    return 0;
                } else {
                    if (highlight == 0) {
                        refresh();
                        endwin();
                        in_game("./map/Level_1");
                    }
                    mvprintw(15, 1, "You chose: %s", choices[highlight]);
                    
                    break;
                }
                
        }
        //printf("%d\n", highlight);
    }

    // End ncurses
    

    return 0;
}
