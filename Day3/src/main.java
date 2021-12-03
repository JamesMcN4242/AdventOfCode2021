import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

class Day3 {
    public static void main(String[] args) throws IOException {
        List<String> input = GetInput();
        System.out.printf("Part One Answer: %d%n", SolvePartOne(input));
    }

    private static List<String> GetInput() throws IOException {
        return Files.readAllLines(Path.of("input.txt"));
    }

    private static int SolvePartOne(List<String> input)
    {
        int charCount = input.get(0).length();
        int[] timesOnesAppeared = new int[charCount];

        for (String line : input) {
            for (int j = 0; j < charCount; ++j) {
                timesOnesAppeared[j] += line.charAt(j) - 48;
            }
        }

        int gamma = 0, epsilon = 0;
        int halfLineCount = input.size() / 2;

        for (int i = 0; i < charCount; ++i) {
            int addition = 1 << (charCount - i - 1);
            if(timesOnesAppeared[i] > halfLineCount) {
                gamma += addition;
            } else {
                epsilon += addition;
            }
        }
        
        return gamma * epsilon;
    }
}
