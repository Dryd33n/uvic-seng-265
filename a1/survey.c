#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RESPONDENTS 5
#define NUM_QUESTIONS 38
#define NUM_CATEGORIES 5
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

struct Respondee {
    char program[32]; //respondee program
    bool fromCanada;
    char birthday[16];
    char response[38][64];
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
    printf("NUMBER OF RESPONDENTS: %d\n", numRespondents);
}



void printQuestionsWithRPF(struct Question * questions, float(* rpfArr)[NUM_LIKERTS], char(* likerts)[32]) {
    printf("\nFOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT");

    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        printf("\n\n%s", questions[i].question);

        for (int j = 0; j < NUM_LIKERTS; ++j) {
            printf("\n%.2f: ", rpfArr[i][j]);
            printf("%s", likerts[j]);
        }
    }
    printf("\n");
}


/**
 * Continuously reads from stdin until a non comment 'char[0] != '#' line is found.
 * @param input the string for which the line will be read into.
 */
void readLine(char input[MAX_LINE_LEN]) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {
        input[strcspn(input, "\n")] = '\0';
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

    char *token = strtok(input, delim);

    while (token != NULL) {
        strcpy(likerts[i++], token);//copy each likert into array of likerts
        token = strtok(NULL, delim);
    }
}



/**
 * Converts a given string containing a likert into its respective value as an int
 * @param question the question for which the given likert is responding to, used to determine question direction
 * @return returns an integer 1,...,6 from given likertStr
 */
int likertToVal(const char * likertStr,
                const char(* likerts)[32])
{
    char cleanLikert[32];
    strcpy(cleanLikert,likertStr);
    cleanLikert[strcspn(cleanLikert, "\n")] = 0;


    for (int i = 0; i < 6; ++i) {//walk through all possible options for likerts
        if(strcmp(cleanLikert, likerts[i]) == 0) {//compare likert[i] to give likert to see if they match
            return i+1;
        }
    }
    return -1;  // default case if likert is not found
}



void constructRespondent(char input[4096], struct Respondee *respondee) {
    const char delim[2] = ",";
    int i = 0;

    const char *token = strtok(input, delim);

     while (token != NULL) {
         if(i > 2) {
             strncpy(respondee->response[i-3], token, 32);
         }else if(i==2) {
             strcpy(respondee->birthday, token);
         }else if(i==1) {
             if(strcmp("yes", token) == 0) {
                respondee->fromCanada = true;
             }else {
                 respondee->fromCanada = false;
             }
         }else if(i==0){
             strcpy(respondee->program, token);
         }

         token = strtok(NULL, delim);
         i++;
     }
}



int readResponses(struct Respondee respondees[MAX_RESPONDENTS]) {
    int i = 0;

     while ( i < MAX_RESPONDENTS) {
         char input[MAX_LINE_LEN*5];
         fgets(input, sizeof(input), stdin);

         if(input[0] != '#') {//ignore line if it is a comment line and keep reading
             constructRespondent(input, &respondees[i]);
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



void summateResponses(const struct Respondee respondees[5], const int numRespondents, int(* responsesSum)[6], const char(* likerts)[32]) {
    for (int i = 0; i < numRespondents; ++i) {
        for (int j = 0; j < NUM_QUESTIONS; ++j) {
            const int likertVal = likertToVal(respondees[i].response[j], likerts);
            responsesSum[j][likertVal-1]++;
        }
    }



}

void computeRPFArr(float(* responsesRPF)[6], int(* responsesSum)[6], int numRespondants) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < 6; ++j) {
            responsesRPF[i][j] = ((float)responsesSum[i][j] / (float)numRespondants) * 100;
        }
    }
}

void computeResponsesScoreArr(struct Respondee * respondees, int numRespondents, int(* responseScores)[NUM_QUESTIONS], struct Question * questions,  const char(* likerts)[32]) {
    for (int i = 0; i < numRespondents; ++i) {
        for (int j = 0; j < NUM_QUESTIONS; ++j) {
            int likertVal = likertToVal(respondees[i].response[j], likerts);
            int likertValDirected = likertVal;
            if(!questions[j].directDirection) {
                likertValDirected = 7 - likertVal;
            }
            responseScores[i][j] = likertValDirected;
        }
    }
}

