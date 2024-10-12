#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "emalloc.h"
#include "input_handling.h"
/**LIKERT TO VAL:
 *
 * Converts a given likert string to a value
 * @param likertStr the likert string to be converted
 * @param likerts array of likerts to compare to
 * @return returns the value of the likert
 */
int likertToVal(const char * likertStr,
                char** likerts)
{
    char* cleanLikert = emalloc(sizeof(char)*(strlen(likertStr)+1));
    strcpy(cleanLikert,likertStr);
    cleanLikert[strcspn(cleanLikert, "\n")] = 0;

    for (int i = 0; i < 6; ++i) {//walk through all possible options for likerts
        if(strcmp(cleanLikert, likerts[i]) == 0) {//compare likert[i] to give likert to see if they match
            free(cleanLikert);
            return i+1;
        }
    }
    free(cleanLikert);
    return -1;  // default case if likert is not found
}














/**SUMMATE RESPONSES:
 *
 * Summate the number of times each likert was chosen for each question
 * @param respondees array of respondee structs
 * @param numRespondents integer containing the number of respondents
 * @param numQuestions
 * @param likerts array of likerts
 */
int** summateResponses(const Respondee* respondees,
                       char** likerts,
                       const Counts counts,
                       int* filterMap) {
    int** responsesSum = emalloc(sizeof(int*)* counts.numQuestions);
    for (int i = 0; i < counts.numQuestions; ++i) {
        responsesSum[i] = emalloc(sizeof(int) * counts.numLikerts);
    }

    for (int i = 0; i < counts.numQuestions; ++i) {
        for (int j = 0; j < counts.numLikerts; ++j) {
            responsesSum[i][j]=0;
        }
    }

    for (int i = 0; i < counts.numRespondents; ++i) {      //for each respondent

        if(filterMap[i]==1) {
            for (int j = 0; j < counts.numQuestions; ++j) {   //for each question answered by respondent
                const int likertVal = likertToVal(respondees[i].response[j], likerts); //convert likert string to respective value
                responsesSum[j][likertVal-1]++; //increment the sum of the respective likert for question i
            }
        }
    }

    return responsesSum;
}




/**MAKE RELATIVE PERCENTUAL FREQUENCY ARRAY:
 *
 * Makes and calculates the relative percentual frequency array from the sum of each time a likert was chosen
 */
float** makeRPFArr(int** responseSum, Counts counts) {
    float** rpfArr = emalloc(sizeof(float*)*counts.numQuestions);
    for (int i = 0; i < counts.numQuestions; ++i) {
        rpfArr[i] = emalloc(sizeof(float) * counts.numLikerts);
    }

    for (int i = 0; i < counts.numQuestions; ++i) {   //for each question
        for (int j = 0; j < 6; ++j) {           //for each likert sum for question i
            rpfArr[i][j] = (float)responseSum[i][j] / (float)(counts.numRespondents - counts.numFilteredOutRespondents) * 100;
        }
    }

    return rpfArr;
}

float ** getRpfArr(const Survey survey, int* filterMap) {
    int** summateArr = summateResponses(survey.respondees, survey.likerts, survey.counts, filterMap);
    float** rpfArr   = makeRPFArr(summateArr, survey.counts);

    free2dArr((void**)summateArr, survey.counts.numQuestions);

    return rpfArr;
}















/**COMPUTE RESPONSES SCORE ARRAY:
 *
 * Computes the responses score array from the respondees array from which likerts where chosen and their
 * corresponding values
 */
int** computeResponsesScoreArr(const Survey survey, const int* filterMap) {
    int numValidRespondents = survey.counts.numRespondents - survey.counts.numFilteredOutRespondents;

    int** responseScores = emalloc(sizeof(int *) * survey.counts.numQuestions);
    for (int i = 0; i <survey. counts.numQuestions; ++i) {
        responseScores[i] = emalloc(sizeof(int) * numValidRespondents);
    }

    int counter = 0;
    for (int i = 0; i < survey.counts.numRespondents; ++i) {      //for each respondent's response
        if(filterMap[i] == 1){
            for (int j = 0; j < survey.counts.numQuestions; ++j) {   //for each question answered by respondent i
                const int likertVal = likertToVal(survey.respondees[i].response[j], survey.likerts); //convert likert string to respective value
                int likertValDirected = likertVal;
                if(!survey.questions[j].directDirection) { //if question is reverse directed then reverse the value
                    likertValDirected = 7 - likertVal;
                }
                responseScores[j][counter] = likertValDirected;
            }

            counter++;
        }
    }

    return responseScores;
}
//
//
//
/**MAKE RESPONSES CATEGORY SCORE ARRAY:
 *
 * Makes the responses category score array from the responses score array by averaging the scores of each category
 * for each respondent
 * @param responsesCatScores 2D array to store the responses category scores
 * @param responsesScores 2D array containing the responses scores
 * @param questions array of questions
 * @param numRespondents integer containing the number of respondents
 */
float** makeResponsesCatScoreArr(int** responsesScores, Survey survey) {
    const int validRespondents = survey.counts.numRespondents - survey.counts.numFilteredOutRespondents;
    float** responsesCatScores = emalloc(sizeof(float*)*5);
    for (int i = 0; i < 5; ++i) {
        responsesCatScores[i] = emalloc(sizeof(float)*validRespondents);
    }


    for (int i = 0; i < validRespondents; ++i) {                  //for each respondent
        char* cats[5] = {"C","I","G","U","P"};
        int catCount[5]={0,0,0,0,0};
        int catSum[5]={0,0,0,0,0};

        for (int j = 0; j < survey.counts.numQuestions; ++j) {               //for each question answered for respondent i
            int cat=-1;

            for (int k = 0; k < 5; ++k) {
                if(strcmp(cats[k], survey.questions[j].category) == 0) {
                    cat = k;
                }
            }

            catCount[cat]++;
            catSum[cat]+=responsesScores[j][i];
        }


        for (int j = 0; j < 5; ++j) { //for each category
            responsesCatScores[j][i] = (float) catSum[j] / (float) catCount[j];
        }
    }

    return responsesCatScores;
}

float** getCatScoreArr(const Survey survey, const int* filterMap) {
    int** responseScoreArr = computeResponsesScoreArr(survey, filterMap);
    float** catScoreArr = makeResponsesCatScoreArr(responseScoreArr, survey);

    free2dArr((void**)responseScoreArr, survey.counts.numQuestions);

    return catScoreArr;
}











double* getAvgCatScores(float** catScores, const Counts counts) {
    double* avgCatScores = emalloc(sizeof(double) * 5);
    int validRespondents = counts.numRespondents - counts.numFilteredOutRespondents;

    for (int i = 0; i < 5; ++i) {      //for each category score
        float catSum = 0;
        for (int j = 0; j < validRespondents; ++j) {  //for each respondent's category score for category i
            catSum += catScores[i][j];
        }
        avgCatScores[i] = (double)catSum / (double)validRespondents;    //compute average category score
    }

    return avgCatScores;
}

