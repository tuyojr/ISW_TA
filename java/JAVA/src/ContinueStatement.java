public class ContinueStatement {
    public static void main(String[] args) {
        int x = 1, y = 10;

        do {
            if (x == y/2) {
                x++;
                continue; // skips the rest of the loop body and goes to the next iteration
            }
            System.out.println("x = " + x);
            x++;
        } while (x <= y);
    }
}
