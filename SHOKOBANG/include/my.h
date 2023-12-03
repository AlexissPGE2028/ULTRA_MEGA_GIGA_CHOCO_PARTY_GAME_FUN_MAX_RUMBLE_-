/*
** EPITECH PROJECT, 2023
** my.h
** File description:
** prototype of all lib
*/

#include <stdarg.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#ifndef MY
    #define MY
typedef struct {
    int width;
    int length;
}TAILLE_MAP_T;
    #include <ncurses.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include "../lib/my_printf/include/my.h"

int check_h(int argc, char **argv);
int check_loose(char **map_tab, char **map_tab_init);
char **my_arraycpy(char **tab);
int input_rigth(char **map_tab, char **map_tab_init, int *posX, int *posY);
int input_left(char **map_tab, char **map_tab_init, int *posX, int *posY);
int input_down(char **map_tab, char **map_tab_init, int *posX, int *posY);
int input_up(char **map_tab, char **map_tab_init, int *posX, int *posY);
char *my_strcpy(char *dest, char const *src);
char *my_strcat(const char *str1, const char *str2);
char **my_str_to_word_array(char const *str);
int my_show_array(char **tab);
void my_putchar(char c);
int my_putstr(char const *str);
int count_digit(int nb);
int my_len_array(char **tab);
#endif
