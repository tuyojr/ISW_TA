package com.company.juniorbackend.controller;

import com.company.juniorbackend.model.Employee;
import com.company.juniorbackend.model.SalaryRate;
import com.company.juniorbackend.service.EmployeeService;
import com.company.juniorbackend.service.SalaryRateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/salaryrates")
public class SalaryRateController {
    @Autowired
    private SalaryRateService salaryRateService;
    @Autowired
    private EmployeeService employeeService;

    // Create a new salary rate
    @PostMapping
    public ResponseEntity<SalaryRate> createSalaryRate(@RequestBody SalaryRate salaryRate) {
        SalaryRate newSalaryRate = salaryRateService.createSalaryRate(salaryRate);
        return ResponseEntity.ok(newSalaryRate);
    }

    // Update an existing salary rate
    @PutMapping("/{rateId}")
    public ResponseEntity<SalaryRate> updateSalaryRate(@PathVariable Long rateId, @RequestBody SalaryRate salaryRate) {
        SalaryRate updatedSalaryRate = salaryRateService.updateSalaryRate(rateId, salaryRate);
        return ResponseEntity.ok(updatedSalaryRate);
    }

    // Retrieve all salary rates
    @GetMapping
    public ResponseEntity<List<SalaryRate>> getAllSalaryRates() {
        List<SalaryRate> salaryRates = salaryRateService.getAllSalaryRates();
        return ResponseEntity.ok(salaryRates);
    }

    // Retrieve a salary rate by ID
    @GetMapping("/{rateId}")
    public ResponseEntity<SalaryRate> getSalaryRateById(@PathVariable Long rateId) {
        SalaryRate salaryRate = salaryRateService.getSalaryRateById(rateId);
        return ResponseEntity.ok(salaryRate);
    }

    // Get all employees for a specific salary rate
    @GetMapping("/{rateId}/employees")
    public ResponseEntity<List<Employee>> getEmployeesBySalaryRate(@PathVariable Long rateId) {
        List<Employee> employees = employeeService.getEmployeesBySalaryRate(rateId);
        return ResponseEntity.ok(employees);
    }
}
