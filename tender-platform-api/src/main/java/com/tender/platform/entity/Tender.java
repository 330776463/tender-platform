package com.tender.platform.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@TableName("t_tender")
public class Tender {
    @TableId(type = IdType.AUTO)
    private Long id;
    
    private String title;
    private String tenderNo;
    private Integer type;
    private Integer budget;
    private String region;
    private String industry;
    private String source;
    private String content;
    private LocalDateTime publishTime;
    private LocalDateTime deadline;
    private String tenderer;
    private String agent;
    private Integer status;
    
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;
    
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
    
    @TableLogic
    private Integer deleted;
}
