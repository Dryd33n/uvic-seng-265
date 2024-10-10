#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "emalloc.h"
#include "dyn_survey.h"

#define MAX_LINE_LEN 3000

void readLine(char input[MAX_LINE_LEN]) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {//read from stdin until EOF
        input[strcspn(input, "\n")] = '\0';
        if(input[0] != '#') {
            break; //stop reading from stdin when non comment line has been found
        }
    }
}


/**COUNT TOKENS
 *Function to count number of tokens in a given string, adapted from dynamic_memory_example.c
 *given by Roberto Bittencourt
 *
 * @param string the string of which tokens will be counter
 * @param delim the delimiter which separates the tokens
 * @return the number of tokens
 */
int countTokens(const char * string, const char * delim) {
    int num_tokens = 0;
    char* stringToCount = emalloc(sizeof(char)* MAX_LINE_LEN);
    strcpy(stringToCount, string);

    /* get the first token from line */
    const char *token = strtok(stringToCount, delim);

    /* for every token in line, count it */
    while (token != NULL) {
        num_tokens++;

        /* get the next token from line or reach end of line */
        token = strtok(NULL, delim);
    }

    free(stringToCount);

    return num_tokens;
}

int* readConfig() {
    const char* delim = ",";
    char buffer[MAX_LINE_LEN]; //buffer to hold line
    readLine(buffer);          //store stdin line to buffer

    const int configTokens = countTokens(buffer, delim);        //number of tokens
    int * configArr = emalloc(sizeof(int) * configTokens); //integer array to store config tokens


    const char* token = strtok(buffer, delim);  //get the first token from the buffer
    int i = 0;                                  //counter to assign token into array

    while (token != NULL) {
        configArr[i] = atoi(token); //stores integer conversion of token into array
        token = strtok(NULL, delim);//gets the next token
        i++;
    }

    return configArr;
}

Question* readQuestions() {
    const char* delim = ";";
    char buffer[MAX_LINE_LEN];
    readLine(buffer);

    const int numQuestions = countTokens(buffer, delim);
    Question* questions = emalloc(sizeof(Question) * numQuestions);

    const char* token = strtok(buffer, delim);


    int i = 0;
    while(token != NULL) {
        Question curQuestion;
        curQuestion.question = emalloc(sizeof(char) * (strlen(token)+1));

        strcpy(curQuestion.question, token); // Assign question



        curQuestion.category[0] = token[0]; // Assign question category
        curQuestion.category[1] = '\0'; // Ensure null termination

        curQuestion.directDirection = true; //set default value



        questions[i++] = curQuestion;
        token = strtok(NULL, delim);
    }

    return questions;
}

void readDirections(Question* questions) {
    const char* delim = ";";
    char buffer[MAX_LINE_LEN];
    readLine(buffer);


    const char* token = strtok(buffer, delim);

    int i = 0;
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

char** readLikerts() {
    const char* delim = ",";
    char buffer[MAX_LINE_LEN];
    readLine(buffer);

    const int numLikerts = countTokens(buffer, delim);
    char** likerts = emalloc(sizeof(char *) * numLikerts);

    const char* token = strtok(buffer, delim);

    int i = 0;
    while (token != NULL) {
        likerts[i] = emalloc(sizeof(char) * (strlen(token)+1));
        strcpy(likerts[i], token);

        token = strtok(NULL, delim);
        i++;
    }



    return likerts;
}

int readNumResponses() {
    char buffer[MAX_LINE_LEN];
    readLine(buffer);
    return atoi(buffer);
}

char** tokenizeRespondee(char* buffer, const int numTokens) {
    char** respondeeTokens = emalloc(sizeof(char *) * numTokens);

    char* token = strtok(buffer, ",");

    int i = 0;
    while(token != NULL) {
        token[strcspn(token, "\n")] = '\0';
        respondeeTokens[i] = emalloc(sizeof(char) * (strlen(token)+1));
        strcpy(respondeeTokens[i],token);
        token = strtok(NULL, ",");
        i++;
    }

    return respondeeTokens;
}

Date tokenizeRespondeeBirthday(char * respondee_token) {
    Date birthday;
    birthday.day = birthday.month = birthday.year = -1;

    const char* token = strtok(respondee_token, "-");

    for (int i = 0; i < 3; ++i) {
        if(i == 0) {
            birthday.year = atoi(token);
        }else if (i == 1) {
            birthday.month = atoi(token);
        }else if (i == 2) {
            birthday.day = atoi(token);
        }

        token = strtok(NULL, "-");
    }

    return birthday;
}



Respondee constructRespondent(char buffer[MAX_LINE_LEN]) {
    Respondee respondee;
    const char delim[2] = ",";
    const int numRespondeeTokens = countTokens(buffer,delim);
    char** respondeeTokens = tokenizeRespondee(buffer, numRespondeeTokens);


    respondee.program = emalloc(sizeof(char) * (strlen(respondeeTokens[0])+1));
    respondee.response = emalloc(sizeof(char *) * (numRespondeeTokens -3));



    strcpy(respondee.program, respondeeTokens[0]);
    respondee.fromCanada = (strcmp(respondeeTokens[1], "yes") == 0);
    respondee.birthday = tokenizeRespondeeBirthday(respondeeTokens[2]);



    for (int i = 0; i < (numRespondeeTokens-3); ++i) {
        respondee.response[i] = emalloc(sizeof(char)*(strlen(respondeeTokens[i+3])+1));
        strcpy(respondee.response[i],respondeeTokens[i+3]);
    }



    freeRespondeeTokens(respondeeTokens, numRespondeeTokens);
    return respondee;
}

Respondee* readResponses(const int numResponses) {
    int i = 0;
    Respondee* respondees = emalloc(sizeof(Respondee) * numResponses);

    while ( i < numResponses) {// for each input line containing response information
        char buffer[MAX_LINE_LEN];
        fgets(buffer, sizeof(buffer), stdin);

        if(buffer[0] != '#') {//ignore line if it is a comment line and keep reading



            respondees[i] = constructRespondent(buffer); //send line off to construct respondent
            i++;

        }
    }





    return respondees;
}