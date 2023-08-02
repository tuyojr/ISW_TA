package com.company.juniorbackend.controller;

import com.company.juniorbackend.model.EmployeeCategory;
import com.company.juniorbackend.service.EmployeeCategoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/employeecategories")
public class EmployeeCategoryController {
    @Autowired
    private EmployeeCategoryService employeeCategoryService;

    @PostMapping
    public ResponseEntity<EmployeeCategory> createEmployeeCategory(@RequestBody EmployeeCategory employeeCategory) {
        EmployeeCategory newEmployeeCategory = employeeCategoryService.createEmployeeCategory(employeeCategory);
        return ResponseEntity.ok(newEmployeeCategory);
    }

    @PutMapping("/{categoryId}")
    public ResponseEntity<EmployeeCategory> updateEmployeeCategory(@PathVariable Long categoryId, @RequestBody EmployeeCategory employeeCategory) {
        EmployeeCategory updatedEmployeeCategory = employeeCategoryService.updateEmployeeCategory(categoryId, employeeCategory);
        return ResponseEntity.ok(updatedEmployeeCategory);
    }

    @GetMapping
    public ResponseEntity<List<EmployeeCategory>> getAllEmployeeCategories() {
        List<EmployeeCategory> employeeCategories = employeeCategoryService.getAllEmployeeCategories();
        return ResponseEntity.ok(employeeCategories);
    }

    @GetMapping("/{categoryId}")
    public ResponseEntity<EmployeeCategory> getEmployeeCategoryById(@PathVariable Long categoryId) {
        EmployeeCategory employeeCategory = employeeCategoryService.getEmployeeCategoryById(categoryId);
        return ResponseEntity.ok(employeeCategory);
    }
}
