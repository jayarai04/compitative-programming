import java.util.Scanner;
public class divisibleby7 {
  public static void main (String [] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("enter a number: ");
    int number = scanner.nextInt();
    if (number % 7 == 0) {
      System.out.println("divisible");
    } else {
      System.out.println("not divisible");
    }
  }
}