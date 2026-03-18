package com.tender.platform;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.tender.platform.mapper")
public class TenderPlatformApplication {
    public static void main(String[] args) {
        SpringApplication.run(TenderPlatformApplication.class, args);
    }
}
