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
    v.data = my_strdup(str);
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

char* my_strdup(const char* str) {
    if (str == NULL) return NULL;
    
    size_t len = strlen(str) + 1;
    char* copy = malloc(len);
    if (copy != NULL) {
        memcpy(copy, str, len);
    }
    return copy;
}
struct Entry {
    char *key;
    Value value;
};
int get_value_pos(Entry* e, char* wanted_char){
    if (e == NULL || wanted_char == NULL){
        printf("Empty or null entry\n");
        return -1;
    }
    Value val = e->value;
    if (val.type != VALUE_STRING_LIST){
        printf("Value format uncorrect\n");
        return -1;
    }
    for (int i = 0; i < val.count; i++ ){
        char* c = &val.data[i];
        if (c == wanted_char){
            return i;
        }
    }
    printf("Not found\n");
    return -1;

}

struct Dictionary{
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
        Entry *new_entries = realloc(dict->entries, sizeof(Entry) * dict->capacity);
        if (!new_entries) {
            fprintf(stderr, "Erreur: échec du realloc\n");
            exit(1);
        }
        dict->entries = new_entries;
    }

    dict->entries[dict->size].key = my_strdup(key);
    dict->entries[dict->size].value = value;
    dict->size++;
}
Entry get_entry(Dictionary *dict, const char *key){
    if (dict->size <= 0){
        return;
    }
    for (int i = 0; i < dict->size; i++){
        Entry e = dict->entries[i];
        char* i_key = e.key;
        if (i_key == key){
            return e;
        }
    }
    return;
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

