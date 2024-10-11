#include <stdio.h>

#include "dyn_survey.h"

/** PRINT INTRO:
 *
 * Prints the survey intro with the number of respondents
 * @param numRespondents integer containing the number of respondents
 */
void printIntro(const int numRespondents) {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n\n");
    printf("NUMBER OF RESPONDENTS: %d\n", numRespondents);
}


void printQuestionsWithRPF(float** rpfArr, const Survey survey) {
    printf("\nFOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT");

    for (int i = 0; i < survey.counts.numQuestions; ++i) {
        printf("\n\n%s", survey.questions[i].question);    //print question

        for (int j = 0; j < survey.counts.numLikerts; ++j) {           //print each relative percentual frequency and likert
            printf("\n%.2f: ", rpfArr[i][j]);
            printf("%s", survey.likerts[j]);
        }
    }
    printf("\n");
}

void printResponseCatScores(const float** catScores, const int numRespondents) {
    printf("\nSCORES FOR ALL THE RESPONDENTS\n\n");

    for (int i = 0; i < numRespondents; ++i) {//for each respondents category scores
        printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",catScores[0][i],catScores[1][i],catScores[2][i],catScores[3][i],catScores[4][i]);
    }
}

void printAvgCatScores(const float * avgCatScores) {
    printf("\nAVERAGE SCORES PER RESPONDENT\n\n");
    printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",avgCatScores[0],avgCatScores[1],avgCatScores[2],avgCatScores[3],avgCatScores[4]);
}
