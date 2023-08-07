package com.company.juniorbackend.model;

import lombok.*;
import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "Salary_Rate")
public class SalaryRate {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "id", nullable = false)
    private EmployeeCategory employeeCategory;

    @Column(nullable = false)
    private Integer level;

    @Column(nullable = false)
    private Integer amount;
}
