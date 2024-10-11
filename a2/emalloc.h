#ifndef _EMALLOC_H_
#define _EMALLOC_H_

#include "dyn_survey.h"
void *emalloc(size_t);

void freeRespondeeTokens(char **respondeeTokens, int numRespondeeTokens);
void freeRespondee(Respondee respondee, int numQuestions);
void freeSummateArr(int** sumArr, int numQuestions);
void free2dArr(void** arr, int arrDepth);

#endif
