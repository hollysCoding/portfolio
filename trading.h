#ifndef TRADING_H
#define TRADING_H

//#include "time.h"
#include "common.h"
#include "simulator.h"

int savePortfolio(char* filename, MyPortfolio* pMyPortfolio);
int readPortfolio(char* filename, MyPortfolio* pMyPortfolio);
void printStock(Position* pPosition);
void printPortfolio(MyPortfolio* pMyPortfolio);
double getBalance(MyPortfolio* pMyPortfolio);
double buy(MyPortfolio* pMyPortfolio, char* ticker, double shares);
double sell(MyPortfolio* pMyPortfolio, char* ticker, double shares);
double buyWithPermission(MyPortfolio* pMyPortfolio, char* ticker, double shares);
double sellWithPermission(MyPortfolio* pMyPortfolio, char* ticker, double shares);

#endif
