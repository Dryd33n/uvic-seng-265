//HEADER INCLUSIONS
#include "input_handling.h" //For structs
#include "emalloc.h"        //For allocation memory
#include "dyn_survey.h"     //For structs

//LIBRARY INCLUSIONS
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


//MACRO DEFINITIONS
#define MAX_LINE_LEN 3000





/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║       UTILITY FUNCTIONS      ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/



/**READ LINE:
 *Continuously reads from stdin until a non-comment line is found and stores it in the input string
 *
 * @param input the string which will be written to by stdin
 */
void readLine(char* input) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {//read from stdin until EOF
        input[strcspn(input, "\n")] = '\0';
        if(input[0] != '#') { //keep reading if line is a comment
            break; //stop reading from stdin when non comment line has been found
        }
    }
}





/**COUNT TOKENS:
 *Function to count number of tokens in a given string, adapted from dynamic_memory_example.c
 *given by Roberto Bittencourt
 *
 * @param string the string of which tokens will be counter
 * @param delim the delimiter which separates the tokens
 * @return the number of tokens
 */
int countTokens(const char * string, const char * delim) {
    int num_tokens = 0;
    char* stringToCount = emalloc(sizeof(char)* MAX_LINE_LEN);
    strcpy(stringToCount, string);

    /* get the first token from line */
    const char *token = strtok(stringToCount, delim);

    /* for every token in line, count it */
    while (token != NULL) {
        num_tokens++;

        /* get the next token from line or reach end of line */
        token = strtok(NULL, delim);
    }

    free(stringToCount);

    return num_tokens;
}










/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║   SURVEY READING FUNCTIONS   ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/

/*              ╔══════════════════════════════════╗
 *              ║  RESPONDEE TOKENIZATION HELPERS  ║
 *              ╚══════════════════════════════════╝
 */



/**TOKENIZE RESPONDEE:
 *Converts the line from stdin to a char array containing the tokens
 *
 * @param buffer the string to be tokenized
 * @param numTokens the number of tokens in the string
 * @return the char array containing the tokens
 */
char** tokenizeRespondee(char* buffer, const int numTokens) {
    char** respondeeTokens = emalloc(sizeof(char *) * numTokens); //allocate memory for tokens

    /* TOKENIZATION */
    char* token = strtok(buffer, ","); //get first token
    int i = 0;
    while(token != NULL) {
        token[strcspn(token, "\n")] = '\0';                    //remove newline character from token
        respondeeTokens[i] = emalloc(sizeof(char) * (strlen(token)+1)); //allocate memory for token
        strcpy(respondeeTokens[i],token);                               //store token in array

        token = strtok(NULL, ","); //get token
        i++;
    }



    return respondeeTokens;
}





/**TOKENIZE DATE:
 *Converts the date string to a Date struct
 *
 * @param respondee_token the string containing the date
 * @return the Date struct containing the date
 */
Date tokenizeDate(char * respondee_token) {
    const char* delim =  "-";

    Date birthday;                                      //create a new date struct
    birthday.day = birthday.month = birthday.year = -1; //set default values

    /* TOKENIZATION */
    const char* token = strtok(respondee_token, delim); //get first token
    for (int i = 0; i < 3; ++i) {
        if(i == 0) {                        //First token, store in year
            birthday.year = atoi(token);    //convert token to integer and store in year
        }else if (i == 1) {                 //Second token, store in month
            birthday.month = atoi(token);   //convert token to integer and store in month
        }else if (i == 2) {                 //Third token, store in day
            birthday.day = atoi(token);     //convert token to integer and store in day
        }

        token = strtok(NULL, delim);  //get next token
    }

    return birthday;
}





/**CALCULATE AGE:
 *Calculates the age of the respondee based on the birthdate and current date
 *
 * @param birthdate the birthdate of the respondee
 * @return the age of the respondee
 */
int calculateAge(Date birthdate) {
    char* dateStr = emalloc(sizeof(char)*16);                                        //allocate memory for date string
    const time_t current_time = time(NULL);                                          //get current time
    strftime(dateStr, 32, "%Y-%m-%d", localtime(&current_time)); //store current date in dateStr
    const Date curDate = tokenizeDate(dateStr);                                      //convert current date to struct
    free(dateStr);                                                                   //free date string

    int age = curDate.year - birthdate.year; //base age calculation on year difference

    /* Decrease age if current date is before birthday */
    if(curDate.month < birthdate.month ||  ((curDate.month == birthdate.month) && (curDate.day < birthdate.day))) {
        age--;
    }

    return age;
}





/**CONSTRUCT RESPONDEE:
 *Constructs a respondee struct from the input string
 *
 * @param buffer the string containing the respondee information
 * @return the constructed respondee struct
 */
