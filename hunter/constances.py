# -*- coding: utf-8 -*-
__author__ = 'Raymond'

university_keywords = {
    20:[u'加州理工学院',u'哈佛大学',u'牛津大学',u'斯坦福大学',u'剑桥大学',u'麻省理工学院',u'普林斯顿大学',u'加州大学伯克利分校',
        u'帝国理工学院',u'耶鲁大学',u'芝加哥大学',u'加州大学洛杉矶分校',u'苏黎世联邦理工学院',u'哥伦比亚大学',u'约翰霍普金斯大学',
        u'宾夕法尼亚大学',u'密歇根大学安娜堡分校',u'密西根大学安娜堡分校',u'杜克大学',u'康奈尔大学',u'多伦多大学',],
    18:[u'西北大学',u'伦敦大学学院',u'东京大学',u'卡耐基梅隆大学',u'新加坡国立大学',u'华盛顿大学',u'佐治亚理工学院',
        u'德克萨斯大学奥斯汀分校',u'伊利诺伊大学厄本那-香槟分校',u'慕尼黑大学',u'威斯康辛大学麦迪逊分校',u'英属哥伦比亚大学',
        u'墨尔本大学',u'洛桑联邦理工学院',u'伦敦政治经济学院',u'爱丁堡大学',u'加州大学圣塔芭芭拉分校',u'纽约大学',u'麦吉尔大学',
        u'伦敦大学国王学院',u'加州大学圣地亚哥分校',u'圣路易斯华盛顿大学',u'香港大学',u'卡罗琳医学院',u'澳州国立大学',
        u'明尼苏达大学双城分校',u'北卡罗来纳大学教堂山分校',u'北京大学',u'清华大学',u'首尔国立大学',u'香港科技大学',
        u'韩国高等科技学院',u'曼彻斯特大学',u'布朗大学',u'加州大学戴维斯分校',u'鲁汶大学(荷语）',u'波士顿大学',
        u'宾州州立大学公园分校',u'京都大学',u'悉尼大学',u'巴黎高等理工学院',u'南洋理工大学',u'比萨高等师范学院',u'莱顿大学',
        u'昆士兰大学',u'浦项科技大学',u'哥廷根大学',u'俄亥俄州立大学',u'莱斯大学',u'海德堡大学',u'代尔夫特理工大学',
        u'鹿特丹伊拉斯姆斯大学',u'瓦格宁根大学',u'布里斯托大学',u'巴塞尔大学',u'南加州大学',u'阿姆斯特丹大学',u'巴黎高等师范学院',
        u'乌得勒支大学',u'柏林洪堡大学',u'柏林自由大学',u'密歇根州立大学',u'杜伦大学',u'莫纳什大学',u'中东理工大学',u'亚利桑那大学',
        u'圣母大学',u'加州大学尔湾分校',u'塔夫斯大学',u'根特大学',u'马萨诸塞大学阿默斯特分校',u'匹兹堡大学',u'艾茉莉大学',
        u'格拉斯哥大学',u'麦克马斯特大学',u'范德堡大学',u'科罗拉多大学博尔德分校',u'斯德哥尔摩大学',u'慕尼黑工业大学',u'乌普萨拉大学',],
    16:[u'上海交通大学',u'武汉大学',u'浙江大学',u'中国人民大学',u'南京大学',u'吉林大学',u'中山大学',u'复旦大学',],
    14:[u'上海财经大学',u'对外经济贸易大学',u'中央财经大学',u'西南财经大学',u'首都经济贸易大学',],
    12:[u'北京师范大学',u'华中科技大学',u'四川大学',u'中国科学技术大学',u'南开大学',u'山东大学',u'中南大学',u'西安交通大学',
        u'厦门大学',u'哈尔滨工业大学',u'北京航空航天大学',u'同济大学',u'天津大学',u'华东师范大学',u'东南大学',u'中国农业大学',
        u'华南理工大学',u'湖南大学',u'西北工业大学',u'大连理工大学',u'北京协和医学院',u'北京理工大学',u'重庆大学',u'东北大学',
        u'中国矿业大学',u'华中师范大学',u'西北大学',u'兰州大学',u'北京科技大学',u'东北师范大学',u'华东理工大学',u'电子科技大学',
        u'长安大学',u'中国地质大学',u'华中农业大学',u'北京交通大学',u'南京农业大学',u'中国海洋大学',u'南京理工大学',u'武汉理工大学',],
    10:[u'西南大学',u'苏州大学',u'西北农林科技大学',u'南京师范大学',u'中国石油大学',u'云南大学',u'哈尔滨工程大学',u'南京航空航天大学',
        u'河海大学',u'湖南师范大学',u'西南交通大学',u'暨南大学',u'北京化工大学',u'郑州大学',u'西安电子科技大学',u'北京林业大学',
        u'中国政法大学',u'合肥工业大学',u'北京邮电大学',u'华南师范大学',u'陕西师范大学',u'中南财经政法大学',u'上海大学',
        u'上海财经大学',u'山西大学',u'北京工业大学',u'福州大学',u'南昌大学',u'首都医科大学',u'中央民族大学',u'江南大学',
        u'东华大学',u'辽宁大学',u'华南农业大学',u'太原理工大学',u'首都师范大学',u'新疆大学',u'安徽大学',u'河南大学',u'海南大学',
        u'华北电力大学',u'东北林业大学',u'浙江工业大学',u'福建师范大学',u'内蒙古大学',u'中央财经大学',u'西南财经大学',u'深圳大学',
        u'广西大学',u'贵州大学',],
}

