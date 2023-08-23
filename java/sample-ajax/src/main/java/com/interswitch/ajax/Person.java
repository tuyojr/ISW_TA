package com.interswitch.ajax;

import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

import java.util.ArrayList;
import java.util.List;

@XmlRootElement
public class Person {
    private String name;
    private String address;
    private List<Courses> myCourses = new ArrayList<>();

    @XmlElement
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlElement
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @XmlElement
    public List<Courses> getMyCourses() {
        return myCourses;
    }

    public void setMyCourses(List<Courses> myCourses) {
        this.myCourses = myCourses;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", address='" + address + '\'' +
                ", myCourses=" + myCourses +
                '}';
    }
}
