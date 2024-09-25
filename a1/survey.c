#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RESPONDENTS 5
#define NUM_QUESTIONS 38
#define NUM_LIKERTS 6

#define MAX_LINE_LEN 4096

/**
 * struct to hold question, question direction and question category
 */
struct Question {
    char question[128];
    _Bool directDirection; //true = direct, false = reverse, true = default
    char category[2];
};


void printIntro(const int numRespondents) {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n\n");
    printf("NUMBER OF RESPONDENTS: %d\n\n", numRespondents);
}


void readLine(char input[MAX_LINE_LEN]) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {
        if(input[0] != '#') {
            break;
        }
    }
}


/**
 * Reads the config line from stdin and store it into array of ints
 * @param arr the 4 bit configuration array
 */
void readConfig(int * arr) {
    char input[MAX_LINE_LEN]; //Buffer to hold config line
    const char delim[2] = ",";
    int i = 0; //iterator for walking through tokens



    readLine(input);

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
    char input[MAX_LINE_LEN];
    const char delim[2] = ";";
    int i = 0;

    readLine(input);

    input[strcspn(input, "\n")] = '\0';

    const char *token = strtok(input, delim); //get first token

    while (token != NULL) { // walk through rest of token
        struct Question curQuestion; // initialize question struct


        strncpy(curQuestion.question, token, sizeof(curQuestion.question)); // Assign question
        curQuestion.question[sizeof(curQuestion.question) -1] = '\0'; // Ensure null termination

        curQuestion.category[0] = token[0]; // Assign question category
        curQuestion.category[1] = '\0'; // Ensure null termination

        curQuestion.directDirection = true; //set default value

        questions[i++] = curQuestion;
        token = strtok(NULL, delim);
    }
}



/**
 * Reads line #3 Containing direction information and stores it into Question struct array
 * @param questions Array of Question structs for which the direction will be assigned
 */
void readDirections(struct Question * questions) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ";";
    int i = 0;

    readLine(input);

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




/**
 * Reads line #4 containing likers and stores them into the given likert array
 * @param likerts array of strings to store the 6 likerts
 */
void readLikerts(char(* likerts)[32]) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ",";
    int i = 0;

    readLine(input);

    const char *token = strtok(input, delim);

    while (token != NULL) {
        strcpy(likerts[i++], token);
        token = strtok(NULL, delim);
    }
}





void initializeEmptyResponses(int(* responseArr)[NUM_LIKERTS]) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < NUM_LIKERTS; ++j) {
            responseArr[i][j] = 0;
        }
    }
}

void initializeEmptyResponsesRPF(float(* responseRPFArr)[NUM_LIKERTS]) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < NUM_LIKERTS; ++j) {
            responseRPFArr[i][j] = 0;
        }
    }
}

void printQuestionsWithRPF(struct Question * questions, float(* rpfArr)[NUM_LIKERTS], char(* likerts)[32]) {
    printf("FOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT\n");

    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        printf("\n%s", questions[i].question);

        for (int j = 0; j < NUM_LIKERTS; ++j) {
            printf("\n%.2f: ", rpfArr[i][j]);
            printf("%s", likerts[j]);
        }
    }
}



void tokenizeResponse(int(* responseArr)[NUM_QUESTIONS], char * input, int index){
    char delim[2] = ",";
    int i = 0;

    const char *token = strtok(input, delim);

    while (token != NULL) {
        if(i > 2) {
        }

        token = strtok(NULL, delim);
        i++;
    }
}

int readResponses(int(* responseArr)[NUM_QUESTIONS]) {
    char input[MAX_LINE_LEN];
    int i = 0;

    while (fgets(input, MAX_LINE_LEN, stdin)) {
        if(input[0] != '#') {
            tokenizeResponse(responseArr, input , i);
        }
    }

    return i;
}

int main() {
    int config[4];                  //Configuration
    struct Question questions[NUM_QUESTIONS];  //Array Of Questions
    char likerts[NUM_LIKERTS][32];

    int responses[NUM_QUESTIONS][NUM_LIKERTS];
    float responsesRPF[NUM_QUESTIONS][NUM_LIKERTS];

    int numRespondents;

    initializeEmptyResponses(responses);

    readConfig(config);
    readQuestions(questions);
    readDirections(questions);
    readLikerts(likerts);

    if(config[0]==1) {
        numRespondents = 0;
        initializeEmptyResponsesRPF(responsesRPF);
        printIntro(numRespondents);
        printQuestionsWithRPF(questions, responsesRPF, likerts);
    }else{
        
        if(config[1]==1) {
            //numRespondents = readResponses(responses);
            //printIntro(numRespondents);
            printQuestionsWithRPF(questions, responsesRPF, likerts);
        }
    }

    return 0;
}
