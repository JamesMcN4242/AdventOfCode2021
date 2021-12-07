module Day7

  def self.load_file
    file = File.open("input.txt")
    file_data = file.read.split(",").map(&:to_i)
    file.close
    file_data
  end

  def self.solve_part_one
    input_data = load_file.sort
    median = input_data[input_data.length / 2]
    moved = 0
    input_data.each { |input|
      moved += (input - median).abs
    }
    moved
  end

  puts solve_part_one
end
