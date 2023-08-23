package com.interswitch.ajax.classwork;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "phone-number")
@XmlAccessorType(XmlAccessType.FIELD)
public class PhoneNumber {
    @XmlElement(name = "work")
    private String work;

    @XmlElement(name = "home")
    private String home;

    public String getWork() {
        return work;
    }

    public void setWork(String work) {
        this.work = work;
    }

    public String getHome() {
        return home;
    }

    public void setHome(String home) {
        this.home = home;
    }

    @Override
    public String toString() {
        return "Phone Number{" +
                "work='" + work + '\'' +
                ", home='" + home + '\'' +
                '}';
    }
}
