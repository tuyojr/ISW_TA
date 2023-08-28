package com.interswitch.ajax.classwork;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Unmarshaller;

import java.io.File;

public class StudentTest {


    public static void main(String[] args) throws JAXBException {
        JAXBContext context = JAXBContext.newInstance(StudentHelper.xmlMappingObjects);
        Unmarshaller unmarshaller = context.createUnmarshaller();
        File file = new File("student.xml");
        Student student = (Student) unmarshaller.unmarshal(file);
        System.out.println(student.toString());
    }
    // the main method above contains the code to unmarshal the XML file into a Java object
}
