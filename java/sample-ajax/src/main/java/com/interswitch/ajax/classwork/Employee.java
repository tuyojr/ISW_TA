package com.interswitch.ajax.classwork;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "employee")
@XmlAccessorType(XmlAccessType.FIELD)
public class Employee {

    @XmlElement(name = "name")
    private String name;

    @XmlElement(name = "phone-number")
    private PhoneNumber phoneNumber = new PhoneNumber();

    @XmlElement(name = "address")
    private Address address = new Address();

    @XmlElement(name = "department")
    private Department department = new Department();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhoneNumber getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(PhoneNumber phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "'" + name + '\'' +
                ", " + phoneNumber +
                ", " + address +
                ", " + department +
                '}';
    }
}
