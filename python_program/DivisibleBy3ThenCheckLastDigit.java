import java.util.Scanner;

public class DivisibleBy3ThenCheckLastDigit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        if (number % 3 == 0) {
            int lastDigit = Math.abs(number) % 10;

            if (lastDigit == 4) {
                System.out.println("The number is divisible by 3 and its last digit is 4.");
            } else {
                System.out.println("The number is divisible by 3 but its last digit is not 4.");
            }
        } else {
            System.out.println("The number is not divisible by 3.");
        }
    }
} 