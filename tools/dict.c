#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dict.h"
#include "char_list.h" 

struct Entry {
    char *key;
    char **value; 
    int value_count;
};

struct Dictionary {
    Entry *entries;
    int size;
    int capacity;
};

Dictionary* create_dict(int capacity) {
    Dictionary *dict = malloc(sizeof(Dictionary));
    if (!dict) return NULL;

    dict->entries = malloc(sizeof(Entry) * capacity);
    if (!dict->entries) {
        free(dict);
        return NULL;
    }

    dict->size = 0;
    dict->capacity = capacity;
    return dict;
}

void free_dict(Dictionary *dict) {
    if (!dict) return;

    for (int i = 0; i < dict->size; i++) {
        free(dict->entries[i].key);
        for (int j = 0; j < dict->entries[i].value_count; j++) {
            free(dict->entries[i].value[j]);
        }
        free(dict->entries[i].value);
    }

    free(dict->entries);
    free(dict);
}

void add_entry(Dictionary *dict, const char *key, char **value, int value_count) {
    if (dict->size >= dict->capacity) {
        dict->capacity *= 2;
        dict->entries = realloc(dict->entries, sizeof(Entry) * dict->capacity);
        if (!dict->entries) {
            perror("Erreur de réallocation");
            exit(1);
        }
    }

    dict->entries[dict->size].key = malloc(strlen(key) + 1);
    strcpy(dict->entries[dict->size].key, key);

    dict->entries[dict->size].value = copy_char_list(value, value_count);
    dict->entries[dict->size].value_count = value_count;

    dict->size++;
}

void print_dict(Dictionary *dict) {
    printf("---- Contenu du dictionnaire ----\n");
    for (int i = 0; i < dict->size; i++) {
        printf("%s : [", dict->entries[i].key);
        for (int j = 0; j < dict->entries[i].value_count; j++) {
            printf("%s", dict->entries[i].value[j]);
            if (j < dict->entries[i].value_count - 1) printf(", ");
        }
        printf("]\n");
    }
}