fn search(nums: Vec<i32>, target: i32) -> i32 {
    for i in nums.iter() {
        if i == target {
            return i.as_i32();
        }
    }
}

fn main() {
    println!(search(Vec { 1, 0, 3, 5, 9, 12 }, 9))
}