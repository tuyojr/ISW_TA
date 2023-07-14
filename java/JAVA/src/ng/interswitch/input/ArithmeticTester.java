package ng.interswitch.input;
import java.util.Scanner;

public class ArithmeticTester {
    public static void main(String[] args) {
        // create a scanner object to read input from the command line
        try(Scanner userInput = new Scanner(System.in)) {

            // prompt the user to enter two numbers
            System.out.println("Enter four numbers:");

            // read the two numbers from the command line; store them in variables
            // nextDouble() reads the next double from the command line
            double firstNumber = userInput.nextDouble();
            double secondNumber = userInput.nextDouble();
            int thirdNumber = userInput.nextInt();
            int fourthNumber = userInput.nextInt();

            // create an object of the BasicArithmetic class and pass the two numbers to the constructor
            BasicArithmetic basicArithmetic = new BasicArithmetic(firstNumber, secondNumber);

            // print the sum and difference of the two numbers
            System.out.printf("Performing addition operation: %s + %s \n", firstNumber, secondNumber);
            System.out.println("The sum of the two numbers is: " + basicArithmetic.addFirstAndSecondNumber());
            System.out.printf("Performing subtraction operation: %s - %s \n", firstNumber, secondNumber);
            System.out.println("The difference of the two numbers is: " + basicArithmetic.subtractFirstAndSecondNumber());
            System.out.println();
            System.out.println("The power of the third number to the fourth number is: " + BasicArithmetic.powerRaiser(thirdNumber, fourthNumber));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
