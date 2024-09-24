#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



/**
 * struct to hold question, question direction and question category
 */
struct Question {
    char question[128];
    _Bool directDirection; //true = direct, false = reverse, true = default
    char category[2];
};

void printIntro() {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n");
}



/**
 * Reads the config line from stdin and store it into array of ints
 * @param arr the 4 bit configuration array
 */
void readConfig(int * arr) {
    const char delim[2] = ",";
    int i = 0; //iterator for walking through tokens

    char input[16]; //Buffer to hold config line
    fgets(input, sizeof(input), stdin); //Store config line into buffer

    const char *token = strtok(input, delim); // get the first token

    while( token != NULL ) {    // walk through rest of tokens
        arr[i++] = atoi(token); //convert each config value to an int
        token = strtok(NULL, delim);
    }
}



/**
 * Reads line of set of questions and stores it in an array of Question structs
 * @param questions array of Question structs
 */
void readQuestions(struct Question * questions) {
    const char delim[2] = ";";
    int i = 0;

    char input[4096];
    fgets(input, sizeof(input), stdin); // read line #2 containing questions

    const char *token = strtok(input, delim); //get first token

    while (token != NULL) { // walk through rest of token
        struct Question curQuestion; // initialize question struct


        strncpy(curQuestion.question, token, sizeof(curQuestion.question)); // Assign question
        curQuestion.question[sizeof(curQuestion.question) -1] = '\0'; // Ensure null termination

        curQuestion.category[0] = token[0]; // Assign question category
        curQuestion.category[1] = '\0'; // Ensure null termination

        questions[i++] = curQuestion;
        token = strtok(NULL, delim);
    }
}



/**
 * Reads line #3 Containing direction information and stores it into Question struct array
 * @param questions Array of Question structs for which the direction will be assigned
 */
void readDirections(struct Question * questions) {
    const char delim[2] = ";";
    int i = 0;

    char input[512];
    fgets(input, sizeof(input), stdin);

    // Remove newline character if present
    input[strcspn(input, "\n")] = '\0';

    const char *token = strtok(input, delim);

    while (token != NULL) {
        if(strcmp(token, "Direct")==0) {
            questions[i].directDirection = true;
        }else if(strcmp(token, "Reverse")==0) {
            questions[i].directDirection = false;
        }

        i++;
        token = strtok(NULL, delim);
    }


}

int main(void) {
    int config[4];
    struct Question questions[38];

    printIntro();
    readConfig(config);
    readQuestions(questions);
    readDirections(questions);

    return 0;
}
