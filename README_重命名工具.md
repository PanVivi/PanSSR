# Clash节点自动重命名工具使用说明

## 问题背景
- ACL4SSR配置无法直接重命名节点
- 订阅更新后，手动重命名会失效
- 需要自动化解决方案

## 解决方案

### 方法1：订阅转换服务（推荐）
在**转换服务URL**中添加重命名参数：

**原始流程：**
1. 你的代理订阅链接：`https://your-proxy.com/sub`
2. 转换服务：`https://sub.example.com/sub?url=你的订阅链接&target=clash`

**添加重命名参数：**
```
https://sub.example.com/sub?url=你的订阅链接&target=clash&rename=日本|🇯🇵 JP&rename=美国|🇺🇲 US&rename=c28s4|🇯🇵 JP-01&rename=c28s1|🇺🇲 US-01
```

**完整示例：**
```
https://sub.example.com/sub?url=https://your-proxy.com/sub&target=clash&rename=日本|🇯🇵 JP&rename=美国|🇺🇲 US&rename=c28s4|🇯🇵 JP-01&rename=c28s1|🇺🇲 US-01&rename=c28s2|🇺🇲 US-02&rename=c28s3|🇺🇲 US-03
```

**这样转换后的Clash配置中，节点名字就会自动重命名！**

### 方法2：自动化脚本（适合本地处理）

#### 文件说明
- `auto_rename.py` - Python重命名脚本
- `rename_clash.bat` - 批处理工具（Windows）

#### 使用步骤

1. **获取Clash配置**
   - 从ACL4SSR生成或订阅转换获取config.yaml

2. **运行重命名**
   ```batch
   # 直接修改原文件
   rename_clash.bat config.yaml

   # 生成新文件
   rename_clash.bat config.yaml renamed_config.yaml
   ```

3. **导入Clash**
   - 将重命名后的文件导入Clash使用

#### 重命名规则
- 🇯🇵 JP-01 - c28s4节点
- 🇺🇲 US-01 - c28s1节点
- 🇺🇲 US-02 - c28s2节点
- 🇺🇲 US-03 - c28s3节点
- 🇺🇲 US-05 - c28s5节点
- 🇺🇲 US-801 - c28s801节点
- 🇯🇵 JP - 其他日本节点
- 🇺🇲 US - 其他美国节点

## 自动化集成

### Windows计划任务
创建计划任务，定期执行重命名：
```batch
schtasks /create /tn "ClashRename" /tr "C:\Path\To\rename_clash.bat config.yaml" /sc daily /st 09:00
```

### Linux/Mac Cron
```bash
0 9 * * * /path/to/python /path/to/auto_rename.py /path/to/config.yaml
```

## 优势
✅ **自动化** - 订阅更新后自动重命名
✅ **保持分组** - c28s标识仍用于自动分组
✅ **灵活配置** - 可自定义重命名规则
✅ **跨平台** - 支持Windows/Linux/Mac