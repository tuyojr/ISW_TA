import java.io.FileReader;
import java.io.IOException;
public class MultipleExceptionHandling {
    /* syntax
    *  try {
    *    // code that may throw an exception
    * } catch (ExceptionType1 e1) {
    *   // code to handle exception to type ExceptionType1
    * } catch (ExceptionType2 e2) {
    *  // code to handle exception to type ExceptionType2
    * } catch (ExceptionType3 e3) {
    * // code to handle exception to type ExceptionType3
    * }
    * OR
    * try {
    *  // code that may throw an exception
    * } catch (ExceptionType1 | ExceptionType2 | ExceptionType3 e) {
    * // code to handle exception to type ExceptionType1, ExceptionType2, or ExceptionType3
    * }
    * */

    // Throw and Throws
    // Throw: used to throw an exception explicitly
    // Throws: used to declare an exception (checked exception)
    /* public void deposit(double amount) throws RemoteException {
    * // Method implementation
    * throw new RemoteException();
    * }
    * // remainder of class definition
    * */
    public static void main(String[] args) {
        // try with resources
        try(FileReader fr = new FileReader("C:\\Users\\Adedolapo.Olutuyo\\Documents\\ISW_TA\\java\\JAVA\\src\\asis_sh.txt")){
            char[] a = new char[100];
            fr.read(a); // reads the content to the array
            for(char c : a)
                System.out.print(c); // prints the characters one by one
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}