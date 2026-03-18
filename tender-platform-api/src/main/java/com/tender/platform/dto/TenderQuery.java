package com.tender.platform.dto;

import lombok.Data;

@Data
public class TenderQuery {
    private Integer page = 1;
    private Integer size = 20;
    private String keyword;
    private Integer type;
    private String region;
    private String industry;
}
