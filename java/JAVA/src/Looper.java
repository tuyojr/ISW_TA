public class Looper {
//    // simple for loop
//    public static void main(String[] args) {
//        for (int i = 1; i <= 10; i++) {
//            if (i < 10) System.out.print(i + ", ");
//            else System.out.println(i + ".");
//        }
//        System.out.println();
//    }

    // nested for loop
    public static void main(String[] args) {
//        for (int i = 1; i <= 3; i ++) {
//            for (int j = 1; j <= 3; j ++) {
//                System.out.print((i + j) + " ");
//            }
//            System.out.println();
//        }
//        // nested for loop II
//        for (int i = 1; i <= 5; i ++) {
//            for (int j = 1; j <= i; j ++) {
//                System.out.print("* ");
//            }
//            System.out.println();
//        }

        // nested for loop III
        // reverse the order of the nested loop
        for (int i = 1; i <= 5; i ++) {
            for (int j = 5; j >= i; j --) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
