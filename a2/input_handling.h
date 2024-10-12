#ifndef _INPUT_HANDLING_H_
#define _INPUT_HANDLING_H_

/* add your include and prototypes here*/
#include <stdio.h>
#include <string.h>
#include "dyn_survey.h"

int *readConfig();

Survey readSurvey();
int* createFilterMap(Survey* survey);


struct filter {
    bool filterProgram;
    char* program;

    bool filterFromCan;
    bool fromCan;

    bool filterAge;
    int minAge;
    int maxAge;
};
typedef struct filter Filter;

#endif
