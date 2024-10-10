#ifndef _INPUT_HANDLING_H_
#define _INPUT_HANDLING_H_

/* add your include and prototypes here*/
#include <stdio.h>
#include <string.h>

int *readConfig();
Question* readQuestions();
void readDirections(Question * questions);
char** readLikerts();
int readNumResponses();
Respondee* readResponses(int numResponses);

#endif
