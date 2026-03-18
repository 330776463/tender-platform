package com.tender.platform.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.tender.platform.dto.TenderQuery;
import com.tender.platform.entity.Tender;
import com.tender.platform.service.TenderService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@Tag(name = "招标信息")
@RestController
@RequestMapping("/api/tender")
@RequiredArgsConstructor
public class TenderController {
    
    private final TenderService tenderService;
    
    @Operation(summary = "招标列表")
    @GetMapping("/list")
    public IPage<Tender> list(TenderQuery query) {
        return tenderService.queryPage(query);
    }
    
    @Operation(summary = "招标详情")
    @GetMapping("/{id}")
    public Tender detail(@PathVariable Long id) {
        return tenderService.getDetail(id);
    }
}
