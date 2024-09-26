#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RESPONDENTS     5
#define NUM_QUESTIONS       38
#define NUM_CATEGORIES      5
#define NUM_LIKERTS         6

#define MAX_LINE_LEN        4096


/**
 * struct to hold question date
 */
struct Question {
    char question[128];     //question content string;
    _Bool directDirection;  //true = direct, false = reverse, true = default
    char category[2];       //category: C,I,G,U,P
};

/**
 * struct to hold the respondee information
 */
struct Respondee {
    char program[32];       //respondee program
    bool fromCanada;        //is respondee from canada
    char birthday[16];      //respondee birthday
    char response[38][64];  //respondee responses stored as strings
};



/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║      PRINTING FUNCTIONS      ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/

/** PRINT INTRO:
 *
 * Prints the survey intro with the number of respondents
 * @param numRespondents integer containing the number of respondents
 */
void printIntro(const int numRespondents) {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n\n");
    printf("NUMBER OF RESPONDENTS: %d\n", numRespondents);
}



/** PRINT QUESTIONS WITH RPF:
 *
 * Prints out all the questions with their corresponding relative percentual
 *
 * @param questions array of questions
 * @param rpfArr    relative percentual frequency array to be filled
 * @param likerts   likert strings array
 */
void printQuestionsWithRPF(struct Question * questions, float(* rpfArr)[NUM_LIKERTS], char(* likerts)[32]) {
    printf("\nFOR EACH QUESTION BELOW, RELATIVE PERCENTUAL FREQUENCIES ARE COMPUTED FOR EACH LEVEL OF AGREEMENT");

    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        printf("\n\n%s", questions[i].question);    //print question

        for (int j = 0; j < NUM_LIKERTS; ++j) {           //print each relative percentual frequency and likert
            printf("\n%.2f: ", rpfArr[i][j]);
            printf("%s", likerts[j]);
        }
    }
    printf("\n");
}


/** PRINT RESPONSE CATEGORY SCORES:
 *
 * prints out the category scores for each respondent
 *
 * @param catScores array of category scores
 * @param numRespondents integer containing the number of respondents
 */
void printResponseCatScores(const float(* catScores)[5], const int numRespondents) {
    printf("\nSCORES FOR ALL THE RESPONDENTS\n\n");

    for (int i = 0; i < numRespondents; ++i) {//for each respondents category scores
        printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",catScores[i][0],catScores[i][1],catScores[i][2],catScores[i][3],catScores[i][4]);
    }
}



/** PRINT AVERAGE CATEGORY SCORES:
 *
 * prints out the average category scores for all respondents
 *
 * @param avgCatScores array of average category scores for all respondents
 */
void printAvgCatScores(const float * avgCatScores) {
    printf("\nAVERAGE SCORES PER RESPONDENT\n\n");
    printf("C:%.2f,I:%.2f,G:%.2f,U:%.2f,P:%.2f\n",avgCatScores[0],avgCatScores[1],avgCatScores[2],avgCatScores[3],avgCatScores[4]);
}








/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║    TOKENIZATION FUNCTIONS    ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/

/*              ╔══════════════════════════════╗
 *              ║     TOKENIZATION HELPERS     ║
 *              ╚══════════════════════════════╝
 */
/**LIKERT TO VAL:
 *
 * Converts a given likert string to a value
 * @param likertStr the likert string to be converted
 * @param likerts array of likerts to compare to
 * @return returns the value of the likert
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


/**CONSTRUCT RESPONDENT:
 *
 * Constructs a respondent struct from a given input string
 * @param input the input string to be tokenized
 * @param respondee the respondee struct to be filled
 */
void constructRespondent(char input[4096], struct Respondee *respondee) {
    const char delim[2] = ",";
    int i = 0;

    const char *token = strtok(input, delim);

    while (token != NULL) {
        if(i > 2) { //if `i` is greater than 2 then we are dealing with responses
            strncpy(respondee->response[i-3], token, 32); //copy response into respondee struct
        }else if(i==2) { //if `i` is 2 then we are dealing with birthday
            strcpy(respondee->birthday, token);
        }else if(i==1) { //if `i` is 1 then we are dealing with fromCanada
            if(strcmp("yes", token) == 0) {
                respondee->fromCanada = true;
            }else {
                respondee->fromCanada = false;
            }
        }else if(i==0){ //if `i` is 0 then we are dealing with program
            strcpy(respondee->program, token);
        }

        token = strtok(NULL, delim);
        i++;
    }
}




/**READ LINE:
 *
 * Continuously reads from stdin until a non comment 'char[0] != '#' line is found.
 * @param input the string for which the line will be read into.
 */
