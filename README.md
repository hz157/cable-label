# 线缆标签格式化工具
<p align="left">🇨🇳 中文简体  |  <a title="English" href="README_en.md">🇬🇧 English</a>
  
<a href="https://www.gnu.org/licenses/gpl-3.0.html#license-text"><img src="https://img.shields.io/github/license/hz157/cable-label" alt="License: MIT"></a>
<a href="https://github.com/hz157/cable-label"><img src="https://img.shields.io/github/stars/hz157/cable-label" alt="Stars"></a> 
</p>

专为网络工程项目设计的线缆标签格式化工具，帮助团队实现线缆标签的标准化和统一化管理。适用于机房、数据中心等环境的线缆识别与标注工作。

<p align="center"><img src= "./docs/img1.png" width="500" /></p>

## ✨ 主要功能
- 📊 ​Excel 数据批量处理-支持批量导入和处理Excel格式的线缆数据
- 🏷️ ​多种标准化标签格式-提供9种标准标签格式选择
- 🔄 ​自动生成双向标签-自动生成本端↔对端的双向标识标签
- 💾 ​结果导出-处理结果可导出为Excel格式，方便打印和使用

## 🌐 在线使用
​立即体验: [线缆标签格式化工具](https://cable-label.bytesycn.cn) 
> 💡 ​访问提示: 该站点仅在中国提供服务，如果您身处中国以外的地区，将会遇到无法访问的情况，建议您通过本地部署方式使用本工具。

无需安装任何软件，直接上传Excel文件即可快速生成标准化线缆标签。

## 🖼️ 风格样例

``` bash
# Style 8
Act: StorageNode-1 OOBM
From: DELL_R550_IPMI
To: Cisco_C9300L_GE1

# Style 9
用途: 存储节点-1 带外管理
本端: 戴尔_R550_IPMI
对端: 思科_C9300L_GE1
```

## 💻 本地部署指南
如果您关心数据安全或需要离线使用，可以轻松在本地部署：

### 环境要求
- Python 3.7+
- pip 包管理工具

### 部署步骤
``` bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装依赖（若在中国可使用清华大学Tsinghua镜像加速安装依赖）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动应用
python app.py
```

启动后访问 http://localhost:5000 即可使用本地版本。

## 📖 使用方法
​- 准备数据-按照模板格式准备Excel文件，包含"Name"、"From"、"To"三列数据
​- 选择样式-从9种标准化标签格式中选择合适的样式
- ​上传处理-上传文件并生成标准化标签
- ​下载结果-获取格式化后的Excel文件

## 🏢 适用场景
- 🖥️ ​数据中心线缆管理-大型数据中心线缆标识与管理
- 📡 ​网络机房线缆标识-企业网络机房线缆标准化标识
- 🔌 ​综合布线系统-办公楼宇综合布线系统标签制作
- 🏢 ​企业IT基础设施-企业IT设备间线缆维护与管理

## ✅ 优势特点
- 🚀 ​提高效率-大幅提升线缆标签制作效率
- ✅ ​减少错误-自动化处理减少人为标注错误
- 🎯 ​统一标准-确保团队使用统一的标签标准
- 📦 ​批量处理-支持大量线缆数据的批量快速处理
