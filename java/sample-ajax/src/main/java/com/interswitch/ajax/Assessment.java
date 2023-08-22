package com.interswitch.ajax;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Unmarshaller;

import java.io.File;

public class Assessment {
    public static void main(String[] args) throws JAXBException {
        JAXBContext studentContext = JAXBContext.newInstance(Student.class);
        Unmarshaller studentUnmarshaller = studentContext.createUnmarshaller();
        File studentFile = new File("student.xml");
        Student student = (Student) studentUnmarshaller.unmarshal(studentFile);

        JAXBContext courseContext = JAXBContext.newInstance(Course.class);
        Unmarshaller courseUnmarshaller = courseContext.createUnmarshaller();
        File courseFile = new File("course.xml");
        Course course = (Course) courseUnmarshaller.unmarshal(courseFile);
        student.getCourse().add(course);

        System.out.println(student);
    }
}
