async function loadFile() {
    var response = await fetch('input.txt')
    return await response.text()
}

function getScore(char) {
    switch (char) {
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137
        default: return 0
    }
}

function solvePartOne(inputLines) {
    let illegal = []
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
    })

    let score = 0
    while (illegal.length > 0) {
        score += getScore(illegal.pop())
    }
    return score
}

loadFile().then(inputBlock => {
        const inputLines = inputBlock.split("\n")

        let outputText = "Part One: " + solvePartOne(inputLines)
        document.getElementById("output").innerText = outputText
    }
)