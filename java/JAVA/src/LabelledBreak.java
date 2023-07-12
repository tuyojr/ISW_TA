class LabelledBreak {
    public static void main(String[] args) {
        int j, k;

        //labelling the outermost loop
        outerMost:
        for(j = 1; j < 5; j++) {

            //labelling the innermost loop
            innerMost:
            for(k = 1; k < 3; k++) {
                System.out.println("j = " + j + " and k = " + k);

                // terminating the outermost loop
                if(j == 3) break outerMost;
            }
        }
    }
}
