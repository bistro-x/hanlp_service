# Hanlp_server 服务

整合 [HanLP](https://github.com/hankcs/HanLP) 提供分词的API服务 [HanLP文档](https://hanlp.hankcs.com/docs/)

## API

### 对文本句进行细颗粒度分词
- Method: **POST**
- Url: /participle
- Body:
```json
{
  "sentence": "阿婆主来到北京立方庭参观自然语义科技公司。"
}
```
- Response: 
```json
{
  "result": ["阿婆主", "来到", "北京", "立方庭", "参观", "自然", "语义", "科技", "公司", "。"]
}
```

### 对文本句进行词性识别
- Method: **POST**
- Url: /lexical
- Body:
```json
{
  "sentence": "阿婆主来到北京立方庭参观自然语义科技公司。"
}
```
- Response: 
```json
{
  "result": ["n", "v", "ns", "ns", "v", "n", "n", "n", "n", "w"]
}
```

## 环境要求

1. python 3.8+

## 文件目录说明

```filetree 
├── README.md -- 项目说明
├── run.py -- 程序运行文件
├── run.sh -- 容器运行脚本
├── /requirements.txt -- 项目使用到的依赖包
├── /Dockerfile -- 项目镜像构建文件
├── /resources/ -- 模型存放目录
```

## 部署/运行

```shell
python run.py
```

## 使用到的框架

```shell
hanlp
```