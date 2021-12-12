#include <algorithm>
#include <iostream>
#include <queue>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

struct Point { int row; int column; };

vector<vector<int>> LoadFileText() 
{
	ifstream fileSteam("../input.txt");
	vector<vector<int>> content;
	string line;
	while (getline(fileSteam, line))
	{
		vector<int> lineContent;
		for (int i = 0, len = line.size(); i < len; ++i)
		{
			lineContent.push_back(line[i] - 48);
		}
		content.push_back(lineContent);
	}
	return content;
}

int SolvePartOne(vector<vector<int>> input, const int dayCount)
{
	int flashes = 0;
	queue<Point> flashingPoints;

	for (int day = 1; day <= dayCount; ++day)
	{
		// Increment each by one
		for (int lineIndex = 0, lineCount = input.size(); lineIndex < lineCount; ++lineIndex)
		{
			for (int valIndex = 0, lineSize = input[lineIndex].size(); valIndex < lineSize; ++valIndex)
			{
				if (++input[lineIndex][valIndex] > 9)
				{
					flashingPoints.push(Point{ lineIndex, valIndex });
				}
			}
		}

		// Loop through flashing points until completion
		while (flashingPoints.size() > 0)
		{
			Point pos = flashingPoints.front();
			flashingPoints.pop();
			++flashes;

			for (int rowChange = -1; rowChange <= 1; ++rowChange)
			{
				for (int columnChange = -1; columnChange <= 1; ++columnChange)
				{
					Point hitPos = Point{ pos.row + rowChange, pos.column + columnChange };
					if (hitPos.row >= 0 && hitPos.row < input.size() && hitPos.column >= 0 && hitPos.column < input[hitPos.row].size()
						&& ++input[hitPos.row][hitPos.column] == 10)
					{
						flashingPoints.push(hitPos);
					}
				}
			}
		}

		// Reset anything that has flashed
		for (int lineIndex = 0, lineCount = input.size(); lineIndex < lineCount; ++lineIndex)
		{
			for (int valIndex = 0, lineSize = input[lineIndex].size(); valIndex < lineSize; ++valIndex)
			{
				if (input[lineIndex][valIndex] > 9)
				{
					input[lineIndex][valIndex] = 0;
				}
			}
		}
	}
	return flashes;
}

void main()
{
	auto input = LoadFileText();
	cout << "Part One: " << SolvePartOne(input, 100) << endl;
	system("PAUSE");
}
