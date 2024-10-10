// INCLUDE LIBRARIES
#include <stdio.h>


// INCLUDE LOCAL HEADERS
#include <stdlib.h>

#include "dyn_survey.h"
#include "input_handling.h"
#include "output.h"
#include "processing.h"
#include "emalloc.h"




int main(){
    int* config = readConfig();
    Question* questions = readQuestions();
    readDirections(questions);
    char** likerts = readLikerts();
    const int numResponses = readNumResponses();
    Respondee *respondees = readResponses(numResponses);

    printIntro(numResponses);
    

    //TODO REMOVE DEBUG CODE
    // printf("Config:");
    // for (int i = 0; i < 3; ++i) {
    //     printf("%d,",config[i]);
    // }
    // printf("\n");
    // for (int i = 0; i < 38; ++i) {
    //     printf("Question(%d): Cat: %s;, Dir: %s; Ques: %s;\n",i+1,questions[i].category,
    //         questions[i].directDirection ? "dir":"rev",
    //         questions[i].question);
    // }
    // for (int j = 0; j < 6; ++j) {
    //     printf("Likert(%d): %s;\n",j, likerts[j]);
    // }
    // for (int j = 0; j < numResponses; ++j) {
    //     printf("\nRespondee (%d):, Program: %s; From Can: %s; Birthday: %d-%d-%d;\n",j+1,respondees[j].program
    //                                               ,respondees[j].fromCanada ? "yes" : "no"
    //                                               ,respondees[j].birthday.year
    //                                               ,respondees[j].birthday.month
    //                                               ,respondees[j].birthday.day);
    //     for (int k = 0; k < 38; ++k) {
    //         printf("%s,", respondees[j].response[k]);
    //     }
    //     printf("\n");
    // }

    //free(respondees);
    free(config);
    free(questions);
    for (int i = 0; i < 6; ++i) {
        free(likerts[i]);
    }
    free(likerts);
 }


