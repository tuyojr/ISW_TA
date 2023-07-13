public class ArrayCloning {
    public static void main(String[] args) {
        int[] mainArr = {33, 44, 55, 66, 77};
        System.out.println("Displaying original array");
        for(int i: mainArr) System.out.println(i);

        System.out.println();

        System.out.println("Getting and displaying cloned array.");
        int[] clonedArr = mainArr.clone();
        // update an index of cloned array
        clonedArr[0] = 99;
        for(int i: clonedArr) System.out.println(i);

        System.out.println();

        System.out.println("Are both arrays equal?");
        System.out.println(mainArr == clonedArr);
    }
}
