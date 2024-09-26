#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RESPONDENTS 5
#define NUM_QUESTIONS 38
#define NUM_LIKERTS 6

#define MAX_LINE_LEN 4096


/**
 * struct to hold question, question direction and question category
 */
struct Question {
    char question[128]; //question string;
    _Bool directDirection; //true = direct, false = reverse, true = default
    char category[2];   //category: C,I,G,U,P
};



/**
 *                           ╔════════════════════════╗
 *                           ║   PRINTING FUNCTIONS   ║
 *                           ╚════════════════════════╝
 *///

/**
 * Prints the survey intro with the number of respondents
 * @param numRespondents integer containing the number of respondents
 */
void printIntro(const int numRespondents) {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n\n");
    printf("NUMBER OF RESPONDENTS: %d\n\n", numRespondents);
}



void printQuestionsWithRPF(struct Question * questions, float(* rpfArr)[NUM_LIKERTS], char(* likerts)[32]) {
    printf("FOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT\n");

    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        printf("\n%s", questions[i].question);

        for (int j = 0; j < NUM_LIKERTS; ++j) {
            printf("\n%.2f: ", rpfArr[i][j]);
            printf("%s", likerts[j]);
        }
    }
}


/**
 * Continuously reads from stdin until a non comment 'char[0] != '#' line is found.
 * @param input the string for which the line will be read into.
 */
void readLine(char input[MAX_LINE_LEN]) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {
        if(input[0] != '#') {
            break; //stop reading from stdin when non comment line has been found
        }
    }
}







/**
 *                       ╔════════════════════════════╗
 *                       ║   TOKENIZATION FUNCTIONS   ║
 *                       ╚════════════════════════════╝
 *///

/**
 * Reads the config line from stdin and store it into array of ints
 * @param arr the 4 bit configuration array
 */
void readConfig(int * arr) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ",";
    int i = 0;

    readLine(input);

    const char *token = strtok(input, delim); // get the first token

    while( token != NULL ) {    // walk through rest of tokens
        arr[i++] = atoi(token); //convert each config value to an int
        token = strtok(NULL, delim);
    }
}



/**
 * Reads line of set of questions and stores it in an array of Question structs
 * @param questions array of Question structs
 */
void readQuestions(struct Question * questions) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ";";
    int i = 0;

    readLine(input);

    input[strcspn(input, "\n")] = '\0';//remove newline character

    const char *token = strtok(input, delim); //get first token

    while (token != NULL) { // walk through rest of token
        struct Question curQuestion; // initialize question struct


        strncpy(curQuestion.question, token, sizeof(curQuestion.question)); // Assign question
        curQuestion.question[sizeof(curQuestion.question) -1] = '\0'; // Ensure null termination

        curQuestion.category[0] = token[0]; // Assign question category
        curQuestion.category[1] = '\0'; // Ensure null termination

        curQuestion.directDirection = true; //set default value

        questions[i++] = curQuestion;
        token = strtok(NULL, delim);
    }
}



/**
 * Reads line #3 Containing direction information and stores it into Question struct array
 * @param questions Array of Question structs for which the direction will be assigned
 */
void readDirections(struct Question * questions) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ";";
    int i = 0;

    readLine(input);

    const char *token = strtok(input, delim);

    while (token != NULL) {
        if(strcmp(token, "Direct")==0) {
            questions[i].directDirection = true;
        }else if(strcmp(token, "Reverse")==0) {
            questions[i].directDirection = false;
        }

        i++;
        token = strtok(NULL, delim);
    }


}



/**
 * Reads line #4 containing likerts and stores them into the given likert array
 * @param likerts array of strings to store the 6 likerts
 */
void readLikerts(char(* likerts)[32]) {
    char input[MAX_LINE_LEN];
    const char delim[2] = ",";
    int i = 0;

    readLine(input);

    const char *token = strtok(input, delim);

    while (token != NULL) {
        strcpy(likerts[i++], token);//copy each likert into array of likerts
        token = strtok(NULL, delim);
    }
}



/**
 * Converts a given string containing a likert into its respective value as an int based on the direction of a question
 * @param likertStr the string containing the given likert to convert to int
 * @param question the question for which the given likert is responding to, used to determine question direction
 * @param likerts the array of possible likerts
 * @return returns an integer 1,...,6 from given likertStr
 */
