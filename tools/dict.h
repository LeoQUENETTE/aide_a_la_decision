#ifndef DICT_H
#define DICT_H

#include "char_list.h"

typedef struct {
    char *key;
    char **value; 
    int value_count;
} Entry;

typedef struct {
    Entry *entries;
    int size;
    int capacity;
} Dictionary;

Dictionary* create_dict(int capacity);
void free_dict(Dictionary *dict);
void add_entry(Dictionary *dict, const char *key, char **value, int value_count);
void print_dict(Dictionary *dict);

#endif
