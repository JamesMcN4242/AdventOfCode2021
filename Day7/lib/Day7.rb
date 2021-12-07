module Day7

  def self.load_file
    file = File.open("input.txt")
    file_data = file.read.split(",").map(&:to_i)
    file.close
    file_data
  end

  def self.solve_part_one(input_data)
    median = input_data[input_data.length / 2]
    moved = 0
    input_data.each { |input|
      moved += (input - median).abs
    }
    moved
  end

  def self.solve_part_two(input_data)
    average = (input_data.sum.to_f / input_data.length.to_f).floor
    fuel_used = 0
    input_data.each { |input|
      fuel_used += ((input - average).abs * ((input - average).abs + 1) / 2)
    }
    fuel_used
  end

  input_data = load_file.sort
  puts "Part One: %d" %solve_part_one(input_data)
  puts "Part Two: %d" %solve_part_two(input_data)
end