int likertToVal(const char * likertStr,
                const struct Question question,
                const char(* likerts)[32])
{
    for (int i = 0; i < 6; ++i) {//walk through all possible options for likerts
        if(strcmp(likertStr, likerts[i]) == 0) {//compare likert[i] to give likert to see if they match
            if(question.directDirection){
                return i+1;
            }
            return 6-i;
        }
    }
    return -1;  // default case if likert is not found
}



/**
 * Parses each response line and stores the response values in a unique row of a int matrix.
 * @param responseArr give row of response matrix to be filled
 * @param input string containing response + respondee information
 * @param questions array of questions
 * @param likerts array of all likerts
 */
void tokenizeResponse(int * responseArr,
                      char * input,
                      const struct Question * questions,
                      const char(* likerts)[32])
{
    const char delim[2] = ",";
    int i = 0;

    const char *token = strtok(input, delim);

    while (token != NULL) {
        if(i > 2) {//skip respondee info
            responseArr[i-3]= likertToVal(token, questions[i-3], likerts);//set value to array from likert
        }

        token = strtok(NULL, delim);
        i++;
    }
}


/**
 * Reads all responses them and process them for further tokenization
 * @param responseArr the response int matrix to be filled
 * @param questions the array of all questions
 * @param likerts the array of all likerts
 * @return returns and integer containing the amount of respondents to the survey
 */
int readResponses(int(* responseArr)[MAX_RESPONDENTS],
                  const struct Question * questions,
                  const char(* likerts)[32])
{
    char input[MAX_LINE_LEN];
    int i = 0;

    while (fgets(input, MAX_LINE_LEN, stdin)!=NULL) {//continuously read from stdin
        if(input[0] != '#') {//ignore line if it is a comment line and keep reading
            tokenizeResponse(responseArr[i], input, questions, likerts);//send off response line for tokenization

            for (int j = 0; j < 38; ++j) {
                printf("%d",responseArr[i][j]);
            }
            i++;
        }
    }

    return i;
}








/**
 *                           ╔══════════════════════════════╗
 *                           ║   INITIALIZATION FUNCTIONS   ║
 *                           ╚══════════════════════════════╝
 *///


void initializeEmptyResponses(int(* responseArr)[MAX_RESPONDENTS]) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < MAX_RESPONDENTS; ++j) {
            responseArr[i][j] = 0;
        }
    }
}

void initializeEmptyResponsesRPF(float(* responseRPFArr)[NUM_LIKERTS]) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < NUM_LIKERTS; ++j) {
            responseRPFArr[i][j] = 0;
        }
    }
}



void summateResponses(int responseArr[NUM_QUESTIONS][MAX_RESPONDENTS],
                      int(* responseSums)[NUM_LIKERTS],
                      const struct Question * questions)
{
    for (int i = 0; i < NUM_QUESTIONS; ++i) {           //for each question
        bool direct = questions[i].directDirection;

        for (int j = 0; j < MAX_RESPONDENTS; ++j) {     //for each respondent response
            if(direct) {
                responseSums[i][responseArr[i][j]]++;   //
            }else {
                responseSums[i][7-responseArr[i][j]]++;
            }
        }
    }
}

void calculateRPF(const int num_respondents,
                  const int(* responseSums)[NUM_LIKERTS],
                  float(* responses_rpf)[NUM_LIKERTS])
{
    if(num_respondents == 0) exit(133);

    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < NUM_LIKERTS; ++j) {
            responses_rpf[i][j] = ((float)responseSums[i][j] / (float)num_respondents)*100;
        }
    }
}


int main() {
    int config[4];                  //Configuration
    struct Question questions[NUM_QUESTIONS];  //Array Of Questions
    char likerts[NUM_LIKERTS][32];
    int responses[NUM_QUESTIONS][MAX_RESPONDENTS];
    int responsesSum[NUM_QUESTIONS][NUM_LIKERTS];
    float responsesRPF[NUM_QUESTIONS][NUM_LIKERTS];
    int numRespondents;

    initializeEmptyResponses(responses);

    readConfig(config);
    readQuestions(questions);
    readDirections(questions);
    readLikerts(likerts);

    if(config[0]==1) {
        numRespondents = 0;
        initializeEmptyResponsesRPF(responsesRPF);
        printIntro(numRespondents);
        printQuestionsWithRPF(questions, responsesRPF, likerts);
    }else{
        
        if(config[1]==1) {
            numRespondents = readResponses(responses, questions, likerts);
            summateResponses(responses,responsesSum, questions);
            calculateRPF(numRespondents, responsesSum, responsesRPF);
            printIntro(numRespondents);
            printQuestionsWithRPF(questions, responsesRPF, likerts);
        }
    }

    return 0;
}
