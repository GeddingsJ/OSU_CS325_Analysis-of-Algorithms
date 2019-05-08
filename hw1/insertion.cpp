#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

const int MAX = 9999;

void insertion(int array[], int n){
	int i, j, point;
	for(i = 1; i < n; i++){
		point = array[i];
		j = i - 1;
		while(j >= 0 && array[j] > point){
			array[j + 1] = array[j];
			j = j - 1;
		}
		array[j + 1] = point;
	}
}

int main(){
	ifstream inFile;

	int n = 0;
	int arr[MAX];
	string line;
	int ticker = 0;

	inFile.open("data.txt");

	//while( !inFile.eof()){
	while(inFile >> arr[n]){
		getline(inFile, line);
		//ticker = stoi(line);
		stringstream stream(line);
		
		while(1){
			int j;
			stream >> j;
			if(!stream){
				break;
			}
			arr[ticker] = j;
			ticker++;
		}
		//insertion(arr, ticker);
		for(int i = 0; arr[i]; i++){
			cout << "Val ( " << n << ") " << arr[i];
		}
		//SEND TO OUTFILE HERE
		n++;
	}

	//inFile >> arr[n];
	//while(inFile){
	//	n++;
	//	inFile >> arr[n];
	//}
	
	inFile.close();

	//for(int i = 0; arr[i]; i++){
	//	cout << arr[i];
	//}
	

	//insertion(arr, n);

	//inFile.close();

	return 0;
}
