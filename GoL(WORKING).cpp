#include <iostream>
using namespace std;

void initializeCells(int arr[][3], int n){
	for (int i = 0; i < n; ++i)
	{
		for (int k = 0; k < n; ++k)
		{
			arr[i][k] = 0;
		}
	}
}

void getCells(int arr[][3], int n) {
	for (int i = 0; i < n; ++i)
	{
		for (int k = 0; k < n; ++k)
		{
			cout << "[" << i << "][" << k << "]: " << arr[i][k];
		}
		cout << endl;
	}	
	cout << endl;
}

bool isAlive(int arr[][3], int row, int collumn, int countAliveCells, int size){
	for (int i = -1; i < 2; ++i)
	{
		for (int k = -1; k < 2; ++k)
		{
			if (i == 0 && k == 0){
				continue;
			}
			
			if (row == 0 && collumn == 0){
				if (i == -1 || k == -1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (row == 0 && collumn == size-1){//|| row == size-1 || collumn == 0 || collumn == size-1){
				if (i == -1 || k == 1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (row == size-1 && collumn == size-1){//|| row == size-1 || collumn == 0 || collumn == size-1){
				if (i == 1 || k == 1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (row == size-1 && collumn == 0){//|| row == size-1 || collumn == 0 || collumn == size-1){
				if (i == 1 || k == -1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (row == 0) {
				if (i == -1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (row == size-1) {
				if (i == 1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (collumn == 0) {
				if (k == -1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (collumn == size-1) {
				if (k == 1){
					continue;
				}
				if (arr[row+i][collumn+k] == 1){
					cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
					continue;
				}
			}

			if (arr[row+i][collumn+k] == 1){
				cout << "This is [" << row+i << "][" << collumn+k << "]: " << arr[row+i][collumn+k] << ", CAC: " << ++countAliveCells << endl;
			}
		}
	}
	if (countAliveCells == 3 && arr[row][collumn] == 1){
		cout << "returned true" << endl;
		return true;
	} else if (countAliveCells == 2 && arr[row][collumn] == 1) {
		cout << "returned true" << endl;
		return true;
	} else if (countAliveCells == 3 && arr[row][collumn] == 0) {
		cout << "returned true1" << endl;
		return true;
	}  else {
		cout << "returned false" << endl;
		return false;
	}
}

void addValueArr(int arr1[][3], int arr2[][3], int count){
	for (int i = 0; i < count; ++i){
		for (int k = 0; k < count; ++k)
		{
			arr1[i][k] = arr2[i][k];
		}
	}
}

void doMoves(int arr[][3], int n){
	int newArr[3][3], countAliveCells = 0;
	initializeCells(newArr, n);
	for (int i = 0; i < n; ++i)
	{
		for (int k = 0; k < n; ++k)
		{	
			countAliveCells = 0;
			cout << "Checking arr[" << i << "][" << k << "]:" << arr[i][k] << endl;
			if (isAlive(arr, i, k, countAliveCells, n)) {
				newArr[i][k] = 1;
			} else {
				newArr[i][k] = 0;
			}	
		}
	}
	addValueArr(arr, newArr, n);
	getCells(arr, n);
	doMoves(newArr, n);
}

int main() {
	int size = 3;
	int arr[3][3];
	
	arr[0][0]=0; arr[0][1]=1; arr[0][2]=0;// arr[0][3]=0; arr[0][4]=0;
	arr[1][0]=0; arr[1][1]=1; arr[1][2]=0;// arr[1][3]=0; arr[1][4]=0;
	arr[2][0]=0; arr[2][1]=1; arr[2][2]=0;// arr[2][3]=0; arr[2][4]=0;
	//arr[3][0]=0; arr[3][1]=0; arr[3][2]=0; arr[3][3]=0; arr[3][4]=0;
	//arr[4][0]=0; arr[4][1]=0; arr[4][2]=0; arr[4][3]=0; arr[4][4]=0;
	
	//initializeCells(arr, size);
	getCells(arr, size);
	doMoves(arr, size);

	return 0;
}