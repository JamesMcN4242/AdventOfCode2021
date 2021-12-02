use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let input = get_input();
    println!("{}", solve_part_one(input));
}

fn solve_part_one(input: Vec<Input>) -> i32 {
    let mut position = [0, 0];
    
    for element in input {
        match element.instruction {
            Instruction::FORWARD => position[0] += element.value,
            Instruction::UP => position[1] -= element.value,
            Instruction::DOWN => position[1] += element.value,
        }
    }

    position[0] * position[1]
}

enum Instruction {
    FORWARD, UP, DOWN
}

pub struct Input {
    instruction : Instruction,
    value : i32
}

fn get_input() -> Vec<Input> {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    let mut vector = Vec::new();
    reader.lines().enumerate().for_each(|(_index, line)| {
        let unwrapped = line.unwrap();
        let line_content: Vec<&str> = unwrapped.split_whitespace().collect();
        
        let mut instruction = Instruction::FORWARD;
        let identify_char = line_content[0].chars().nth(0).unwrap();
        if identify_char == 'd' {
            instruction = Instruction::DOWN;
        } else if identify_char == 'u' {
            instruction = Instruction::UP;
        }
        let element = Input {instruction: instruction, value: line_content[1].parse().unwrap()};
        vector.push(element);
    });

    vector
}