package com.interswitch.services.task.controller;

import com.interswitch.services.task.model.Task;
import com.interswitch.services.task.repository.TaskRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TaskController {
    private static final Logger LOGGER = LoggerFactory.getLogger(TaskController.class);

    @Autowired
    TaskRepository repository;

    public TaskController(TaskRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/{assignedTo}")
    public List<Task> findTaskByEmployeeID(@PathVariable("assignedTo") Long assignedTo) {
        LOGGER.info("Task find: assignedTo={}", assignedTo);
        return repository.findTaskByEmployeeId(assignedTo);
    }
}
