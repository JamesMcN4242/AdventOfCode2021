async function loadFile() {
    var response = await fetch('input.txt')
    return await response.text()
}

function getScoreIllegal(char) {
    switch (char) {
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137
        default: return 0
    }
}

function getScoreIncomplete(char) {
    switch (char) {
        case '(': return 1
        case '[': return 2
        case '{': return 3
        case '<': return 4
        default: return 0
    }
}

function solveParts(inputLines) {
    let illegal = []
    let remaining = []

    inputLines.forEach(line => {
        let characterStack = []
        for (let i = 0; i < line.length; ++i) {
            const char = line[i]
            switch (char) {
                case '(':
                case '{':
                case '<':
                case '[':
                    characterStack.push(char)
                    break

                case ')':
                    if (characterStack.pop() !== '(') {
                        illegal.push(')')
                        return
                    }
                    break

                case '}':
                case '>':
                case ']':
                    const compare = characterStack.pop().charCodeAt(0) + 2
                    if (compare !== char.charCodeAt(0)) {
                        illegal.push(char)
                        return
                    }
                    break
            }
        }

        remaining.push(characterStack)
    })

    let partOneScore = 0
    while (illegal.length > 0) {
        partOneScore += getScoreIllegal(illegal.pop())
    }

    let partTwoScores = []
    remaining.forEach(outstanding => {
        let score = 0
        while (outstanding.length > 0) {
            score *= 5
            score += getScoreIncomplete(outstanding.pop())
        }
        partTwoScores.push(score)
    })

    partTwoScores.sort(function(a, b) { return a - b})
    return [partOneScore, partTwoScores[Math.floor(partTwoScores.length / 2)]]
}

loadFile().then(inputBlock => {
        const inputLines = inputBlock.split("\n")
        const output = solveParts(inputLines)
        const outputText = "Part One: " + output[0] + "\nPart Two: " + output[1]
        document.getElementById("output").innerText = outputText
    }
)