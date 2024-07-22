package com.example.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import model.Vehicle;
import repository.SwitchRepository;

@EnableDiscoveryClient
@RestController
@RequestMapping("/switch")
public class SwitchController {

	@GetMapping("/status")
	public String status() {
		return "switch Service is up and running!";
	}

	@Autowired
	private SwitchRepository switchRepo;

	@GetMapping("/vehicle")
	public List<Vehicle> getAllvehicle() {
		return switchRepo.findAll();
	}

	@GetMapping("/vehicle/{vehicle_number}")
	public Vehicle getvehicleById(@PathVariable String vehicle_number) {
		return switchRepo.findById(vehicle_number).orElse(null);
	}

}