void computeResponsesCatScoreArr(float(* responsesCatScores)[5], const int(* responsesScores)[38], const struct Question * questions, const int numRespondents) {

    for (int i = 0; i < numRespondents; ++i) {
        int cCount=0, iCount=0, gCount=0, uCount=0, pCount=0;
        int cSum=0, iSum=0, gSum=0, uSum=0, pSum = 0;

        for (int j = 0; j < NUM_QUESTIONS; ++j) {
            const char *category = questions[j].category;

            if(strcmp("C",category) == 0) {
                cCount++;
                cSum +=responsesScores[i][j];
            }else if(strcmp("I",category) == 0) {
                iCount++;
                iSum +=responsesScores[i][j];
            }else if(strcmp("G",category) == 0) {
                gCount++;
                gSum +=responsesScores[i][j];
            }else if(strcmp("U",category) == 0) {
                uCount++;
                uSum +=responsesScores[i][j];
            }else if(strcmp("P",category) == 0) {
                pCount++;
                pSum +=responsesScores[i][j];
            }else {
                printf("error");
            }
        }
        responsesCatScores[i][0] = (float)cSum / cCount;
        responsesCatScores[i][1] = (float)iSum / iCount;
        responsesCatScores[i][2] = (float)gSum / gCount;
        responsesCatScores[i][3] = (float)uSum / uCount;
        responsesCatScores[i][4] = (float)pSum / pCount;
    }

}

void printResponseCatScores(float(* catScores)[5], int numRespondents) {
        printf("\nSCORES FOR ALL THE RESPONDENTS\n\n");

    for (int i = 0; i < numRespondents; ++i) {
        printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",catScores[i][0],catScores[i][1],catScores[i][2],catScores[i][3],catScores[i][4]);
    }
}

void computerAvgCatScores(float * avgCatScore, float(* catScores)[NUM_CATEGORIES], int numRespondents) {
    for (int i = 0; i < NUM_CATEGORIES; ++i) {
        float catSum = 0;
        for (int j = 0; j < numRespondents; ++j) {
            catSum += catScores[j][i];
        }
        avgCatScore[i] = catSum / (float)numRespondents;
    }
}

void printAvgCatScores(float * avgCatScores) {
    printf("\nAVERAGE SCORES PER RESPONDENT\n\n");
    printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",avgCatScores[0],avgCatScores[1],avgCatScores[2],avgCatScores[3],avgCatScores[4]);
}

int main() {
    int config[4];                  //Configuration
    struct Question questions[NUM_QUESTIONS];  //Array Of Questions
    char likerts[NUM_LIKERTS][32];
    int responses[NUM_QUESTIONS][MAX_RESPONDENTS];
    float responsesRPF[NUM_QUESTIONS][NUM_LIKERTS];
    int numRespondents = 0;

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
        struct Respondee respondents[MAX_RESPONDENTS];
        numRespondents = readResponses(respondents);
        printIntro(numRespondents);

        if(config[1]==1) {
            int responsesSum[NUM_QUESTIONS][NUM_LIKERTS];
            summateResponses(respondents, numRespondents, responsesSum, likerts);
            computeRPFArr(responsesRPF, responsesSum, numRespondents);
            printQuestionsWithRPF(questions, responsesRPF, likerts);
        }


        if(config[2]==1 || config [3] == 1) {
            int responsesScores[numRespondents][NUM_QUESTIONS];
            float responsesCatScores[numRespondents][NUM_CATEGORIES];
            computeResponsesScoreArr(respondents, numRespondents, responsesScores, questions, likerts);
            computeResponsesCatScoreArr(responsesCatScores, responsesScores, questions, numRespondents);

            if(config[2] == 1) {
                printResponseCatScores(responsesCatScores, numRespondents);
            }

            if(config[3] == 1) {
                float avgCatScores[NUM_CATEGORIES];
                computerAvgCatScores(avgCatScores, responsesCatScores, numRespondents);
                printAvgCatScores(avgCatScores);
            }


        }
    }

    return 0;
}
