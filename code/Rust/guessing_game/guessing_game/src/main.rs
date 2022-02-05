use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number!");
    let secret_number = rand::thread_rng().gen_range(1..101);

    // FOR DEBUG: Uncomment to display secret number
    // println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse(){
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Sorry bud, that's way too low."),
            Ordering::Greater => println!("Slow your roll, man! That number's way too huge!"),
            Ordering::Equal => {
                println!("Yeah, buddy! You got it! You got it!!!");
                break;
            }
        }
    }
}
