package com.example;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class SonarQubeTest {

    // Hardcoded credentials (Vulnerability)
    private static final String DB_USER = "admin";
    private static final String DB_PASS = "password123";

    public static void main(String[] args) {
        SonarQubeTest test = new SonarQubeTest();
        test.run();
    }

    public void run() {
        // Unused variable (Code Smell)
        int unusedVariable = 10;

        // Hardcoded SQL query with potential SQL injection (Vulnerability)
        String userInput = "'; DROP TABLE users; --";
        executeQuery("SELECT * FROM users WHERE name = '" + userInput + "'");

        // Empty try-catch block (Code Smell)
        try {
            readFile("test.txt");
        } catch (Exception e) {
            // ignored
        }

        // Recursive call without exit condition (Bug)
        infiniteLoop();
    }

    // Method with exception handling issues (Code Smell)
    public void readFile(String filePath) throws IOException {
        File file = new File(filePath);
        FileInputStream fis = new FileInputStream(file);
        fis.read();
        fis.close();
    }

    // SQL Injection Risk (Vulnerability)
    public void executeQuery(String query) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", DB_USER, DB_PASS);
            Statement stmt = conn.createStatement();
            stmt.execute(query);
            conn.close();
        } catch (Exception e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }

    // Infinite loop (Bug)
    public void infiniteLoop() {
        while (true) {
            System.out.println("This loop never ends!");
        }
    }
}
