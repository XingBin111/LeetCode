#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>

using namespace std;

// 顺时针旋转90度
void rotate(vector<vector<int> >& matrix){
    reverse(matrix.begin(), matrix.end());

    int row = matrix.size(), col = matrix[0].size();
    for(int i=0; i< row; i++)
        for(int j=i+1; j<col; j++)
            swap(matrix[i][j], matrix[j][i]);
}

// 逆时针旋转90度
void anti_rotate(vector<vector<int> >& matrix){
    int row = matrix.size(), col = matrix[0].size();
    for(int i=0; i<col; i++)
        reverse(matrix[i].begin(), matrix[i].end());

    for(int i=0; i< row; i++)
        for(int j=i+1; j<col; j++)
            swap(matrix[i][j], matrix[j][i]);
}

void show(vector<vector<int> >& matrix){
    int row = matrix.size(), col = matrix[0].size();
    for(int i=0; i< row; i++){
        cout << "row " << i << " :";
        for(int j=0; j<col; j++)
            cout << matrix[i][j] << "   " ;
        cout << "\n";
    }
}

int main(){
    vector<vector<int> > matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    cout << "before rotate:\n";
    show(matrix);

    rotate(matrix);
    cout << "顺时针旋转90度:\n";
    show(matrix);

    matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    anti_rotate(matrix);
    cout << "逆时针旋转90度:\n";
    show(matrix);

    cout << -123/10 << endl;
    cout << -123%10 << endl;
    return 0;
        
}