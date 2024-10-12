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
    /* READ DATA */
    int* config     = readConfig();              //reads config from stdin
    Survey survey   = readSurvey();              //reads questions, directions, likerts, respondees
    int* filterMap  = filterSurvey(&survey);     //reads filters at bottom


    /* PROCESSING AND OUTPUT */
    printIntro(survey.counts.numValidRespondents);

    if(config[0]==1){                                               //FOR RELATIVE PERCENTUAL FREQUENCIES
        float** rpfArr = getRpfArr(survey, filterMap);              //Get required data to print RPF
        printQuestionsWithRPF(rpfArr, survey);                      //Print data
        free2dArr((void **) rpfArr, survey.counts.numQuestions);    //Free RPF data Array
    }

    if(config[1] == 1 || config[2]==1){
        float** catScores = getCatScoreArr(survey, filterMap);                   //Get category scores required for both

        if(config[1] == 1){                                                      //FOR CATEGORY SCORES
            printResponseCatScores(catScores, survey.counts.numValidRespondents);//Print category scores
        }

    if(config[2]==1) {                                                           //FOR AVG CATEGORY SCORES
            double* avgCatScores = getAvgCatScores(catScores, survey.counts);    //Get average category scores
            printAvgCatScores(avgCatScores);                                     //Print average category scores
            free(avgCatScores);                                                  //Free avg category scores data array
        }

        free2dArr((void**)catScores, 5);                                  //Free category scores data array
    }


    /* FREE DYNAMICALLY ALLOCATED MEMORY */
    free(config);         //Free config int array
    freeSurvey(survey);   //Free survey struct
    free(filterMap);      //Free filter map int array
 }


