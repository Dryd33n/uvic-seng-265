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

    float** rpfArr = getRpfArr(survey, filterMap);
    printQuestionsWithRPF(rpfArr, survey);

    free(config);
 }


