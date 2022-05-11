#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr)
{
    vector<int> answer;

    for (vector<int>::iterator it = arr.begin(); it != arr.end(); it++)
    {
        if (answer.size() == 0 || *it != answer.back())
        {
            answer.push_back(*it);
        }
    }

    return answer;
}