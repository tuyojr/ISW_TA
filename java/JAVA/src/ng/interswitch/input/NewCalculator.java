package ng.interswitch.input;

public interface NewCalculator {
    int addTwoNumbers(int firstNumber, int secondNumber);
    int subtractTwoNumbers(int firstNumber, int secondNumber);
    int multiplyTwoNumbers(int firstNumber, int secondNumber);

//    public class User implements NewCalculator {
//        @Override
//        public int addTwoNumbers(int firstNumber, int secondNumber) {
//            return firstNumber + secondNumber;
//        }
//        @Override
//        public int subtractTwoNumbers(int firstNumber, int secondNumber) {
//            return firstNumber - secondNumber;
//        }
//        @Override
//        public int multiplyTwoNumbers(int firstNumber, int secondNumber) {
//            return firstNumber * secondNumber;
//        }
//    }
//
//    public static void main(String[] args) {
//        User user = new User();
//        System.out.println(user.addTwoNumbers(2, 3));
//        System.out.println(user.subtractTwoNumbers(2, 3));
//        System.out.println(user.multiplyTwoNumbers(2, 3));
//    }
}
