package com.interswitch.ajax;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;

import java.io.File;
import java.io.StringWriter;

public class PersonTest {
    public static void main(String[] args) throws JAXBException {
        Person person = new Person();
        person.setName("Itachi Uchiha");
        person.setAddress("7, Uchiha District, Konohagakure.");

        JAXBContext context = JAXBContext.newInstance(Person.class);
        Marshaller marshaller = context.createMarshaller();

        StringWriter writer = new StringWriter();
        marshaller.marshal(person, writer);
        System.out.println(writer);

        // Unmarshaller
        Unmarshaller unmarshaller = context.createUnmarshaller();
        File file = new File("person.xml");
        Person person1 = (Person) unmarshaller.unmarshal(file);
        System.out.println(person1);
    }
}
