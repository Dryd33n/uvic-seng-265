#ifndef _DYN_SURVEY_H_
#define _DYN_SURVEY_H_
#include <stdbool.h>

/*              ╔══════════════════════════════════╗
 *              ║             STRUCTS              ║
 *              ╚══════════════════════════════════╝
 */

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
    char* program;      //respondee program
    bool fromCanada;    //is respondee from canada
    Date birthday;      //respondee birthday
    int age;
    char** response;    //respondee responses stored as strings
};
typedef struct respondee Respondee;



struct readQuestionRes {
    Question* questions;
    int numQuestions;
};
typedef struct readQuestionRes rqr;



struct readLikertRes {
    char** likerts;
    int numLikerts;
};
typedef  struct readLikertRes rlr;



struct counts {
    int numQuestions;
    int numLikerts;
    int numRespondents;
    int numFilteredOutRespondents;
    int numValidRespondents;
};
typedef struct counts Counts;



struct survey {
    Question* questions;
    Respondee* respondees;
    char ** likerts;
    Counts counts;
};
typedef struct survey Survey;

#endif
