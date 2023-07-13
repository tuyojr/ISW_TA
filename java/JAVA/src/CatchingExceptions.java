import java.io.*;
public class CatchingExceptions {
    /* syntax
    *  try {
    *     // code that may throw an exception
    * } catch (Exception e) {
    *    // code to handle the exception
    * }
    * */
    public static void main(String[] args) {
        try {
            int[] nums = new int[2];
            System.out.println("Element Three: " + nums[3]);
        } catch (ArrayIndexOutOfBoundsException e) { // java.lang.ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 2
            System.out.println("This throws an exception: " + e);
        }
        System.out.println("This is after the exception block");
    }
}
