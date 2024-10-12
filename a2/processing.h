#ifndef _PROCESSING_H_
#define _PROCESSING_H_
#include "dyn_survey.h"

/* add your include and prototypes here*/

float ** getRpfArr(Survey survey, int* filterMap);
float** getCatScoreArr(Survey survey, const int* filterMap);
double* getAvgCatScores(float** catScores, Counts counts);
#endif