Respondee constructRespondent(char* buffer) {
    Respondee respondee; //create a new respondee struct

    const char delim[2] = ",";                                              //delimiter for tokens
    const int numRespondeeTokens = countTokens(buffer,delim);          //count number of tokens
    char** respondeeTokens = tokenizeRespondee(buffer, numRespondeeTokens); //tokenize the string


    respondee.program = emalloc(sizeof(char) * (strlen(respondeeTokens[0])+1)); //allocate memory for program
    strcpy(respondee.program, respondeeTokens[0]);                              //store program in respondee

    respondee.fromCanada = strcmp(respondeeTokens[1], "yes") == 0; //convert fromCanada to boolean and store

    respondee.birthday = tokenizeDate(respondeeTokens[2]); //convert birthday to Date struct and store

    respondee.age = calculateAge(respondee.birthday); //calculate age and store

    respondee.response = emalloc(sizeof(char *) * (numRespondeeTokens-3)); //allocate memory for responses
    for (int i = 0; i < numRespondeeTokens-3; ++i) {
        respondee.response[i] = emalloc(sizeof(char)*(strlen(respondeeTokens[i+3])+1)); //allocate memory for response
        strcpy(respondee.response[i],respondeeTokens[i+3]); //store response in respondee
    }

    free2dArr((void**)respondeeTokens, numRespondeeTokens); //free memory allocated for tokens
    return respondee;
}






/*              ╔═══════════════════════════════════╗
 *              ║   MAIN SURVEY READING FUNCTIONS   ║
 *              ╚═══════════════════════════════════╝
 */


/**READ CONFIG:
 *Reads the config from stdin and stores it in an integer array
 *
 * @return the integer array containing the config
 */
int* readConfig() {
     const char* delim = ",";
     char* buffer = emalloc(sizeof(char)*MAX_LINE_LEN);  //buffer to hold line
     readLine(buffer);                                   //store stdin line to buffer

     const int configTokens = countTokens(buffer, delim);    //number of tokens
     int * configArr = emalloc(sizeof(int) * configTokens);       //integer array to store config tokens


     const char* token = strtok(buffer, delim);  //get the first token from the buffer
     int i = 0;                                  //counter to assign token into array

     while (token != NULL) {
         configArr[i] = atoi(token); //stores integer conversion of token into array
         token = strtok(NULL, delim);//gets the next token
         i++;
     }



     free(buffer);
    return configArr;
}





/**READ QUESTIONS:
 *Reads the questions from stdin and stores them in a Question struct array
 *
 * @return the Question array containing the questions
 */
rqr readQuestions() {
    const char* delim = ";";                          //delimiter for questions
    char* buffer = emalloc(sizeof(char)*MAX_LINE_LEN);//allocate buffer to store line
    readLine(buffer);                                 //store stdin line to buffer

    const int numQuestions = countTokens(buffer, delim);       //count number of questions
    Question* questions = emalloc(sizeof(Question) * numQuestions); //allocate array of questions


    /* TOKENIZATION */
    const char* token = strtok(buffer, delim); //get first token
    int i = 0;
    while(token != NULL) {
        Question curQuestion;                                             //create a new question struct
        curQuestion.question = emalloc(sizeof(char) * (strlen(token)+1)); //allocate memory for question

        strcpy(curQuestion.question, token); //Set question value
        curQuestion.category[0] = token[0];  //Set question category
        curQuestion.category[1] = '\0';      //Ensure null termination For category

        curQuestion.directDirection = true;  //set default value

        questions[i++] = curQuestion;        //store question in array

        token = strtok(NULL, delim);         //get next token
    }


    free(buffer); //Free memory allocated for buffer

    rqr res;                        //create a result struct to be returned containing questions and number of questions
    res.questions = questions;      //set questions
    res.numQuestions = numQuestions;//set number of questions
    return res;                     //return structs
}





/**READ DIRECTIONS:
 *Reads the question direction from stdin and stores them in the Question struct array
 *
 * @param questions the array of questions to store the directions
 */
void readDirections(Question* questions) {
    const char* delim = ";";                           //delimiter for directions
    char* buffer = emalloc(sizeof(char)*MAX_LINE_LEN); //allocate buffer to store line
    readLine(buffer);                                  //store stdin line to buffer


    /* TOKENIZATION */
    const char* token = strtok(buffer, delim); //get first token
    int i = 0;
    while (token != NULL) {
        if(strcmp(token, "Direct")==0) {         //convert token to boolean
            questions[i].directDirection = true;
        }else if(strcmp(token, "Reverse")==0) {
            questions[i].directDirection = false;
        }

        i++;
        token = strtok(NULL, delim); // get next token
    }

    free(buffer); //Free memory allocated for buffer
}





/**READ LIKERTS:
 *Reads the likerts from stdin and stores them in a char array
 *
 * @return the char array containing the likerts and count of likerts in a struct
 */
