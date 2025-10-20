#ifndef DICT_H
#define DICT_H

#include "char_list.h"

typedef enum {
    VALUE_STRING,
    VALUE_STRING_LIST,
    VALUE_DICTIONARY
} ValueType;

typedef struct {
    ValueType type;
    void *data;
    int count;
} Value;

typedef struct {
    char *key;
    Value value;
} Entry;

typedef struct {
    Entry *entries;
    int size;
    int capacity;
} Dictionary;

void print_value(Value v, int indent); 
void print_indent(int indent);
void free_value(Value v);
Value make_string_value(const char *str);
Value make_string_list_value(char **list, int count);
Value make_dict_value(Dictionary *subdict);

Dictionary* create_dict(int capacity);
void free_dict(Dictionary *dict);
void add_entry(Dictionary *dict, const char *key, Value value);
void print_dict(Dictionary *dict, int indent);

#endif
