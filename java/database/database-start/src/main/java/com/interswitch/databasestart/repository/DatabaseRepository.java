package com.interswitch.databasestart.repository;

import com.interswitch.databasestart.model.DatabaseModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DatabaseRepository extends JpaRepository<DatabaseModel, Long> {
}
