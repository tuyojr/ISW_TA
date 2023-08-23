package com.interswitch.ajax.classwork;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Unmarshaller;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class ClassTest {
    public static void main(String[] args) throws JAXBException {
        JAXBContext context = JAXBContext.newInstance(ClassMapHelper.xmlMappingObjects);
        Unmarshaller unmarshaller = context.createUnmarshaller();
        File file = new File("employee.xml");
        Employee employee = (Employee) unmarshaller.unmarshal(file);
//        System.out.println(employee.toString());

        JSONObject emp = new JSONObject(employee);
        System.out.println(emp);

        Employee e1 = (Employee) unmarshaller.unmarshal(file);
        Employee e2 = (Employee) unmarshaller.unmarshal(file);
        Employee e3 = (Employee) unmarshaller.unmarshal(file);
//        List<Employee> list = new ArrayList<>();
//        list.add(e1);
//        list.add(e2);
//        list.add(e3);
        JSONArray ja = new JSONArray(List.of(e1, e2, e3));
        System.out.println(ja);
    }
}