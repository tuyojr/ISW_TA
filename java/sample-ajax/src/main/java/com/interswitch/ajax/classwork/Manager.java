package com.interswitch.ajax.classwork;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class Manager {
    @XmlElement(name = "name")
    private String name;

    @XmlElement(name = "phone-no")
    private PhoneNumber phoneNumber = new PhoneNumber();

    public String getManagerName() {
        return name;
    }

    public void setManagerName(String name) {
        this.name = name;
    }

    public PhoneNumber getManagerPhoneNumber() {
        return phoneNumber;
    }

    public void setManagerPhoneNumber(PhoneNumber phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    @Override
    public String toString() {
        return "Manager{" +
                "name='" + name + '\'' +
                ", phoneNumber=" + phoneNumber +
                '}';
    }
}
