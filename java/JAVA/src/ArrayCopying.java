public class ArrayCopying {
    // syntax:
    // System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length)
    public static void main(String[] args) {
        // declaring the source array
        char[] copyFrom = {'d', 'e', 'c', 'a', 'f', 'f', 'e',
                           'i', 'n', 'a', 't', 'e', 'd'};

        // declaring the destination array and the number of elements to be copied
        char[] copyTo = new char[7];

        // copying the elements from the source array to the destination array
        System.arraycopy(copyFrom, 2, copyTo, 0, 7);

        // printing the elements of the destination array
        System.out.println(new String(copyTo));
    }
}
