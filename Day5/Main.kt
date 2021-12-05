import java.io.File

data class Vector2Int(val x: Int, val y: Int)
data class Instruction(val fromPos: Vector2Int, val toPos: Vector2Int)

fun main() {
    val instructions = loadInput("input.txt")
    val hashMap = solvePartOne(instructions)
    println("Part One Solution: ${countValOrHigherInMap(hashMap, 2)}")
    println("Part Two Solution: ${solvePartTwo(instructions, hashMap)}")
}

fun solvePartOne(instructions: List<Instruction>) : HashMap<Vector2Int, Int> {
    val positionHash = hashMapOf<Vector2Int, Int>()

    for(instruction in instructions) {
        if (instruction.fromPos.x == instruction.toPos.x) {
            val min = minOf(instruction.fromPos.y, instruction.toPos.y)
            val max = maxOf(instruction.fromPos.y, instruction.toPos.y)
            for (yPos in min..max) {
                incrementOrAddMapVal(positionHash, Vector2Int(instruction.toPos.x, yPos))
            }

        } else if (instruction.fromPos.y == instruction.toPos.y) {
            val min = minOf(instruction.fromPos.x, instruction.toPos.x)
            val max = maxOf(instruction.fromPos.x, instruction.toPos.x)
            for (xPos in min..max) {
                incrementOrAddMapVal(positionHash, Vector2Int(xPos, instruction.toPos.y))
            }
        }
    }

    return positionHash
}

fun solvePartTwo(instructions: List<Instruction>, positionHash: HashMap<Vector2Int, Int>) : Int {
    for (instruction in instructions) {
        if (instruction.fromPos.x != instruction.toPos.x && instruction.fromPos.y != instruction.toPos.y) {
            val min = minOf(instruction.fromPos.x, instruction.toPos.x)
            val max = maxOf(instruction.fromPos.x, instruction.toPos.x)
            val startAtFrom = min == instruction.fromPos.x
            val yAddition = if ((instruction.fromPos.y < instruction.toPos.y && startAtFrom) || (!startAtFrom && instruction.fromPos.y > instruction.toPos.y)) 1 else -1
            var yVal = if (startAtFrom) instruction.fromPos.y else instruction.toPos.y
            for (xVal in min..max) {
                incrementOrAddMapVal(positionHash, Vector2Int(xVal, yVal))
                yVal += yAddition
            }
        }
    }
    return countValOrHigherInMap(positionHash, 2)
}

fun countValOrHigherInMap(positionHash: HashMap<Vector2Int, Int>, value: Int) : Int {
    var count = 0
    for (keyVal in positionHash) {
        if (keyVal.value >= value) {
            count++
        }
    }
    return count
}

fun incrementOrAddMapVal(positionHash: HashMap<Vector2Int, Int>, key: Vector2Int) {
    when (val count = positionHash[key])
    {
        null -> positionHash[key] = 1
        else -> positionHash[key] = count + 1
    }
}

fun loadInput(filename: String) : List<Instruction> {
    val lines = File(filename).readLines()
    val instructions = arrayListOf<Instruction>()

    for (line in lines) {
        val positions = line.split(" -> ")
        val from = positions[0].split(",")
        val to = positions[1].split(",")
        instructions.add(Instruction(Vector2Int(from[0].toInt(), from[1].toInt()), Vector2Int(to[0].toInt(), to[1].toInt())))
    }

    return instructions
}