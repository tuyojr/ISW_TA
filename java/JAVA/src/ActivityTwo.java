// Write a program to store information of students which may include ID, name, course.
// Store 5 student information and display them using a map. Information must be secured in an object.

import java.util.*;

public class ActivityTwo {

    private int studentID;
    private String studentName;
    private String studentCourse;

    public int getStudentID() {
        return studentID;
    }

    public String getName() {
        return studentName;
    }

    public String getCourse() {
        return studentCourse;
    }

    public void setStudentID(int studentID) {
        this.studentID = studentID;
    }

    public void setName(String studentName) {
        this.studentName = studentName;
    }

    public void setCourse(String studentCourse) {
        this.studentCourse = studentCourse;
    }

//    create 5 students
    public static void main(String[] args) {
//        Map<Integer, String> students = new HashMap<>();
        Map<Integer, ActivityTwo> students = new HashMap<>();
        ActivityTwo student1 = new ActivityTwo();
        student1.setStudentID(221);
        student1.setName("Sherlock");
        student1.setCourse("Sociopath");

        ActivityTwo student2 = new ActivityTwo();
        student2.setStudentID(7);
        student2.setName("Bond");
        student2.setCourse("Spying");

        ActivityTwo student3 = new ActivityTwo();
        student3.setStudentID(97);
        student3.setName("BNXN");
        student3.setCourse("Music");

        ActivityTwo student4 = new ActivityTwo();
        student4.setStudentID(1917);
        student4.setName("Captain");
        student4.setCourse("Soldier");

        ActivityTwo student5 = new ActivityTwo();
        student5.setStudentID(10);
        student5.setName("Messi");
        student5.setCourse("Football");

//        students.put(student1.getStudentID(), student1.getName() + " " + student1.getCourse());
//        students.put(student2.getStudentID(), student2.getName() + " " + student2.getCourse());
//        students.put(student3.getStudentID(), student3.getName() + " " + student3.getCourse());
//        students.put(student4.getStudentID(), student4.getName() + " " + student4.getCourse());
//        students.put(student5.getStudentID(), student5.getName() + " " + student5.getCourse());
        students.put(student1.getStudentID(), student1);
        students.put(student2.getStudentID(), student2);
        students.put(student3.getStudentID(), student3);
        students.put(student4.getStudentID(), student4);
        students.put(student5.getStudentID(), student5);

        System.out.println();
        System.out.println("Map Elements");
        System.out.println("\t" + students);
    }
}
