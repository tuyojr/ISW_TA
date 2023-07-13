public class ActivityOne {
    static int sqr(int a){
        return a * a;
    }

    static int[][] twoDArray(int a, int b){
        int[][] arr = new int[a][b];
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++){
                arr[i][j] = count++;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        System.out.println(sqr(4));
        int[][] x = twoDArray(3, 6);
        for (int[] i : x) {
            for (int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
