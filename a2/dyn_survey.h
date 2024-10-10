#ifndef _DYN_SURVEY_H_
#define _DYN_SURVEY_H_
#include <stdbool.h>

/* add your library includes, constants and typedefs here*/
struct question {
    char* question;     //question content string;
    _Bool directDirection;  //true = direct, false = reverse, true = default
    char category[2];       //category: C,I,G,U,P
};
typedef struct question Question;

struct date {
    int year;
    int month;
    int day;
};

typedef struct date Date;

struct respondee {
    char* program;       //respondee program
    bool fromCanada;        //is respondee from canada
    Date birthday;      //respondee birthday
    char** response;  //respondee responses stored as strings
};
typedef struct respondee Respondee;

#endif
