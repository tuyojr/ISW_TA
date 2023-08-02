package com.company.juniorbackend.service;

import com.company.juniorbackend.model.Department;

import java.util.*;

public interface DepartmentService {
    Department createDepartment(Department department);

    Department updateDepartment(Long departmentId, Department department);

    List<Department> getAllDepartments();

    Department getDepartmentById(Long departmentId);
}
