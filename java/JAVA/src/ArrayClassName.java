public class ArrayClassName {
    public static void main(String[] args) {
        // declaring and initializing an array
        int[] arr = {1, 2, 3};

        // getting the class name of Java array
        Class c = arr.getClass();
        String name = c.getName();

        // printing the class name of Java array
        System.out.println(name);
    }
}
