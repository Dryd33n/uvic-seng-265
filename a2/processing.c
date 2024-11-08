//HEADER INCLUSIONS
#include "emalloc.h"
#include "input_handling.h"

//LIBRARY INCLUSIONS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



/*              ╔═══════════════════════╗
 *              ║        HELPERS        ║
 *              ╚═══════════════════════╝
 */



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








/*              ╔══════════════════════════════════════════════════════╗
 *              ║       RELATIVE PERCENTUAL FREQUENCIES HELPERS        ║
 *              ╚══════════════════════════════════════════════════════╝
 */



/**SUMMATE RESPONSES:
 *
 * Summates the responses for each likert for each question
 * @param respondees array of respondees
 * @param likerts array of likerts
 * @param counts struct containing the number of questions, likerts, and respondents
 * @param filterMap array of integers containing the filter map
 * @return returns the 2D array containing the sum of each likert for each question
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





/**MAKE RELATIVE PERCENTUAL FREQUENCIES ARRAY:
 *
 * Makes the relative percentual frequencies array from the responses sum array
 * @param responseSum 2D array containing the sum of each likert for each question
 * @param counts struct containing the number of questions, likerts, and respondents
 * @return returns the relative percentual frequencies array
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







/*              ╔══════════════════════════════════════╗
 *              ║       CATEGORY SCORES HELPERS        ║
 *              ╚══════════════════════════════════════╝
 */




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



/**MAKE RESPONSES CATEGORY SCORE ARRAY:
 *
 * Makes the responses category score array from the responses score array
 * @param responsesScores 2D array containing the score of each response for each question
 * @param survey the survey struct containing the questions
 * @return returns the responses category score array
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










/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║  MAIN PROCESSING FUNCTIONS   ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/



/**GET RELATIVE PERCENTUAL FREQUENCIES ARRAY:
 *
 * Gets the relative percentual frequencies array from the survey
 * @param survey the survey struct containing the questions, likerts, respondees, and counts
 * @param filterMap the filter map array
 * @return returns the relative percentual frequencies array
 */
float ** getRpfArr(const Survey survey, int* filterMap) {
    int** summateArr = summateResponses(survey.respondees, survey.likerts, survey.counts, filterMap);
    float** rpfArr   = makeRPFArr(summateArr, survey.counts);

    free2dArr((void**)summateArr, survey.counts.numQuestions);

    return rpfArr;
}





/**GET CATEGORY SCORE ARRAY:
 *
 * Gets the category score array from the survey
 * @param survey the survey struct containing the questions, likerts, respondees, and counts
 * @param filterMap the filter map array
 * @return returns the category score array
 */
float** getCatScoreArr(const Survey survey, const int* filterMap) {
    int** responseScoreArr = computeResponsesScoreArr(survey, filterMap);
    float** catScoreArr = makeResponsesCatScoreArr(responseScoreArr, survey);

    free2dArr((void**)responseScoreArr, survey.counts.numQuestions);

    return catScoreArr;
}




/**GET AVG CATEGORY SCORES:
 *
 * Gets the average category scores from the category scores array
 * @param catScores the category scores array
 * @param counts the counts struct containing the number of questions, likerts, and respondents
 * @return returns the average category scores array
 */
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





