#include <stdio.h>

/** PRINT INTRO:
 *
 * Prints the survey intro with the number of respondents
 * @param numRespondents integer containing the number of respondents
 */
void printIntro(const int numRespondents) {
    printf("Examining Science and Engineering Students' Attitudes Towards Computer Science\n");
    printf("SURVEY RESPONSE STATISTICS\n\n");
    printf("NUMBER OF RESPONDENTS: %d", numRespondents);
}

