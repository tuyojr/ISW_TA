package com.interswitch.ajax;


import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

import java.util.ArrayList;

@XmlRootElement(name = "studentCourse")
@XmlAccessorType(XmlAccessType.FIELD)
public class StudentCourse {
    @XmlElement(name = "course")
    private ArrayList<Courses> courses = new ArrayList<>();

    public ArrayList<Courses> getCourses() {
        return courses;
    }

    public void setCourses(ArrayList<Courses> courses) {
        this.courses = courses;
    }

    @Override
    public String toString() {
        return "StudentCourse{" +
                "courses=" + courses +
                '}';
    }
}
