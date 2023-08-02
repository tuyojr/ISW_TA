package com.company.juniorbackend.service.impl;

import com.company.juniorbackend.model.Employee;
import com.company.juniorbackend.repository.EmployeeRepository;
import com.company.juniorbackend.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmployeeServiceImpl implements EmployeeService {
    private final EmployeeRepository employeeRepository;

    @Autowired
    public EmployeeServiceImpl(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }


    @Override
    public Employee createEmployee(Employee employee) {
        return employeeRepository.save(employee);
    }

    @Override
    public Employee updateEmployee(Long employeeId, Employee employee) {
        Employee existingEmployee = employeeRepository.findById(employeeId).orElse(null);
        if (existingEmployee != null) {
            existingEmployee.setName(employee.getName());
            existingEmployee.setPhone(employee.getPhone());
            existingEmployee.setAddress(employee.getAddress());
            existingEmployee.setDateOfBirth(employee.getDateOfBirth());
            return employeeRepository.save(existingEmployee);
        }
        return null;
    }

    @Override
    public List<Employee> getAllEmployees() {
        return employeeRepository.findAll();
    }

    @Override
    public Employee getEmployeeById(Long employeeId) {
        return employeeRepository.findById(employeeId).orElse(null);
    }

    @Override
    public List<Employee> getEmployeesBySalaryRate(Long rateId) {
        return employeeRepository.findBySalaryRateId(rateId);
    }

    @Override
    public List<Employee> getEmployeesByDepartment(Long departmentId) {
        return employeeRepository.findByDepartmentId(departmentId);
    }

    @Override
    public List<Employee> getEmployeesManagedByManager(Long managerId) {
        return employeeRepository.findByManagerId(managerId);
    }
}
