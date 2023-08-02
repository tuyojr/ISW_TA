package com.company.juniorbackend.service;

import com.company.juniorbackend.model.Employee;

import java.util.*;

public interface EmployeeService {
    Employee createEmployee(Employee employee);
    Employee updateEmployee(Long employeeId, Employee employee);
    List<Employee> getAllEmployees();
    Employee getEmployeeById(Long employeeId);
    List<Employee> getEmployeesBySalaryRate(Long rateId);
    List<Employee> getEmployeesByDepartment(Long departmentId);
    List<Employee> getEmployeesManagedByManager(Long managerId);
}
