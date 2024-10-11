#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"
#include "dyn_survey.h"

void *emalloc(const size_t n) {
    void *p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}


void freeRespondee(const struct respondee respondee, const int numQuestions) {
    free(respondee.program);
    for (int i = 0; i < numQuestions; ++i) {
        free(respondee.response[i]);
    }
    free(respondee.response);
}


void freeRespondeeTokens(char **respondeeTokens, int numRespondeeTokens) {
    for (int j = 0; j < numRespondeeTokens; ++j) {
        free(respondeeTokens[j]);
    }
    free(respondeeTokens);
}


void freeSummateArr(int** sumArr, const int numQuestions) {
    for (int i = 0; i < numQuestions; ++i) {
        free(sumArr[i]);
    }
    free(sumArr);
}

void free2dArr(void** arr, const int arrDepth) {
    for (int i = 0; i < arrDepth; ++i) {
        free(arr[i]);
    }
    free(arr);
}