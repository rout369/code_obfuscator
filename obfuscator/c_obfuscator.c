#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE 1024
#define MAX_CODE 10000

// Function to obfuscate variable names
void obfuscate_variables(char *code) {
    // Define original and obfuscated variable names
    char *original_vars[] = {"x", "y", "sum", "add"};
    char *obfuscated_vars[] = {"a1B", "b2C", "sX9", "fZ7"};
    
    int var_count = sizeof(original_vars) / sizeof(original_vars[0]);

    for (int i = 0; i < var_count; i++) {
        char *pos = strstr(code, original_vars[i]);
        while (pos) {
            // Replace the variable name in-place
            strncpy(pos, obfuscated_vars[i], strlen(obfuscated_vars[i]));
            pos = strstr(pos + strlen(obfuscated_vars[i]), original_vars[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (!input) {
        printf("Error opening input file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (!output) {
        printf("Error opening output file.\n");
        fclose(input);
        return 1;
    }

    char line[MAX_LINE];
    char obfuscated_code[MAX_CODE] = "";

    while (fgets(line, sizeof(line), input)) {
        strcat(obfuscated_code, line);
    }

    obfuscate_variables(obfuscated_code);

    fputs(obfuscated_code, output);

    fclose(input);
    fclose(output);

    printf("C Code Obfuscation Complete!\n");
    return 0;
}
