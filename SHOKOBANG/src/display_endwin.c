#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ncurses.h>

#define MAX_BUFFER_SIZE 10024

char* executeCommand(const char* command) {
    FILE* fp;
    char buffer[MAX_BUFFER_SIZE];
    char* result;

    // Open the command for reading
    fp = popen(command, "r");
    if (fp == NULL) {
        printf("Failed to run command\n");
        exit(1);
    }

    // Read the output and store it in a buffer
    size_t bytesRead = fread(buffer, 1, sizeof(buffer) - 1, fp);
    buffer[bytesRead] = '\0';

    // Close the pipe
    pclose(fp);

    // Allocate memory for the result and copy the buffer content
    result = strdup(buffer);

    return result;
}

int display_endwin() {
    // Initialize ncurses
    system("cat map/chocolatine.txt");

    return 0;
}
