package repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import model.Vehicle;

public interface SwitchRepository extends MongoRepository<Vehicle, String> {
}
