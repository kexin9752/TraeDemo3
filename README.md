# 随机壁纸助手 (Wallpaper Helper)

一个简单易用的跨平台随机壁纸设置工具，支持从本地文件夹和在线API获取并设置壁纸。

## 📋 项目介绍

**随机壁纸助手**是一款轻量级工具，帮助用户快速设置随机壁纸，提升桌面视觉体验。

### 核心功能

- **本地壁纸随机设置**：从指定文件夹中随机选择图片作为壁纸
- **在线壁纸获取**：从Picsum Photos API获取高质量随机壁纸
- **多系统支持**：兼容Windows、macOS和Linux操作系统
- **简洁直观的GUI界面**：友好的用户交互体验

### 应用场景

- 每天自动更换不同壁纸，保持桌面新鲜感
- 快速预览和设置本地图片集合
- 获取高质量的在线壁纸资源

## 🚀 快速开始

### 下载与使用

1. **直接下载可执行文件**
   - 访问[Release页面](https://github.com/kexin9752/TraeDemo3/releases/tag/v0.1.0)
   - 下载`wallpaper_helper.exe`文件
   - 双击运行即可使用

2. **从源码运行**
   ```bash
   # 克隆仓库
   git clone https://github.com/kexin9752/TraeDemo3.git
   cd TraeDemo3
   
   # 安装依赖
   pip install -r requirements.txt
   
   # 运行应用
   python wallpaper_helper.py
   ```

## 📦 打包流程

### 环境要求

- Python 3.6+
- pip包管理器

### 依赖安装

```bash
# 安装项目依赖
pip install -r requirements.txt
```

### 打包命令

```bash
# 生成单文件可执行文件
pyinstaller --onefile wallpaper_helper.py

# 或使用spec文件
pyinstaller wallpaper_helper.spec
```

### 打包配置

- `--onefile`：生成单个可执行文件
- 打包后文件位于`dist/`目录
- 支持Windows、macOS和Linux平台打包

## 📖 使用指南

1. **本地壁纸设置**
   - 点击"浏览"按钮选择本地壁纸文件夹
   - 点击"从本地随机设置"按钮
   - 系统会从选择的文件夹中随机选择一张图片作为壁纸

2. **在线壁纸设置**
   - 直接点击"从在线随机设置"按钮
   - 系统会自动从Picsum Photos API下载一张随机壁纸并设置

3. **系统支持**
   - Windows：直接支持
   - macOS：通过osascript命令设置
   - Linux：支持GNOME、KDE等常见桌面环境

## 📄 版本信息

### 当前版本
- **v0.1.0** (2026-01-21)

### 更新日志

#### v0.1.0 (2026-01-21)
- 首次发布
- 实现本地壁纸随机设置功能
- 实现在线壁纸获取功能
- 支持多系统平台
- 提供GUI操作界面

## 🛠️ 技术实现

- **语言**：Python 3
- **GUI框架**：Tkinter (Python标准库)
- **网络请求**：requests
- **图片处理**：Pillow
- **系统调用**：ctypes (Windows)、os.system (macOS/Linux)

## ⚠️ 已知限制

- 在线壁纸获取依赖网络连接
- 临时文件不会自动删除，可能占用少量磁盘空间
- Linux系统下部分桌面环境可能需要额外配置

## 📞 联系方式

- **GitHub**：[https://github.com/kexin9752/TraeDemo3](https://github.com/kexin9752/TraeDemo3)

## 📄 许可证

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件
