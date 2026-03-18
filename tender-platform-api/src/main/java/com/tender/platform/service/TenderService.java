package com.tender.platform.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;
import com.tender.platform.dto.TenderQuery;
import com.tender.platform.entity.Tender;

public interface TenderService extends IService<Tender> {
    IPage<Tender> queryPage(TenderQuery query);
    Tender getDetail(Long id);
}
