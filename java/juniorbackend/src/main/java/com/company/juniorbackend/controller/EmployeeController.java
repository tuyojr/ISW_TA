package com.company.juniorbackend.controller;

import com.company.juniorbackend.model.Employee;
import com.company.juniorbackend.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/employees")
public class EmployeeController {
    @Autowired
    private EmployeeService employeeService;

    // Create a new employee
    @PostMapping
    public ResponseEntity<Employee> createEmployee(@RequestBody Employee employee) {
        Employee newEmployee = employeeService.createEmployee(employee);
        return ResponseEntity.ok(newEmployee);
    }

    // Update an existing employee
    @PutMapping("/{employeeId}")
    public ResponseEntity<Employee> updateEmployee(@PathVariable Long employeeId, @RequestBody Employee employee) {
        Employee updatedEmployee = employeeService.updateEmployee(employeeId, employee);
        return ResponseEntity.ok(updatedEmployee);
    }

    // Retrieve all employees
    @GetMapping
    public ResponseEntity<List<Employee>> getAllEmployees() {
        List<Employee> employees = employeeService.getAllEmployees();
        return ResponseEntity.ok(employees);
    }

    // Retrieve an employee by ID
    @GetMapping("/{employeeId}")
    public ResponseEntity<Employee> getEmployeeById(@PathVariable Long employeeId) {
        Employee employee = employeeService.getEmployeeById(employeeId);
        return ResponseEntity.ok(employee);
    }

    // Get all employees for a specific salary rate
    @GetMapping("/salaryrates/{rateId}/employees")
    public ResponseEntity<List<Employee>> getEmployeesBySalaryRate(@PathVariable Long rateId) {
        List<Employee> employees = employeeService.getEmployeesBySalaryRate(rateId);
        return ResponseEntity.ok(employees);
    }

    // Get all employees for a specific department
    @GetMapping("/departments/{departmentId}/employees")
    public ResponseEntity<List<Employee>> getEmployeesByDepartment(@PathVariable Long departmentId) {
        List<Employee> employees = employeeService.getEmployeesByDepartment(departmentId);
        return ResponseEntity.ok(employees);
    }

    // Get all employees managed by a specific manager
    @GetMapping("/{employeeId}/employees")
    public ResponseEntity<List<Employee>> getEmployeesManagedByManager(@PathVariable Long employeeId) {
        List<Employee> employees = employeeService.getEmployeesManagedByManager(employeeId);
        return ResponseEntity.ok(employees);
    }
}