void readLine(char input[MAX_LINE_LEN]) {
    while(fgets(input, MAX_LINE_LEN, stdin)!= NULL) {//read from stdin until EOF
        input[strcspn(input, "\n")] = '\0';
        if(input[0] != '#') {
            break; //stop reading from stdin when non comment line has been found
        }
    }
}




/*              ╔══════════════════════════════╗
 *              ║    TOKENIZATION FUNCTIONS    ║
 *              ╚══════════════════════════════╝
 */

/**READ CONFIG:
 *
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



/**READ QUESTIONS:
 *
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



/**READ DIRECTIONS:
 *
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



/**READ LIKERTS:
 *
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



/**READ RESPONSES:
 *
 * Reads the responses from stdin and stores them into an array of Respondee structs
 * @param respondees array of respondee structs to be filled
 * @return returns the number of respondents
 */
int readResponses(struct Respondee respondees[MAX_RESPONDENTS]) {
    int i = 0;

     while ( i < MAX_RESPONDENTS) {// for each input line containing response information
         char input[MAX_LINE_LEN*5];
         fgets(input, sizeof(input), stdin);

         if(input[0] != '#') {//ignore line if it is a comment line and keep reading
             constructRespondent(input, &respondees[i]); //send line off to construct respondent
             i++;
         }
     }

    return i;
}









/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║   INITIALIZATION FUNCTIONS   ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/

/**INITIALIZE EMPTY RESPONSES RPF:
 *
 * Initializes the empty responses relative percentual frequency array
 * @param responseRPFArr 2D array to store the relative percentual frequencies
 */
void initializeEmptyResponsesRPF(float(* responseRPFArr)[NUM_LIKERTS]) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {
        for (int j = 0; j < NUM_LIKERTS; ++j) {
            responseRPFArr[i][j] = 0;
        }
    }
}








/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║     STATISTICS FUNCTIONS     ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/

/**SUMMATE RESPONSES:
 *
 * Summate the number of times each likert was chosen for each question
 * @param respondees array of respondee structs
 * @param numRespondents integer containing the number of respondents
 * @param responsesSum 2D array to store the sum of responses
 * @param likerts array of likerts
 */
void summateResponses(const struct Respondee respondees[5],
                      const int numRespondents,
                      int(* responsesSum)[NUM_LIKERTS],
                      const char(* likerts)[32]) {
    for (int i = 0; i < numRespondents; ++i) {      //for each respondent
        for (int j = 0; j < NUM_QUESTIONS; ++j) {   //for each question answered by respondent i
            const int likertVal = likertToVal(respondees[i].response[j], likerts); //convert likert string to respective value
            responsesSum[j][likertVal-1]++; //increment the sum of the respective likert for question i
        }
    }



}



/**MAKE RELATIVE PERCENTUAL FREQUENCY ARRAY:
 *
 * Makes and calculates the relative percentual frequency array from the sum of each time a likert was chosen
 * @param responsesRPF 2D array to store the relative percentual frequencies
 * @param responsesSum 2D array containing the sum of responses
 * @param numRespondents integer containing the number of respondents
 */
void makeRPFArr(float(* responsesRPF)[NUM_LIKERTS],
                const int(* responsesSum)[NUM_LIKERTS],
                const int numRespondents) {
    for (int i = 0; i < NUM_QUESTIONS; ++i) {   //for each question
        for (int j = 0; j < 6; ++j) {           //for each likert sum for question i
            responsesRPF[i][j] = ((float)responsesSum[i][j] / (float)numRespondents) * 100;
        }
    }
}



/**COMPUTE RESPONSES SCORE ARRAY:
 *
 * Computes the responses score array from the respondees array from which likerts where chosen and their
 * corresponding values
 * @param responseScores 2D array to store the response scores
 * @param respondees array of respondee structs
 * @param questions array of questions
 * @param likerts array of likerts
 * @param numRespondents integer containing the number of respondents
 */
void computeResponsesScoreArr(int(* responseScores)[NUM_QUESTIONS],
                              const struct Respondee * respondees,
                              const struct Question * questions,
                              const char(* likerts)[32],
                              const int numRespondents) {
    for (int i = 0; i < numRespondents; ++i) {      //for each respondent's response
        for (int j = 0; j < NUM_QUESTIONS; ++j) {   //for each question answered by respondent i
            int likertVal = likertToVal(respondees[i].response[j], likerts); //convert likert string to respective value
            int likertValDirected = likertVal;
            if(!questions[j].directDirection) { //if question is reverse directed then reverse the value
                likertValDirected = 7 - likertVal;
            }
            responseScores[i][j] = likertValDirected;
        }
    }
}



