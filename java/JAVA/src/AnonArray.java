public class AnonArray {
    static void printArray(int arr[]) {
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
    }

    public static void main(String[] args) {
        printArray(new int[] { 10, 22, 44, 66 }); // passing anonymous array to method
    }
}
