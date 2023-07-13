import java.util.*;
public class Lists {
    public static void main(String[] args) {
        List first = new ArrayList();
        first.add("Gandalf");
        first.add(1);
        first.add(2);
        first.add("Harry");

        System.out.println(first);

        List second = new LinkedList();
        second.add("Gallahad");
        second.add(1);
        second.add(2);
        second.add("Hermionie");
        System.out.println();
        System.out.println(second);
    }
}
