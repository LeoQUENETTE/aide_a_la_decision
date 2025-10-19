#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_KEY_VAL_LEN 50

typedef struct {
    char *key;
    char *value;
} Entry;

typedef struct {
    Entry *entries;
    int size;
    int capacity;
} Dictionary;

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
        free(dict->entries[i].value);
    }

    free(dict->entries);
    free(dict);
}


void add_entry(Dictionary *dict, const char *key, const char *value) {
    if (dict->size >= dict->capacity) {
        dict->capacity *= 2;
        dict->entries = realloc(dict->entries, sizeof(Entry) * dict->capacity);
        if (!dict->entries) {
            perror("Erreur de réallocation");
            exit(1);
        }
    }

    dict->entries[dict->size].key = malloc(strlen(key) + 1);
    dict->entries[dict->size].value = malloc(strlen(value) + 1);

    strcpy(dict->entries[dict->size].key, key);
    strcpy(dict->entries[dict->size].value, value);
    dict->size++;
}

const char* get_value(Dictionary *dict, const char *key) {
    for (int i = 0; i < dict->size; i++) {
        if (strcmp(dict->entries[i].key, key) == 0) {
            return dict->entries[i].value;
        }
    }
    return NULL;
}

void print_dict(Dictionary *dict) {
    printf("---- Contenu du dictionnaire ----\n");
    for (int i = 0; i < dict->size; i++) {
        printf("%s : %s\n", dict->entries[i].key, dict->entries[i].value);
    }
}
