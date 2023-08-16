package com.interswitch.service.salary.client;

import com.interswitch.service.salary.model.Department;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.*;

@FeignClient(name = "department-service")
public interface DepartmentClient {
    @GetMapping("/department/{departmentId}")
    public List<Department> findDepartmentById(@PathVariable("departmentId") Long departmentId);
}
