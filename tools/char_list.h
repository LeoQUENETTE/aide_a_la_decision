#ifndef CHAR_LIST_H
#define CHAR_LIST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void free_char_list(char** list, int size);
void shuffle_list(char **list, int n);
char** copy_char_list(char **src, int count);

#endif
