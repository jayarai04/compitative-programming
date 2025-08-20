import java.util.Scanner;

public class divisibleandlastdigit {
  public static void main (String[] args){
  Scanner scanner = new Scanner(System.in);
  System.out.println("enter a number:");
  int number = scanner.nextInt();
  int lastdigit = Math.abs(number) % 10;

  if ( number % 3 == 0 && lastdigit == 4 ) {
    System.out.println("divisible by 3 and last digit is 4");
  } else {
    System.out.println("not divisibile and last digit is not 4");
  }
 }
}