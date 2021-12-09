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

void main () {
  var board = GetInput();
  print('Part One: ${SolvePartOne(board)}');
}