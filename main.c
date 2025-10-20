#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "tools/dict.h"
#include "tools/char_list.h"



char** generateAlphabet(int n) {
    int compteur = 0;
    char prefix[3] = "";
    char **labels = malloc(n * sizeof(char*));

    for (char c = 'a'; compteur < n; ++c) {
        if (c > 'z') {
            c = 'a';
            if (prefix[0] == '\0') {
                prefix[0] = 'a';
                prefix[1] = '\0';
            } else {
                prefix[0]++;
            }
        }
        char label[4];
        if (prefix[0] != '\0')
            sprintf(label, "%s%c", prefix, c);
        else
            sprintf(label, "%c", c);

        labels[compteur] = malloc(strlen(label) + 1);
        strcpy(labels[compteur], label);
        compteur++;
    }
    return labels;
}

char** generateNumbers(int n) {
    char **numbers = malloc(sizeof(char*) * n);
    char nombre_str[12];
    for (int i = 0; i < n; i++) {
        sprintf(nombre_str, "%d", i);
        numbers[i] = malloc(strlen(nombre_str)+1);
        strcpy(numbers[i], nombre_str);
    }
    return numbers;
}


int main() {
    int n = 5;
    srand((unsigned int) time(NULL));

    Dictionary *school_pref = create_dict(4);
    Dictionary *scholar_pref = create_dict(4);

    char** schools = generateAlphabet(n);
    char** scholars = generateNumbers(n);


    for (int i = 0; i < n; i++) {
        char** copy_scholars = copy_char_list(scholars,n);
        char** copy_schools = copy_char_list(schools,n);
        
        shuffle_list(copy_scholars,n);
        shuffle_list(copy_schools,n);
        
        add_entry(scholar_pref, scholars[i], make_string_list_value(copy_schools,n));
        add_entry(school_pref, schools[i], make_string_list_value(copy_scholars,n));

        free_char_list(copy_scholars,n);
        free_char_list(copy_schools,n);
    }

    print_dict(school_pref,0);
    printf("\n");
    print_dict(scholar_pref,0);

    free_dict(school_pref);
    free_dict(scholar_pref);
    
    printf("OK dict free\n");
    
    free_char_list(schools, n);
    free_char_list(scholars, n);

    printf("OK all free\n");
    return 0;
}