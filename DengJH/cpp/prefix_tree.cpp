/* 
查找和插入的效率为O(n), n为待插入字符串长度
空间消耗很大
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define ALPHABET_SIZE 26

typedef struct trie_node
{
    int count;          // 记录该节点代表的单词个数
    trie_node *children[ALPHABET_SIZE];     // 各子节点
}* trie;

trie_node* create_trie_node()
{
    trie_node* pNode = new trie_node();
    pNode->count = 0;
    for(int i=0; i<ALPHABET_SIZE; i++)
        pNode->children[i] = nullptr;
    return pNode;
}

void trie_insert(trie root, string s)
{   
    cout << "insert string: " << s << " in trie\n";
    trie_node* node = root;
    
    for(int i=0; i<s.length(); i++)
    {   
        char p = s[i];
        if(node->children[p-'a'] == nullptr)
            node->children[p-'a'] = create_trie_node();
        node = node->children[p-'a'];
    }
    node->count++;
}

int trie_search(trie root, string s)
{   
    trie_node* node = root;
    for(int i=0; i<s.length(); i++)
    {   
        char p = s[i];
        node = node->children[p-'a'];
        if(node == nullptr)
            return 0;
    }
    return 1;
}

int main()
{
    char keys[][8] = {"the", "a", "there", "answer", "any", "by", "bye", "their"};
    trie root = create_trie_node();
    for(int i=0; i<8; i++)
        trie_insert(root, keys[i]);

    char s[][32] = {"Present in trie", "Not present in trie"};
    printf("%s --- %s\n", "the", trie_search(root, "the")>0?s[0]:s[1]);
    printf("%s --- %s\n", "these", trie_search(root, "these")>0?s[0]:s[1]);
    printf("%s --- %s\n", "their", trie_search(root, "their")>0?s[0]:s[1]);
    printf("%s --- %s\n", "thaw", trie_search(root, "thaw")>0?s[0]:s[1]);
    return 0;
}