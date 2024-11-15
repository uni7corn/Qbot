# 基金投资策略分析
![GitHub Repo stars](https://img.shields.io/github/stars/sunshowerc/fund-strategy)
![GitHub forks](https://img.shields.io/github/forks/sunshowerc/fund-strategy)
[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://sunshowerc.github.io/fund/)
![](https://img.shields.io/badge/-%E8%B4%A2%E5%AF%8C%E8%87%AA%E7%94%B1-red)


无需数据库，通过 jsonp 借用基金网站的数据接口，根据历史数据，通过图表展示效果。

对历史的各个时间点，符合一定的条件时，进行某些投资策略，包括定投，止盈，补仓等投资操作，最后进行投资策略成果分析，通过图表展示效果。

[在线访问地址：http://sunshowerc.github.io/fund/](http://sunshowerc.github.io/fund/)

> 由于用 github page 白嫖的，有墙，打不开就多刷新几次。

## 内容列表
- [背景](#背景)
- [安装](#安装)
- [开发](#开发)
- [使用说明](#使用说明)
  - [基础回测功能](#基础回测功能)
  - [策略对比](#策略对比)
- [感谢](#感谢)


## 背景

很多人都在鼓吹指数定投，微笑曲线，巴菲特鼎力推荐blabla，但割韭菜的大V太多，很容易被带节奏。

网上也有定投计算器，但往往只有一个结果，没有过程，不够得劲。

**数据不会说谎，用数据说话是程序员的浪漫。**

> 基于这个模型，也可以简单拓展成股票的交易模型，不过基于本人对炒股不是很熟，所以大家有兴趣的可以自行 fork 改造。

## 安装与运行
### 方式一
需要 node 开发环境
- npm
- node

```
npm install
```
运行命令
```
npm start
```

### 方式二
使用docker运行项目

在项目路径下运行以下命令构建项目的docker镜像
```
docker build -t fund_strategy .
```

镜像构建完毕后运行
```
docker run -dp 8000:8000 fund_strategy --name="fund_strategy_instance"
```

等待项目启动过程中，可通过以下命令查看启动日志：
```
docker logs -f fund_strategy_instance
```

启动后，可通过`http://locahost:8000`访问网页

## 使用说明
这是个开源的静态 web 仓库，无任何其他依赖。

开箱即用，[可在线访问]((http://sunshowerc.github.io/fund/))

### 基础回测功能

1. 输入你想要回测的基金，可以直接输入搜索。
2. 设置定投策略
3. 【可选】设置止盈策略
4. 【可选】设置补仓策略
5. 点击查询 
![image](https://user-images.githubusercontent.com/13402013/100250664-dfaa6800-2f78-11eb-936d-cc1acdad9c66.png)

 
### 策略对比
1. 保存两条及以上搜索条件
2. 点击策略对比
  ![image](https://user-images.githubusercontent.com/13402013/100251039-462f8600-2f79-11eb-93ed-45725c1da70f.png)

3. 将打开[策略对比页](http://sunshowerc.github.io/fund/#/compare), 勾选需要对比的策略条件，查询得到结果
  ![image](https://user-images.githubusercontent.com/13402013/100251436-bb9b5680-2f79-11eb-9ca3-51155368fee6.png)


## 感谢
- 感谢诸位的 star 👍 ，祝大家基金暴涨，早日财富自由。
- 感谢某基金网站提供白嫖数据的接口。


