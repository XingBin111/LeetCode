#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

bool NEIGHBOR_HOODS_4 = true;
vector<vector<int> > OFFSETS_4(5, vector<int>(2, 0));
void show_img(vector<vector<int> >& binary_img);

vector<vector<int> >& neighbor_value(vector<vector<int> >& binary_img, vector<vector<int> > offsets, bool reverse)
{
    int rows = binary_img.size();
    int cols = binary_img[0].size();

    int label_index = 0;
    int rows_[2];
    int cols_[2];
    if(!reverse)
    {
        rows_[0] = 0;   rows_[1] = 1;
        cols_[0] = 0;   cols_[1] = 1;
    }
    else
    {
        rows_[0] = rows-1;  rows_[1] = -1;
        cols_[0] = cols-1;  cols_[1] = -1;
    }
    for(int i=rows_[0]; (i<=rows-1) && i>=0; i+=rows_[1])
    {
        for(int j=cols_[0]; (j<=cols-1)&&j>=0; j+=cols_[1])
        {
            if(binary_img[i][j]==0)
                continue;
            int label = 256;   
            for(int k=0; k<offsets.size(); k++)
            {
                int r = min(max(0, i + offsets[k][0]), rows-1);
                int c = min(max(0, j + offsets[k][1]), cols-1);
                int v = binary_img[r][c];
                if(v == 0)
                    continue;
                label = (v < label) ? v : label;
            }
            // 如果周围没有更小的像素就赋新的标签
            if(label == 255)
            {
                label_index++;
                label = label_index;
            }
            binary_img[i][j] = label;
        }
    }
    return binary_img;
}

vector<vector<int> >& two_pass(vector<vector<int> >& binary_img, const vector<vector<int> > offsets)
{
    binary_img = neighbor_value(binary_img, offsets, false);
    show_img(binary_img);

    binary_img = neighbor_value(binary_img, offsets, true);
    return binary_img;
}

vector<vector<int> >& recursive_seed(vector<vector<int> >& binary_img, int seed_row, int seed_col, int num, int max_num=100)
{
    int rows = binary_img.size();
    int cols = binary_img[0].size();
    binary_img[seed_row][seed_col] = num;
    for(int i=0; i<OFFSETS_4.size(); i++)
    {
        int r = min(max(0, seed_row + OFFSETS_4[i][0]), rows-1);
        int c = min(max(0, seed_col + OFFSETS_4[i][1]), cols-1);
        int v = binary_img[r][c];
        if(v < max_num)
            continue;
        binary_img = recursive_seed(binary_img, r, c, num);
    }
    return binary_img;
}

vector<vector<int> >& seed_filling(vector<vector<int> >& binary_img,int max_num=100)
{
    int rows = binary_img.size();
    int cols = binary_img[0].size();
    int num = 1;
    for(int i=0; i<rows; i++)
    {
        for(int j=0; j<cols; j++)
        {
            int val = binary_img[i][j];
            if(val <= max_num)
                continue;
            
            // 只对255的像素值进行递归
            binary_img = recursive_seed(binary_img, i, j, num);
            num++;
        }
    }
    return binary_img;
}

void show_img(vector<vector<int> >& binary_img)
{
    int rows = binary_img.size();
    int cols = binary_img[0].size();
    for(int i=0; i<rows; i++)
    {
        for(int j=0; j<cols; j++)
        {
            cout << binary_img[i][j] << "    ";
        }
        cout << endl;
    }
}

int main()
{
    OFFSETS_4[0] = vector<int>({0, -1});
    OFFSETS_4[1] = vector<int>({-1, 0});
    OFFSETS_4[2] = vector<int>({0, 0});
    OFFSETS_4[3] = vector<int>({0, 1});
    OFFSETS_4[4] = vector<int>({1, 0});

    vector<vector<int> > binary_img(4, vector<int>(7, 0));
    int n = 14;
    int idxs[] = {0, 2, 0, 5,
            1, 0, 1, 1, 1, 2, 1, 4, 1, 5, 1, 6,
            2, 2, 2, 5,
            3, 1, 3, 2, 3, 4, 3, 6};
    for(int i=0; i<n; i++)
    {
        int idx[] = {idxs[2*i], idxs[2*i+1]};
        binary_img[idx[0]][idx[1]] = 255;
    }

    show_img(binary_img);
    // binary_img = two_pass(binary_img, OFFSETS_4);
    binary_img = seed_filling(binary_img);
    show_img(binary_img);
    return 0;
}