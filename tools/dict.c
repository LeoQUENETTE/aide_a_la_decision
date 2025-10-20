#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dict.h"
#include "char_list.h" 


struct Value{
    ValueType type;
    void *data;
    int count;
};

void print_indent(int indent) {
    for (int i = 0; i < indent; i++){
        printf("  ");
    };
}

void print_value(Value v, int indent) {
    switch (v.type) {
        case VALUE_STRING:
            printf("\"%s\"", (char*)v.data);
            break;

        case VALUE_STRING_LIST: {
            char **list = (char**)v.data;
            printf("[");
            for (int i = 0; i < v.count; i++) {
                printf("\"%s\"", list[i]);
                if (i < v.count - 1) printf(", ");
            }
            printf("]");
            break;
        }

        case VALUE_DICTIONARY:
            printf("{\n");
            print_dict((Dictionary*)v.data, indent + 1);
            print_indent(indent);
            printf("}");
            break;

        default:
            printf("<unknown>");
            break;
    }
}

void free_value(Value v) {
    switch (v.type) {
        case VALUE_STRING:
            free(v.data);
            break;

        case VALUE_STRING_LIST:
            free_char_list((char**)v.data, v.count);
            break;

        case VALUE_DICTIONARY:
            free_dict((Dictionary*)v.data);
            break;

        default:
            break;
    }
}

Value make_string_value(const char *str) {
    Value v;
    v.type = VALUE_STRING;
    v.data = strdup(str);
    v.count = 1;
    return v;
}

Value make_string_list_value(char **list, int count) {
    Value v;
    v.type = VALUE_STRING_LIST;
    v.data = copy_char_list(list, count);
    v.count = count;
    return v;
}

Value make_dict_value(Dictionary *subdict) {
    Value v;
    v.type = VALUE_DICTIONARY;
    v.data = subdict;
    v.count = 0;
    return v;
}
struct Entry {
    char *key;
    Value value;
};

struct Dictionnary{
    Entry *entries;
    int size;
    int capacity;
};


Dictionary* create_dict(int capacity) {
    Dictionary *dict = malloc(sizeof(Dictionary));
    dict->entries = malloc(sizeof(Entry) * capacity);
    dict->size = 0;
    dict->capacity = capacity;
    return dict;
}

void add_entry(Dictionary *dict, const char *key, Value value) {
    if (dict->size >= dict->capacity) {
        dict->capacity *= 2;
        dict->entries = realloc(dict->entries, sizeof(Entry) * dict->capacity);
    }

    dict->entries[dict->size].key = strdup(key);
    dict->entries[dict->size].value = value;
    dict->size++;
}

void free_dict(Dictionary *dict){
    if (!dict) return;
    for (int i = 0; i < dict->size; i++){
        free(dict->entries[i].key);
        free_value(dict->entries[i].value);
    }
    free(dict->entries);
    free(dict);
}

void print_dict(Dictionary *dict, int indent) {
    if (!dict) return;
    for (int i = 0; i < dict->size; i++) {
        print_indent(indent);
        printf("\"%s\": ", dict->entries[i].key);
        print_value(dict->entries[i].value, indent);
        printf("\n");
    }
}