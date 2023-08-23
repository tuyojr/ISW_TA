package com.interswitch.ajax;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Unmarshaller;

import java.io.File;

public class MapperTest {
    public static void main(String[] args) throws JAXBException {
        JAXBContext context = JAXBContext.newInstance(MapHelper.xmlMappingObjects);
        Unmarshaller unmarshaller = context.createUnmarshaller();
        File file = new File("person.xml");
        Person person = (Person) unmarshaller.unmarshal(file);
        System.out.println(person.toString());

        file = new File("student-course.xml");
        StudentCourse studentCourse = (StudentCourse) unmarshaller.unmarshal(file);
        person.setMyCourses(studentCourse.getCourses());
        System.out.println(person);
    }
}
