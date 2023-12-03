##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## emacs
##

NAME = MY_CHOCOBANG

SRC =	  src/main.c\
	  lib/my_count_digits.c\
	  lib/my_str_to_word_array.c\
	  lib/my_show_array.c\
	  lib/my_strcat.c\
	  lib/my_len_array.c\
	  lib/my_array_cpy.c\
	  lib/my_strcpy.c\
	  src/all_input.c\
	  src/verif_loose_or_win.c\
	  src/display_endwin.c

all :
	make -C lib/my_printf
	gcc -g3 -o $(NAME) $(SRC) lib/my_printf/libmy.a -lncurses

clean :
	rm -f *~
	rm -f #*#
	rm -f $(OBJ)
	rm -f *.gc*

fclean : clean
	rm -f $(NAME)

re : fclean all

.PHONY: all clean fclean re lib
