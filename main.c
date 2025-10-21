#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "tools/dict.h"
#include "tools/char_list.h"



char** generateAlphabet(int n) {
    char **labels = malloc(n * sizeof(char*));
    if (!labels) return NULL;
    
    int count = 0;
    
    for (char c = 'a'; c <= 'z' && count < n; c++, count++) {
        labels[count] = malloc(2);
        labels[count][0] = c;
        labels[count][1] = '\0';
    }

    for (char c1 = 'a'; count < n; c1++) {
        for (char c2 = 'a'; c2 <= 'z' && count < n; c2++, count++) {
            labels[count] = malloc(3);
            labels[count][0] = c1;
            labels[count][1] = c2;
            labels[count][2] = '\0';
        }
    }
    
    return labels;
}

char** generateNumbers(int n) {
    char **numbers = malloc(sizeof(char*) * n);
    if (!numbers) return NULL;
    
    for (int i = 0; i < n; i++) {
        numbers[i] = malloc(12);
        if (!numbers[i]) {
            for (int j = 0; j < i; j++) free(numbers[j]);
            free(numbers);
            return NULL;
        }
        sprintf(numbers[i], "%d", i);
    }
    return numbers;
}

void simple_algo(Dictionary *prio_dict, Dictionary *second_dict){
    if (second_dict->size <= 0 && prio_dict->size <= 0){
        return;
    }

    // int n = second_dict->size;
    // for (int i = 0; i < n; i++){
        
    // }
    return;
}

int main() {
    int n = 5;
    srand((unsigned int) time(NULL));

    Dictionary *school_pref = create_dict(n);
    Dictionary *scholar_pref = create_dict(n);

    char** schools = generateAlphabet(n);
    char** scholars = generateNumbers(n);

    
    for (int i = 0; i < n; i++) {
        char** copy_scholars = copy_char_list(scholars,n);
        char** copy_schools = copy_char_list(schools,n);
        
        shuffle_list(copy_scholars,n);
        shuffle_list(copy_schools,n);
        
        add_entry(scholar_pref, scholars[i], make_string_list_value(copy_schools,n));
        add_entry(school_pref, schools[i], make_string_list_value(copy_scholars,n));
    }

    simple_algo(school_pref, scholar_pref);

    Entry e = get_entry(school_pref, "a");
    int pos = get_value_pos(&e,"1");
    printf("%i\n",pos);

    free_dict(school_pref);
    free_dict(scholar_pref);
    
    free_char_list(schools, n);
    free_char_list(scholars, n);
    return 0;
}