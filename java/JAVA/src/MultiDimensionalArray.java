public class MultiDimensionalArray {
    // syntax:
    // data_type[][] array_name = new data_type[row_size][column_size];

    static int[][] multiArray() {
        int[][] arr = {{ 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 }};
        return arr;
    }

    public static void main(String[] args) {
        for(int i = 0; i < multiArray().length; i++){
            for(int j = 0; j < multiArray()[i].length; j++){
                System.out.print(multiArray()[i][j] + " ");
            }
            System.out.println();
        }
    }
}
