
/*
============================================================================
Name        : Project3_004.c
Author      : Saeed Rajput
Date        : 2018/11/16
Copyright   : Your copyright notice
Description : Hello World in C, Ansi-style
============================================================================
*/

#ifndef COMMON_H
#define COMMON_H

//Systems incldues
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Local includes

//Constants

#define MAX_TICKER_SIZE 10
#define MAX_MY_STOCKS 5

//structs
typedef struct {
	char ticker[MAX_TICKER_SIZE];
	double price;
	double shares;
} Position;

typedef struct {
	double balance;
	Position positions[MAX_MY_STOCKS];
	int positionsSize;
	int positionsCapacity;  //Should be set to MAX_MY_STOCKS
} MyPortfolio;

//Prototypes
int initializePortfolio(char* fileName, MyPortfolio* pMyPortfolio);
Position* findStock(MyPortfolio* pMyPortfolio, char* ticker);

#endif
