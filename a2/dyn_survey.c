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
    Survey survey = readSurvey();
    int* filterMap = filterSurvey(&survey);

    printIntro(survey.counts.numRespondents - survey.counts.numFilteredOutRespondents);


    if(config[0]==1){
        float** rpfArr = getRpfArr(survey, filterMap);
        printQuestionsWithRPF(rpfArr, survey);
        free2dArr((void **) rpfArr, survey.counts.numQuestions);
    }

    if(config[1] == 1 || config[2]==1){
        float** catScores = getCatScoreArr(survey, filterMap);

        if(config[1] == 1){
            printResponseCatScores(catScores, survey.counts.numRespondents-survey.counts.numFilteredOutRespondents);
        }

        if(config[2]==1) {
            double* avgCatScores = getAvgCatScores(catScores, survey.counts);
            printAvgCatScores(avgCatScores);
            free(avgCatScores);
        }

        free2dArr((void**)catScores, 5);
    }

    free(config);
    freeSurvey(survey);
    free(filterMap);
 }


