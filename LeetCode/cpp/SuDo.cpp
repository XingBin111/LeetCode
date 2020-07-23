#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class Solution {
public:
    bool isSafe(char num, vector<vector<char>>& board, int row, int col) {

    // check if num exist in row
    for (int j=0; j < 9; j++) {
        if (board[row][j]==num)
			return false;
    }

    // check if num exist in col
    for (int i=0; i < 9; i++) {
        if (board[i][col]==num)
			return false;
    }

    // check if num exist in subgrid
    int R= row - row % 3;
    int C= col - col % 3;

    for (int r=R; r < R+3; r++) {
        for (int c=C; c < C+3; c++) {
            if (board[r][c]==num)
				return false;
        }
    }
    return true;
}
    
    bool backtrack(vector<vector<char>>& board, vector<char>& nums, int row, int col)
    {
        int n = board.size();
        if(row == 9)
            return true;
        if(col == 9)
            return backtrack(board, nums, row+1, 0);
        
        if(board[row][col] != '.')
            return backtrack(board, nums, row, col+1);
        
        for(int i=0; i<9; i++)
        {
            char e = nums[i];
            if(isSafe(e, board, row, col))
            {
                board[row][col] = e;
                bool sudokuCanBeSolvedFurther = backtrack(board, nums, row, col+1);
                if(sudokuCanBeSolvedFurther)
                    return true;
            }
        }
        board[row][col] = '.';
        return false;
    }
    
    void solveSudoku(vector<vector<char>>& board) {
        vector<char> nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
        backtrack(board, nums, 0, 0);
    }
};