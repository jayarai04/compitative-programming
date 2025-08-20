import java.util.Scanner;
  public class lastdigit {
    public static void main (String[] args) {
      Scanner scanner = new Scanner(System.in);
      System.out.println("enter a number: ");
      int number = scanner.nextInt();

      int lastdigit = Math.abs(number) % 10;

      if (lastdigit == 4) {
        System.out.println("last digit is 4");
      } else {
        System.out.println("last digit is not 4");
      }
    }
  }