rlr readLikerts() {
    const char* delim = ",";                           //delimiter for likerts
    char* buffer = emalloc(sizeof(char)*MAX_LINE_LEN); //allocate buffer to store line
    readLine(buffer);                                  //store stdin line to buffer

    const int numLikerts = countTokens(buffer, delim);  //count number of likerts

    char** likerts = emalloc(sizeof(char *) * numLikerts);   //allocate array of likerts

    /* TOKENIZATION */
    const char* token = strtok(buffer, delim);  //get first token
    int i = 0;
    while (token != NULL) {
        likerts[i] = emalloc(sizeof(char) * (strlen(token)+1)); //allocate memory for likert
        strcpy(likerts[i], token);                              //store likert in array

        token = strtok(NULL, delim);// get next token
        i++;
    }

    free(buffer);   //Free memory allocated for buffer

    rlr res;                    //create a result struct to be returned containing likerts and number of likerts
    res.likerts = likerts;      //set likerts
    res.numLikerts = numLikerts;//set number of likerts
    return res;                 //return result struct
}





/**READ NUM RESPONSES:
 *Reads the number of responses from stdin
 *
 * @return the number of responses
 */
int readNumResponses() {
    char* buffer =  emalloc(sizeof(char)*MAX_LINE_LEN); //buffer to store line
    readLine(buffer);                                   //store stdin line to buffer

    const int result = atoi(buffer); //convert buffer to integer
    free(buffer);                    //free buffer

    return result;                   //return integer
}





/**READ RESPONSES:
 *Reads the responses from stdin and stores them in a Respondee struct array
 *
 * @param numResponses the number of responses to read
 * @return the Respondee array containing the responses
 */
Respondee* readResponses(const int numResponses) {
    int i = 0;
    Respondee* respondees = emalloc(sizeof(Respondee) * numResponses);

    while ( i < numResponses) {                            //for each input line containing response information
        char* buffer = emalloc(sizeof(char)*MAX_LINE_LEN); //allocate buffer to store line
        fgets(buffer, MAX_LINE_LEN, stdin);     //store stdin line to buffer
        if(buffer[0] != '#') {                           //if line isn't a comment
            respondees[i] = constructRespondent(buffer); //send line off to construct respondent
            i++;
        }

        free(buffer);  //free buffer
    }

    return respondees;
}





/**READ SURVEY:
 *Reads the survey from stdin and stores it in a Survey struct
 *
 * @return the Survey struct containing the survey information
 */
Survey readSurvey() {
    Survey survey;

    /* READ QUESTIONS */
    const rqr resQ              = readQuestions();  //get questions array and number of questions
    survey.questions            = resQ.questions;   //store questions in survey
    survey.counts.numQuestions  = resQ.numQuestions;//store number of questions in survey

    /* READ DIRECTIONS */
    readDirections(survey.questions); //modify questions array to include directions

    /* READ LIKERTS */
    const rlr resL           = readLikerts();  //get likerts array and number of likerts
    survey.likerts           = resL.likerts;   //store likerts in survey
    survey.counts.numLikerts = resL.numLikerts;//store number of likerts in survey

    /* READ NUM RESPONSES */
    survey.counts.numRespondents            = readNumResponses();           //store number of respondents in survey
    survey.counts.numFilteredOutRespondents = 0;                            //set default value for filtered out respondents
    survey.counts.numValidRespondents       = survey.counts.numRespondents; //set default value for valid respondents

    /* READ RESPONSES */
    survey.respondees = readResponses(survey.counts.numRespondents); //store respondees in survey

    return survey;
}










/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║  SURVEY FILTERING FUNCTIONS  ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/


/*              ╔══════════════════════════════════╗
 *              ║        FILTERING HELPERS         ║
 *              ╚══════════════════════════════════╝
 */



/**NEW BLANK FILTER:
 *Creates a new blank filter struct with all values set to false or -1
 *
 * @return the new blank filter
 */
Filter newBlankFilter(void) {
    Filter filter;

    filter.filterProgram = false;
    filter.filterFromCan = false;
    filter.filterAge = false;

    filter.program = NULL;
    filter.fromCan = NULL;
    filter.minAge = -1;
    filter.maxAge = -1;

    return filter;
}




/**EDIT FILTER:
 *Edits the filter struct based on the input string
 *
 * @param filter the filter struct to be edited
 * @param filterStr the string containing the filter information
 */
