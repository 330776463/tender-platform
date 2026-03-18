package com.tender.platform.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.tender.platform.dto.TenderQuery;
import com.tender.platform.entity.Tender;
import com.tender.platform.mapper.TenderMapper;
import com.tender.platform.service.TenderService;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

@Service
public class TenderServiceImpl extends ServiceImpl<TenderMapper, Tender> implements TenderService {

    @Override
    public IPage<Tender> queryPage(TenderQuery query) {
        Page<Tender> page = new Page<>(query.getPage(), query.getSize());
        
        LambdaQueryWrapper<Tender> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(StringUtils.hasText(query.getType()), Tender::getType, query.getType())
               .like(StringUtils.hasText(query.getKeyword()), Tender::getTitle, query.getKeyword())
               .eq(StringUtils.hasText(query.getRegion()), Tender::getRegion, query.getRegion())
               .orderByDesc(Tender::getPublishTime);
        
        return page(page, wrapper);
    }

    @Override
    public Tender getDetail(Long id) {
        return getById(id);
    }
}
