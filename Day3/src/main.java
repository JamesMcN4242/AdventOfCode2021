import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

class Day3 {
    public static void main(String[] args) throws IOException {
        List<String> input = Files.readAllLines(Path.of("input.txt"));
        System.out.printf("Part One Answer: %d%n", SolvePartOne(input));
        System.out.printf("Part Two Answer: %d%n", SolvePartTwo(input));
    }

    private static int SolvePartOne(List<String> input)
    {
        int gamma = 0, epsilon = 0;
        int[] mostCommonBits = GetMostCommonBits(input);

        for (int i = 0; i < mostCommonBits.length; ++i) {
            int addition = 1 << (mostCommonBits.length - i - 1);
            if(mostCommonBits[i] == 1) {
                gamma += addition;
            } else {
                epsilon += addition;
            }
        }
        
        return gamma * epsilon;
    }

    private static int SolvePartTwo(List<String> input)
    {
        List<String> oxygenRating = input;
        List<String> co2ScrubRating = new ArrayList<>(input);

        LoopTilCompletion(oxygenRating, false);
        LoopTilCompletion(co2ScrubRating, true);
        return Integer.parseInt(oxygenRating.get(0), 2) * Integer.parseInt(co2ScrubRating.get(0), 2);
    }

    private static void LoopTilCompletion(List<String> input, boolean removeLeastCommon) {
        int charCount = input.get(0).length();
        char removeIfOne = removeLeastCommon ? '1' : '0';
        char removeIfZero = removeLeastCommon ? '0' : '1';

        for(int i = 0; i < charCount && input.size() > 1; ++i)
        {
            int mostCommon = GetMostCommonBit(input, i);
            char toRemove = mostCommon == 1 ? removeIfOne : removeIfZero;
            int finalI = i;
            input.removeIf(n -> n.charAt(finalI) == toRemove);
        }
    }

    private static int[] GetMostCommonBits(List<String> input) {
        int charCount = input.get(0).length();
        int[] mostCommon = new int[charCount];

        for(int i = 0; i < charCount; ++i) {
            mostCommon[i] = GetMostCommonBit(input, i);
        }
        return mostCommon;
    }

    private static int GetMostCommonBit(List<String> input, int charIndex) {
        int timesOnesAppeared = 0;

        for (String line : input) {
            timesOnesAppeared += line.charAt(charIndex) - 48;
        }

        int halfLineCount = (input.size() / 2) + (input.size() % 2);
        timesOnesAppeared = timesOnesAppeared >= halfLineCount ? 1 : 0;
        return timesOnesAppeared;
    }
}