package com.interswitch.service.salary;

import com.interswitch.service.salary.model.Salary;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.springframework.util.Assert;
import com.interswitch.service.salary.repository.SalaryRepository;

import java.util.List;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class SalaryRepositoryTest {

    private static final SalaryRepository repository = new SalaryRepository();

    @Test
    @Order(1)
    void testAddDepartment() {
        Salary salary = new Salary(1L, 2563270L, "1999-12-22");
        salary = repository.add(salary);
        Assert.notNull(salary, "Salary is null.");
        Assert.isTrue(salary.getEmployeeId() == 1L, "Salary bad id.");
    }

    @Test
    @Order(2)
    void testFindAll() {
        List<Salary> salaries = repository.findAll();
        Assert.isTrue(salaries.size() == 1, "Departments size is wrong.");
        Assert.isTrue(salaries.get(0).getEmployeeId() == 1L, "Salary bad id.");
    }

//    @Test
//    @Order(3)
//    void testFindByOrganization() {
//        List<Salary> salaries = repository.findSalariesByEmployeeId(1L);
//        Assert.isTrue(salaries.size() == 1, "Departments size is wrong.");
//        Assert.isTrue(salaries.get(0).getId() == 1L, "Salary bad id.");
//    }

    @Test
    @Order(3)
    void testFindById() {
        Salary salary = repository.findSalaryByEmployeeId(1L);
        Assert.notNull(salary, "Salary not found.");
        Assert.isTrue(salary.getEmployeeId() == 1L, "Salary bad id.");
    }

}
