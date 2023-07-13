import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
public class FileReading {
    public static void main(String[] args) throws FileNotFoundException, FileNotFoundException {
        File file = new File("C:\\Users\\User\\Desktop\\Java\\src\\demo.txt");
        FileReader fr = new FileReader(file);
    }
}
