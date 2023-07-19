import java.io.*;

public class BufferInput {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Whats your favorite video game?: ");
        String game = null;
        try {
            game = br.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        System.out.print("Your favorite video game is " + game);
        int game2 = 0;
        try {
            game2 = br.read();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        System.out.println("Readline(): " + game);
        System.out.println("Read(): " + game2 + "["+ (char)game2 +"]");
    }
}