job_keywords = {
    30:[u'高盛',u'摩根士丹利',u'摩根大通',u'美银美林',u'德意志银行',u'瑞士信贷',u'瑞银集团',u'野村',u'汇丰',u'渣打',u'花旗',
        u'中金',u'巴克莱',u'法国巴黎银行',u'麦格理',u'凯雷',u'KKR',u'黑石',u'IDG',u'贝塔斯曼',u'鼎晖投资',u'淡马锡',u'CVC',
        u'麦肯锡',u'贝恩',u'波士顿咨询',u'Goldman',u'Morgan Stanley',u'JP Morgan',u'BAML',u'UBS',u'Nomura',u'HSBC',u'citi',
        u'CICC',u'Barclays',u'BNP',u'CDH',u'McKinsey',u'Bain',u'BCG'],
    26:[u'中信证券',u'海通证券',u'国泰君安',u'中国工商银行',u'中国建设银行',u'中国银行',u'天弘基金',u'华夏基金',u'嘉实基金',
        u'易方达基金',u'中信信托',u'平安信托',u'中诚信托',u'中国人寿',u'中国人保',u'中国平安',u'普华永道',u'德勤',u'毕马威',
        u'安永',u'春华资本',u'红杉资本',u'君联资本',u'九鼎投资',u'高翎资本',u'软银赛富',u'磐石基金',u'通用创投',u'凯鹏华盈',
        u'兰馨亚洲',u'复星资本',u'厚朴投资',u'弘毅投资',u'经纬中国',u'北极光创投',u'华平投资',u'方源资本',u'戈壁',u'罗兰贝格',
        u'埃森哲',u'美世咨询',u'思略特',u'科尔尼',u'致盛',u'怡安翰威特',u'韬睿惠悦',u'中信',u'海通',u'工商银行',u'建设银行',
        u'中行',u'天弘',u'华夏',u'嘉实',u'易方达',u'Pwc',u'Deloitte',u'KPMG',u'Roland Berger',u'Accenture',u'美世',
        u'Strategy&',u'ATK',u'ZS Associates',u'Aon Hewitt',u'Towers Waston',u'工行',u'建行',u'Ernst&Young',u'RB',
        u'Mercer',u'Aon',],
    22:[u'广发证券',u'华泰证券',u'招商证券',u'国信证券',u'银河证券',u'中信建投',u'申银万国',u'中国农业银行',u'交通银行',u'招商银行',
        u'中信银行',u'浦东发展银行',u'兴业银行',u'民生银行',u'工银瑞信',u'中银基金',u'广发基金',u'建信基金',u'招商基金',
        u'汇添富基金',u'博时基金',u'上投摩根基金',u'华润深国投信托',u'对外经济贸易信托',u'上海国际信托',u'华融国际信托',
        u'中融国际信托',u'华宝信托',u'建信信托',u'太平洋保险',u'新华保险',u'中国太平',u'泰康人寿',u'安邦保险',u'生命人寿',
        u'阳光保险',u'申万',u'农业银行',u'交行',u'招行',u'浦发银行',u'兴业',u'民生',u'工银瑞信基金',u'汇添富',u'博时',u'上投摩根',
        u'深国投信托',u'外贸信托',u'华融信托',u'中融信托',u'农行',],
    20:[u'银行',u'信托公司',u'保险公司',u'基金公司',u'投资管理公司',u'投资公司']
}

work_keywords = {
    10:[u'分析',u'投资',u'产品',u'项目',u'销售',u'交易',u'助理',u'行业研究',u'市场研究',u'风险控制',u'风控',u'策划',u'助理研究',
        u'市场拓展',u'公司研究',u'风险管理',u'会计',u'审计',u'数据运营',u'业务',u'管理培训',u'策略',u'宏观',u'咨询',u'柜员',u'客户',]
}

leadership_keywords = {
    10:[u'学生会主席',u'会长',u'组长',u'创始人',u'创办人',u'副主席',u'团委书记',u'团委副书记',],
    8:[u'部长',u'副部长',u'副部',u'团支书',u'班长',],
}

degree_keywords = {
    10:[u'博士'],
    8:[u'硕士',u'研究生'],
    6:[u'学士',u'本科']
}

# GPA and ranking not resolved!
study_keywords = {
    5:[u'前5%',u'top 5%',u'国家奖学金',u'综合奖学金'],
    4:[u'前10%',u'top 10%',u'一等奖学金'],
    3:[u'前20%',u'top 20%',u'二等奖学金']
}

skill_keywords = {
    5:[u'CFA三级',u'CPA全科',u'Bloomberg',u'FRM二级'],
    4:[u'CFA二级',u'CPA三科',u'CPA四科',u'Wind',u'STATA',u'SAS',u'SPSS',u'Matlab',u'FRM一级',u'CGA',u'ACCA',u'CICPA',],
}


major_keywords = {
    5:[u'金融',u'投资',u'金融工程',u'保险',u'统计',u'国际经济与贸易',u'财政',u'精算',u'经济学',u'会计'],
    4:[u'工商管理',u'市场营销',u'管理学',u'营销学',u'人力资源',u'财务管理',u'经济法']
}

# Language test not resolved!
language_keywords = {
    5:[u'日语',u'德语',u'法语',u'西班牙语',u'葡萄牙语'],
}
