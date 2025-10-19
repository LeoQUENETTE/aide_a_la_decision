#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dict.c"

char** generateAlphabet(int n){
    int compteur = 0;
    char prefix[3] = "";
    const int TAILLE_MAX_CHAINE = n / 26; 
    char **labels = malloc(n * sizeof(char*));
    if (labels == NULL) {
        perror("malloc failed");
        exit(EXIT_FAILURE);
    }
    for (char c = 'a'; compteur < n; ++c){
        if (c > 'z') {
            c = 'a';
            if (prefix[0] == '\0') {
                prefix[0] = c; 
                prefix[1] = '\0';
            } else {    
                prefix[0]++;
            }
        }
        char label[4];
        if (prefix[0] != '\0'){
            sprintf(label, "%s%c", prefix, c);}
        else{
            sprintf(label, "%c", c);}
        
        labels[compteur] = malloc(strlen(label) + 1);
        strcpy(labels[compteur], label);
        compteur = compteur + 1;
    }
    return labels;
}

int main() {
    Dictionary *dict = create_dict(4);
    int n = 26 * 6;
    char nombre_str[10];
    char** labels = generateAlphabet(n);
    for (int i = 0; i < n; i++){
        sprintf(nombre_str, "%d", i);
        printf("%c\n",labels[i]);
        add_entry(dict, nombre_str, labels[i]);
        free(labels[i]);
    }
    free(labels);
    print_dict(dict);
    return 0;
}