/**MAKE RESPONSES CATEGORY SCORE ARRAY:
 *
 * Makes the responses category score array from the responses score array by averaging the scores of each category
 * for each respondent
 * @param responsesCatScores 2D array to store the responses category scores
 * @param responsesScores 2D array containing the responses scores
 * @param questions array of questions
 * @param numRespondents integer containing the number of respondents
 */
void makeResponsesCatScoreArr(float(* responsesCatScores)[5],
                              const int(* responsesScores)[NUM_QUESTIONS],
                              const struct Question * questions,
                              const int numRespondents) {

    for (int i = 0; i < numRespondents; ++i) {                  //for each respondent
        int cCount=0, iCount=0, gCount=0, uCount=0, pCount=0;
        int cSum=0, iSum=0, gSum=0, uSum=0, pSum = 0;

        for (int j = 0; j < NUM_QUESTIONS; ++j) {               //for each question answered for respondent i
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
            }
        }
        responsesCatScores[i][0] = (float)cSum / cCount;    //compute average category scores for respondent i
        responsesCatScores[i][1] = (float)iSum / iCount;    //
        responsesCatScores[i][2] = (float)gSum / gCount;    //
        responsesCatScores[i][3] = (float)uSum / uCount;    //
        responsesCatScores[i][4] = (float)pSum / pCount;    //
    }

}



/**COMPUTE AVERAGE CATEGORY SCORES:
 *
 * Computes the average category scores from the responses category scores array by averaging the scores of each
 * category for all respondents
 * @param avgCatScore array to store the average category scores
 * @param catScores 2D array containing the category scores
 * @param numRespondents integer containing the number of respondents
 */
void computeAvgCatScores(float * avgCatScore,
                         const float(* catScores)[NUM_CATEGORIES],
                         const int numRespondents) {
    for (int i = 0; i < NUM_CATEGORIES; ++i) {      //for each category score
        float catSum = 0;
        for (int j = 0; j < numRespondents; ++j) {  //for each respondent's category score for category i
            catSum += catScores[j][i];
        }
        avgCatScore[i] = catSum / (float)numRespondents;    //compute average category score
    }
}





/*░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 *
 *                           ╔══════════════════════════════╗
 *                           ║            MAIN              ║
 *                           ╚══════════════════════════════╝
 *
 *░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/


int main() {
    int numRespondents = 0;                         //Number of Respondents
    int config[4];                                  //Configuration
    struct Question questions[NUM_QUESTIONS];       //Array Of Questions
    char likerts[NUM_LIKERTS][32];                  //Array of Likerts
    float responsesRPF[NUM_QUESTIONS][NUM_LIKERTS]; //Array of Relative Percentual Frequencies

    readConfig(config);              //Read Config From Standard input, store in `config`
    readQuestions(questions);        //Read Questions From Standard input store in `questions`
    readDirections(questions);       //Read Directions From Standard input store in `questions`
    readLikerts(likerts);            //Read Likerts From Standard input store in `likerts`

    if(config[0]==1) {  //PRINT ONLY EMPTY SURVEY
        initializeEmptyResponsesRPF(responsesRPF);
        printIntro(numRespondents);
        printQuestionsWithRPF(questions, responsesRPF, likerts);
    }else{
        struct Respondee respondents[MAX_RESPONDENTS]; //Array of Respondents which stores responses
        numRespondents = readResponses(respondents);   //Read Responses From Standard input store in `respondents`
        printIntro(numRespondents);

        if(config[1]==1) {  //PRINT SURVEY WITH RELATIVE PERCENTUAL FREQUENCIES
            int responsesSum[NUM_QUESTIONS][NUM_LIKERTS];
            summateResponses(respondents, numRespondents, responsesSum, likerts);
            makeRPFArr(responsesRPF, responsesSum, numRespondents);
            printQuestionsWithRPF(questions, responsesRPF, likerts);
        }

        if(config[2]==1 || config [3] == 1) {  //PRINT CATEGORY SCORES
            int responsesScores[numRespondents][NUM_QUESTIONS];       //Array of Responses Scores
            float responsesCatScores[numRespondents][NUM_CATEGORIES]; //Array of Responses Category Scores
            computeResponsesScoreArr(responsesScores, respondents, questions, likerts, numRespondents);
            makeResponsesCatScoreArr(responsesCatScores, responsesScores, questions, numRespondents);

            if(config[2] == 1) { //PRINT CATEGORY SCORES FOR EACH RESPONDENT
                printResponseCatScores(responsesCatScores, numRespondents);
            }

            if(config[3] == 1) { //PRINT AVERAGE CATEGORY SCORES
                float avgCatScores[NUM_CATEGORIES]; //Array of Average Category Scores
                computeAvgCatScores(avgCatScores, responsesCatScores, numRespondents);
                printAvgCatScores(avgCatScores);
            }
        }
    }

    return 0;
}
