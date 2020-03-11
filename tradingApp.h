
/*
============================================================================
Name        : tradingApp.h for Project 4
Author      : Holly Schlichting
Date        : 2018/12/1
Copyright   : Your copyright notice
Description : Hello World in C, Ansi-style
============================================================================
*/

#ifndef TRADINGAPP_H
#define TRADINGAPP_H

//Systems incldues
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Local includes
#include "common.h"
//Constants

//Structs

//Prototypes
void process();
void menu(MyPortfolio* pMyPortfolio);
double buySpecific(MyPortfolio* pMyPortfolio, char* ticker, double shares);
double sellSpecific(MyPortfolio* pMyPortfolio, char* ticker, double shares);
void currentPrices(MyPortfolio* pMyPortfolio, char* ticker);
void printWorth(MyPortfolio* pMyPortfolio);
#endif
