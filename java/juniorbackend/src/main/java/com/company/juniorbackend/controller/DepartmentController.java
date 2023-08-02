package com.company.juniorbackend.controller;

import com.company.juniorbackend.model.Department;
import com.company.juniorbackend.service.DepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/departments")
public class DepartmentController {
    @Autowired
    private DepartmentService departmentService;

    // Create a new department
    @PostMapping
    public ResponseEntity<Department> createDepartment(@RequestBody Department department) {
        Department newDepartment = departmentService.createDepartment(department);
        return ResponseEntity.ok(newDepartment);
    }

    // Update an existing department
    @PutMapping("/{departmentId}")
    public ResponseEntity<Department> updateDepartment(@PathVariable Long departmentId, @RequestBody Department department) {
        Department updatedDepartment = departmentService.updateDepartment(departmentId, department);
        return ResponseEntity.ok(updatedDepartment);
    }

    // Retrieve all departments
    @GetMapping
    public ResponseEntity<List<Department>> getAllDepartments() {
        List<Department> departments = departmentService.getAllDepartments();
        return ResponseEntity.ok(departments);
    }

    // Retrieve a department by ID
    @GetMapping("/{departmentId}")
    public ResponseEntity<Department> getDepartmentById(@PathVariable Long departmentId) {
        Department department = departmentService.getDepartmentById(departmentId);
        return ResponseEntity.ok(department);
    }
}