void editFilter(Filter *filter, char* filterStr) {
    int filterVal = -1; //default value for filter val, used to determine which filter is being edited
    const char* delim = ",";

    /* TOKENIZATION */
    const char* token = strtok(filterStr, delim);
    int i = 0;
    while(token != NULL) {

        if(i == 0) {// First token determines which filter is being edited
            filterVal = atoi(token);
        }else {
            switch (filterVal) {
                case 0: //filter program
                    filter->filterProgram = true;                               //set filter program to true
                    filter->program = emalloc(sizeof(char)*(strlen(token)+1));  //allocate memory for program
                    strcpy(filter->program, token);                             //store program in filter
                    return;
                case 1: //filter fromCan
                    filter->filterFromCan = true;               //set filter fromCan to true
                    filter->fromCan = strcmp("yes", token)==0;  //convert token to boolean and store in fromCan
                    return;                                     //return after setting fromCan
                case 2: //filter age
                    filter->filterAge = true;         //set filter age to true
                    if(i==1) {                        //if first token, store in minAge
                        filter->minAge = atoi(token); //convert token to integer and store in minAge
                    }else {                           //if second token, store in maxAge
                        filter->maxAge = atoi(token); //convert token to integer and store in maxAge
                        return;
                    }
                default:
            }
        }

        i++;
        token = strtok(NULL, delim); //get next token
    }
}





/**FILTER PROGRAM:
 *Edits the filter map to filter out respondees who are not in the specified program
 *
 * @param filterMap the filter map to be modified
 * @param program the program to filter by
 * @param survey the survey containing the respondees
 */
void filterProgram(int* filterMap, const char* program, const Survey survey) {
    for (int i = 0; i < survey.counts.numRespondents; ++i) {                     //for each respondee
        if(strcmp(program, survey.respondees[i].program)!=0){ filterMap[i] = 0;} //if respondee is not in program, set filterMap to 0
    }
}





/**FILTER FROM CAN:
 *Edits the filter map to filter out respondees who are not from Canada
 *
 * @param filterMap the filter map to be modified
 * @param fromCan the boolean value to filter by
 * @param survey the survey containing the respondees
 */
void filterFromCan(int* filterMap, bool fromCan, Survey survey) {
    for (int i = 0; i < survey.counts.numRespondents; ++i) {                //for each respondee
        if(fromCan != survey.respondees[i].fromCanada){ filterMap[i] = 0;}  //if respondee is not from Canada, set filterMap to 0
    }
}





/** FILTER AGE:
 *Edits the filter map to filter out respondees who are not within the specified age range
 *
 * @param filterMap the filter map to be modified
 * @param minAge the minimum age to filter by
 * @param maxAge the maximum age to filter by
 * @param survey the survey containing the respondees
 */
void filterAge(int* filterMap, const int minAge, const int maxAge, const Survey survey) {
    for (int i = 0; i < survey.counts.numRespondents; ++i) { //for each respondee
        if(!(minAge <= survey.respondees[i].age              //if respondee is not above minAge
            && survey.respondees[i].age <= maxAge) ) {       //or below maxAge, set filterMap to 0
            filterMap[i] = 0;
        }
    }
}





/** CREATE FILTER MAP:
 * Creates a filter map based on the filter input and respondee information
 *
 * @param survey the survey to be filtered
 * @return filterMap the filter map to be modified
 */
int* createFilterMap(Survey* survey) {
    Filter filter = newBlankFilter(); //create a new blank filter
    int filteredOutRespondents = 0;   //default value for filtered out respondents


    int* filterMap = emalloc(sizeof(int)*survey->counts.numRespondents); //allocate memory for filter map
    for (int j = 0; j < survey->counts.numRespondents; ++j) {            //initialize filter map to all 1s
        filterMap[j] = 1;
    }

    /* TOKENIZATION */
    int i = 0;
    while(i < 3) {
        char buffer[MAX_LINE_LEN]="-1"; //set default value for buffer
        readLine(buffer);               //store stdin line to buffer

        if(strcmp(buffer, "-1")==0) {   //if buffer did not get modified since at EOF
            break;
        }

        editFilter(&filter, buffer);   //if buffer was modified, filter was found, then edit filter based on buffer

        i++;
    }

    if(!filter.filterProgram && !filter.filterFromCan && !filter.filterAge) { //if no filter was found, return filterMap
        return filterMap;
    }

    if(filter.filterProgram) {
        filterProgram(filterMap, filter.program, *survey);         //if program filter was found filter by program
    }

    if(filter.filterFromCan) {
        filterFromCan(filterMap, filter.fromCan, *survey);         //if fromCan filter was found filter by fromCan
    }

    if(filter.filterAge) {
        filterAge(filterMap, filter.minAge, filter.maxAge, *survey);//if age filter was found filter by age
    }

    for (int i = 0; i < survey->counts.numRespondents; ++i) {       //count number of filtered out respondents
        if(filterMap[i]==0) filteredOutRespondents++;
    }

    survey->counts.numFilteredOutRespondents = filteredOutRespondents;//set number of filtered out respondents
    survey->counts.numValidRespondents = survey->counts.numRespondents - filteredOutRespondents;//set number of valid respondents

    freeFilter(filter); //free filter struct

    return filterMap;
}

