using System.Collections.Generic;
using System.IO;

public class Day12
{
    private Dictionary<string, List<string>> m_graphNodes = new Dictionary<string, List<string>>();

    private string[] LoadInput()
    {
        return File.ReadAllLines("../../../input.txt");
    }

    private void BuildGraph()
    {
        var input = LoadInput();
        foreach(var line in input)
        {
            var segments = line.Split('-');
            if (!m_graphNodes.ContainsKey(segments[0])) m_graphNodes.Add(segments[0], new List<string>());
            if (!m_graphNodes.ContainsKey(segments[1])) m_graphNodes.Add(segments[1], new List<string>());
            m_graphNodes[segments[0]].Add(segments[1]);
            m_graphNodes[segments[1]].Add(segments[0]);
        }
    }

    private void SolvePartOne()
    {
        List<List<string>> allPaths = new List<List<string>>(100);
        List<string> currentPath = new List<string> { "start" };
        AddAllPaths(allPaths, currentPath);
        System.Console.WriteLine($"Part One: {allPaths.Count}");
    }

    private void AddAllPaths(List<List<string>> toAddTo, List<string> currentPath)
    {
        string mostRecent = currentPath[currentPath.Count - 1];
        if (mostRecent == "end")
        {
            toAddTo.Add(currentPath);
            return;
        }

        foreach(string nextNode in m_graphNodes[mostRecent])
        {
            if(char.IsLower(nextNode[0]) && currentPath.Contains(nextNode))
            {
                continue;
            }

            List<string> newList = new List<string>(currentPath);
            newList.Add(nextNode);
            AddAllPaths(toAddTo, newList);
        }
    }

    public void Run()
    {
        BuildGraph();
        SolvePartOne();
    }
} 

static class Program
{
    static void Main(string[] args)
    {
        Day12 solution = new Day12();
        solution.Run();
    }
}
