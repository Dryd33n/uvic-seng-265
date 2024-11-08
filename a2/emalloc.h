#ifndef _EMALLOC_H_
#define _EMALLOC_H_

#include "dyn_survey.h"
#include "input_handling.h"

void *emalloc(size_t);
void freeRespondee(Respondee respondee, int numQuestions);
void free2dArr(void** arr, int arrDepth);
void freeSurvey(Survey survey);
void freeFilter(Filter filter);

#endif
