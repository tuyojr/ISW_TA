package com.interswitch.service.salary.model;

public class Department {
    private Long id;

    public Department() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Department(Long id) {

        this.id = id;
    }

    @Override
    public String toString() {
        return "Department{" +
                "id=" + id +
                '}';
    }
}
