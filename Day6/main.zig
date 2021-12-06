const std = @import("std");
const print = std.debug.print;

pub fn main() !void {
    print("Part One: {}\n", .{solveForDays(80)});
    print("Part Two: {}\n", .{solveForDays(256)});
}

fn solveForDays(dayCount: u64) !u64 {
    var file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    var fishArr: [9]u64 = [9]u64{0, 0, 0, 0, 0, 0, 0 , 0, 0};
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        for (line) |value| {
            if(value >= 48) {
                fishArr[value-48] += 1;
            }
        }
    }       
            
    var day: u32 = 0;
    while (day < dayCount) {
        const dayZeroCount: u64 = fishArr[0];

        var index: u32 = 0;
        while(index < 8) {
            fishArr[index] = fishArr[index + 1];
            index += 1;
        }
        fishArr[6] += dayZeroCount;
        fishArr[8] = dayZeroCount;
        day += 1;
    }

    var totalFish: u64 = 0;
    for (fishArr) |fishCount| {
        totalFish += fishCount;
    }
    return totalFish;
}