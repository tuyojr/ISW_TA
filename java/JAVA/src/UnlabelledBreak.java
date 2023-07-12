class UnlabelledBreak {
    public static void main(String[] args) {
        String[] arr = {"Shisui", "Fugaku", "Sasuke", "Itachi", "Madara", "Hagoromo"};
        String searchName = "Fugaku";

        int j;
        boolean foundIt = false;

        for (j = 0; j < arr.length; j++) {
            if (arr[j] == searchName) {
                foundIt = true;
                break;
            }
        }
        if (foundIt) {
            System.out.println(searchName + " found in the array at index " + j);
        } else {
            System.out.println(searchName + " not found in the array.");
        }
    }
}
