package com.interswitch.services.task.repository;

import com.interswitch.services.task.model.Task;

import java.util.*;

public class TaskRepository {
    private List<Task> tasks = new ArrayList<>();

    public Task add(Task newTask){
        newTask.setId((long) (tasks.size()+1));
        tasks.add(newTask);
        return newTask;
    }
    public List<Task> findTaskByEmployeeId(Long assignedTo){
        return tasks.stream()
                .filter(a -> a.getAssignedTo().equals(assignedTo))
                .toList();
    }

    public List<Task> findAll(){
        return tasks;
    }
}
