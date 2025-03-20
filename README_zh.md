# MyTools

**MyTools** 是一个个人工具集合，包含一系列实用的自动化脚本和工具。其中，第一个工具是用于 **批量注册 Open5GS 订阅用户**，帮助简化 5G 核心网的用户管理。

[🔗 切换英文版本 (英文文档)](./README.md)

## 📌 工具 1：批量注册 Open5GS 订阅用户

该工具允许你在 **Open5GS** 中批量添加订阅用户。

### 🔧 **使用方法**
1. **修改 Open5GS Web UI 配置**
   - 编辑 `webui/server/index.js`
   - 注释掉 `server.use(csrf);` 这一行
   - 保存文件并重启 Web UI：
     ```sh
     systemctl restart open5gs-webui
     ```

2. **运行 Python 脚本**，修改想要添加的用户imsi范围和目标地址。
   ```sh
   python register_subscribers.py
   ```

3. **脚本执行后刷新网页**，你将会在 Open5GS 的数据库中看到批量添加的用户。

### 📜 **脚本逻辑**
- 连接 Open5GS Web UI API
- 依次创建 **180** 个 IMSI 订阅用户
- 发送 `POST` 请求，将用户数据存入 Open5GS 数据库
- 打印每个用户的注册状态（成功或失败）

## 🔮 未来计划
- 添加更多 Open5GS 相关的自动化工具
- 提供用户管理、QoS 监控、网络仿真等功能

> **📢 注意**：请确保 Open5GS 服务器已启用 API 访问，并且 CSRF 保护已禁用或正确配置，否则请求可能会失败。

🚀 **欢迎使用 MyTools，让 5G 核心网管理更高效！**