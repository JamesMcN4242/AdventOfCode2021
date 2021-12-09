import 'dart:collection';
import 'dart:io';

List<List<int>> GetInput() {
  String fileContent = File('input.txt').readAsStringSync();
  List<String> lines = fileContent.replaceAll("\r", "").split("\n");
  var board = [
    for(var row = 0; row < lines.length; row++)
      [for (var column = 0; column < lines[row].length; column++)
        int.parse(lines[row][column])
        ],
  ];

  return board;
}

int SolvePartOne(List<List<int>> board) {
  int value = 0;
  for(var row = 0; row < board.length; row++) {
    for (var column = 0; column < board[row].length; column++) {
      var currentVal = board[row][column];
      if ((row == 0 || currentVal < board[row-1][column]) &&
          (row == board.length - 1 || currentVal < board[row+1][column]) &&
          (column == 0 || currentVal < board[row][column-1]) &&
          (column == board[row].length - 1 || currentVal < board[row][column+1])) {
          value += (currentVal + 1);
      }
    }
  }
  
  return value;
}

int SolvePartTwo(List<List<int>> board) {
  List<int> basinSizes = List.empty(growable: true);

  for(var row = 0; row < board.length; row++) {
    for (var column = 0; column < board[row].length; column++) {
      var currentVal = board[row][column];
      if ((row == 0 || currentVal < board[row-1][column]) &&
          (row == board.length - 1 || currentVal < board[row+1][column]) &&
          (column == 0 || currentVal < board[row][column-1]) &&
          (column == board[row].length - 1 || currentVal < board[row][column+1])) {

        var currentVal = board[row][column];
        Queue<List<int>> toConsider = Queue.from([[row-1, column, currentVal], [row+1, column, currentVal], [row, column -1, currentVal], [row, column + 1, currentVal]]);
        Set<int> inBasin = Set.identity();
        inBasin.add((row << 16) | column);
        while(toConsider.length > 0) {
          var curr = toConsider.removeFirst();
          if(inBasin.contains((curr[0] << 16) | curr[1]) || !IsPartOfBasin(board, curr[2], curr)) continue;

          var value = board[curr[0]][curr[1]];
          toConsider.add([curr[0] - 1, curr[1], value]);
          toConsider.add([curr[0] + 1, curr[1], value]);
          toConsider.add([curr[0], curr[1] - 1, value]);
          toConsider.add([curr[0], curr[1] + 1, value]);
          inBasin.add((curr[0] << 16) | curr[1]);
        }

        basinSizes.add(inBasin.length);
      }
    }
  }

  basinSizes.sort();
  var len = basinSizes.length;
  return basinSizes[len - 1] * basinSizes[len - 2] * basinSizes[len - 3];
}

bool IsPartOfBasin(List<List<int>> board, int previousValue, List<int> coord) {
  return coord[0] >= 0 && coord[1] >= 0 && board.length > coord[0] && board[coord[0]].length > coord[1] && board[coord[0]][coord[1]] > previousValue && board[coord[0]][coord[1]] != 9;
}

void main () {
  var board = GetInput();
  print('Part One: ${SolvePartOne(board)}');
  print('Part Two: ${SolvePartTwo(board)}');
}