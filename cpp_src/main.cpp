#include<stdio.h>
#include<iostream>
#include <vector>

using namespace std;

void print_vect(vector<int> &abc)
{

	vector<int>::iterator it;
	for(unsigned int i = 0;i< abc.size();i++)
	{
		cout << abc[i] << endl;
	}	

}


int main()
{


	vector<int> wow1;
	wow1.push_back(120);
	wow1.push_back(110); 
	print_vect(wow1);
	vector<int> wow;
	wow.push_back(20);
	wow.push_back(10); 
	print_vect(wow);
}



