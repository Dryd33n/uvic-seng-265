//HEADER INCLUSIONS
#include "emalloc.h"
#include "dyn_survey.h"

//LIBRARY INCLUSIONS
#include <stdlib.h>
#include <stdio.h>





/**EMALLOC:
 *Allocates memory of size n and checks if the allocation was successful, returning a pointer to the block of memory
 *
 * @param n size of memory to be allocated
 * @return returns a pointer to a block of memory of size n
 */
void* emalloc(const size_t n) {
    void *p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}






/**FREE RESPONDEE:
 *Frees the memory allocated for the respondee tokens
 *
 * @param respondeeTokens the respondee tokens to be freed
 * @param numRespondeeTokens the number of respondee tokens
 */
void freeRespondee(const struct respondee respondee, const int numQuestions) {
    free(respondee.program);
    for (int i = 0; i < numQuestions; ++i) {
        free(respondee.response[i]);
    }
    free(respondee.response);
}





/**FREE FILTER:
 *Frees the memory allocated for the filter
 *
 * @param filter the filter to be freed
 */
void freeFilter(Filter filter) {
    free(filter.program);
}





/**FREE 2D ARRAY:
 *Frees the memory allocated for a 2D array
 *
 * @param arr the 2D array to be freed
 * @param arrDepth the depth of the 2D array
 */
void free2dArr(void** arr, const int arrDepth) {
    for (int i = 0; i < arrDepth; ++i) {
        free(arr[i]);
    }
    free(arr);
}





/**FREE QUESTIONS:
 *Frees the memory allocated for the questions
 *
 * @param survey the survey containing the questions to be freed
 */
void freeQuestions(Survey survey) {
    for (int i = 0; i < survey.counts.numQuestions; ++i) {
        free(survey.questions[i].question);
    }
    free(survey.questions);
}





/**FREE RESPONDEES:
 *Frees the memory allocated for the respondees
 *
 * @param survey the survey containing the respondees to be freed
 */
void freeRespondees(Survey survey){
    for (int i = 0; i < survey.counts.numRespondents; ++i) {
        freeRespondee(survey.respondees[i], survey.counts.numQuestions);
    }
    free(survey.respondees);
}





/**FREE SURVEY:
 *Frees the memory allocated for the survey
 *
 * @param survey the survey to be freed
 */
void freeSurvey(Survey survey) {
    freeQuestions(survey);                                          //free questions
    free2dArr((void**)survey.likerts, survey.counts.numLikerts);    //free likerts
    freeRespondees(survey);                                         //free respondees
}


