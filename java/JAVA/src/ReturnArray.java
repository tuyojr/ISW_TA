public class ReturnArray {
    static int[] get() {
        return new int[] { 10, 22, 44, 66 };
    }

    public static void main(String[] args) {
        int[] arr = get();
        for (int j : arr) System.out.print(j + " ");

        // ArrayIndexOutOfBoundsException
        int[] a = get();
        for(int i = 0; i <= a.length; i++){
            System.out.print(i); // 01234
            System.out.println(a[i]); // 10 22 44 66 Exception
        }
    }
}
