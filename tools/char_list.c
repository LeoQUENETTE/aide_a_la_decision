#include "char_list.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void free_char_list(char** list, int size) {
    for (int i =0; i < size; i++) {
        free(list[i]);
    }
    free(list);
}

void shuffle_list(char **list, int n) {
    if (list == NULL || n <= 1) return;

    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        char *temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
}

char** copy_char_list(char **src, int count) {
    char **dst = malloc(sizeof(char*) * count);
    for (int i = 0; i < count; i++) {
        dst[i] = malloc(strlen(src[i]) + 1);
        strcpy(dst[i], src[i]);
    }
    return dst;
}