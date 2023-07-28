package com.interswitch.databasestart.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "customers", uniqueConstraints = {@UniqueConstraint(columnNames = "id"), @UniqueConstraint(columnNames = "phoneNumber")})
public class DatabaseModel {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "fullName")
    private String fullName;

    @Column(name = "phoneNumber", unique = true)
    private Long phoneNumber;

    @Column(name = "dateJoined")
    private String dateJoined;
}
