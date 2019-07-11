#-*- coding:utf-8 -*-
"""
author:zx
"""
# 项目表信息
project_sql = '''
select 
	pj.projectLeve,pj.projectType,pj.projectClassName
from
	project as pj 
where 
	pj.projectLeve is not null
	and pj.projectClassName is not null 
	and pj.projectType is not null
'''
# 这里M0-M6表示项目金额分段，比如M1表示0-100000项目金额
# 这个SQL表示项目信息和金额表合并在一起了用来做数据挖掘
projectMoney_and_project_sql = '''
select 
	pj.projectLeve,pj.projectType,pj.projectClassName,(case when pjm.projectMoney between 0 and 100000 then 'M1'
	 when pjm.projectMoney between 100000 and 200000 then 'M2'
	 when pjm.projectMoney between 200000 and 300000 then 'M3'
	 when pjm.projectMoney between 300000 and 400000 then 'M4'
	 when pjm.projectMoney between 400000 and 500000 then 'M5'
	 when pjm.projectMoney > 500000 then  'M6'
	 else  'M0'
	 end )
from
	project as pj,
	projectMoney as pjm
where 
	pj.projectLeve is not null
	and pj.projectID = pjm.projectID
	and pj.projectClassName is not null 
	and pj.projectType is not null
'''
#paper表信息
paper_sql = '''
select
	ps.paperLever,ps.paperType,ps.projectAuditDesc
from 
	papers as ps 
where
	ps.paperLever is not null 
	and ps.paperType is not null
	and ps.projectAuditDesc is not null
'''
#patent表数据信息
patent_sql = '''
select 
    pt.patentLever,pt.patentType,pt.patentUnit,pt.projectAudit
from 
    patent as pt
where 
    pt.patentLever is not null 
    and pt.patentType is not null 
    and pt.patentUnit is not null
    and pt.projectAudit is not null
'''