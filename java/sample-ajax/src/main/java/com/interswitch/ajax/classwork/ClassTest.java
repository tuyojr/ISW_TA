package com.interswitch.ajax.classwork;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Unmarshaller;

import java.io.File;

public class ClassTest {
    public static void main(String[] args) throws JAXBException {
        JAXBContext context = JAXBContext.newInstance(ClassMapHelper.xmlMappingObjects);
        Unmarshaller unmarshaller = context.createUnmarshaller();
        File file = new File("employee.xml");
        Employee employee = (Employee) unmarshaller.unmarshal(file);
        System.out.println(employee.toString());
    }
}