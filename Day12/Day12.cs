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

        foreach (string nextNode in m_graphNodes[mostRecent])
        {
            if (char.IsLower(nextNode[0]) && currentPath.Contains(nextNode))
            {
                continue;
            }

            List<string> newList = new List<string>(currentPath);
            newList.Add(nextNode);
            AddAllPaths(toAddTo, newList);
        }
    }

    private void SolvePartTwo()
    {
        /* I admit there is probably tons of ways to go about this differently, or to combine it into part ones method without so much duplication...
           buuuut I'm watching a film at the same time and just wanting to get this finished
           Side note: "Run" is a rather obvious film from the get go, but still enjoyable. If you haven't seen it before, then I'd recommend it.
           If you have however, then I think we need to talk about how bad the pharmacist is. 
           Like COME ON. You have a girl in front of you very clearly having a panic attack, who has just asked what these muscle relaxing animal drugs would do to a human.
           And you just straight up don't process that could be connected to the fact she is in a wheelchair!?
           There is being oblivious, and then there is that. I bet this woman when she finds out about the whole scenario will be sitting thinking
           "if only there was a sign", completely none the wiser that she's just shafted someone's life so extremely.
           Actually. Multiple people's lives. All because you don't connect the rather obvious dots of wheel chair -> leg numbing drug -> panic attack immediately after hearing that
           Anyway, I'll stop complaining about this fictional character now. On with the code! Really just a copy paste with two minor changes
         */
        List<List<string>> allPaths = new List<List<string>>(100);
        List<string> currentPath = new List<string> { "start" };
        AddAllPathsPartTwo(allPaths, currentPath, false);
        System.Console.WriteLine($"Part Two: {allPaths.Count}");
    }

    private void AddAllPathsPartTwo(List<List<string>> toAddTo, List<string> currentPath, bool containsReusedSmall)
    {
        string mostRecent = currentPath[currentPath.Count - 1];
        if (mostRecent == "end")
        {
            toAddTo.Add(currentPath);
            return;
        }

        foreach (string nextNode in m_graphNodes[mostRecent])
        {
            if (nextNode == "start" || (containsReusedSmall && char.IsLower(nextNode[0]) && currentPath.Contains(nextNode)))
            {
                continue;
            }

            List<string> newList = new List<string>(currentPath);
            newList.Add(nextNode);
            AddAllPathsPartTwo(toAddTo, newList, containsReusedSmall || char.IsLower(nextNode[0]) && currentPath.Contains(nextNode));
        }
    }

    public void Run()
    {
        BuildGraph();
        SolvePartOne();
        SolvePartTwo();
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
