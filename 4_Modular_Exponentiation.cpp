#include <iostream>
#include <vector>

using namespace std;


int ModularExpo(int, vector<int>, int, int);

vector<int> BinaryK(int k)
{
vector<int> K;
int tmp = k;
int i=0;


while(tmp > 0)
{

K.push_back(tmp%2);


tmp = (tmp-K[i])/2;
i++;
}


return K;
}

int ModularExpo(int a, vector<int> K, int n, int k)
{
int i, A, b;


if(n==1)
return 0;


b = 1;
if(k==0)
return b;


A = a;

if(K[0] == 1) {
b = a;
}

for(i=1; i<=K.size()-1; i++)
{

A = (A*A) % n;

if(K[i] == 1)
b = (A*b) % n;
}

return b;
}

int main()
{
int i, a, k, n, answer;
vector<int> K;


cout<<"Please enter k value: ";    
cin>>k; 

cout<<"Please enter an 'a' value: ";    
cin>>a; 

cout<<"Please enter n value: ";    
cin>>n; 

K = BinaryK(k);

answer = ModularExpo(a, K, n, k);

cout << "The answer is: "<< answer;

return 0;
}



