import java.util.*;
public class Sets {
    public static void main(String[] args) {
        int[] count = {33, 44, 55, 55, 77, 88, 99};
        Set<Integer> set = new HashSet<Integer>();
        try {
            for (int i = 0; i < 5; i++) {
                set.add(count[i]);
            }
            System.out.println(set);
            TreeSet sortedSet = new TreeSet<Integer>(set);
            System.out.println("The sorted list is:");
            System.out.println(sortedSet);
            System.out.println("The First element in the set is: " + (Integer)sortedSet.first());
            System.out.println("The last element in the set is: " + (Integer)sortedSet.last());
            System.out.println("The size of the set is: " + (Integer)sortedSet.size());
        } catch (Exception e) {}
    }
}
