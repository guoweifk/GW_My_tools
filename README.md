# MyTools


**MyTools** is a personal toolset that includes a collection of automated scripts and utilities. The first tool in this set is designed for **batch registering Open5GS subscribers**, simplifying 5G core network user management.

[🔗 Click here for the Chinese version (中文文档)](./README_zh.md)

## 📌 Tool 1: Batch Register Open5GS Subscribers

This tool allows you to **batch add subscribers** in Open5GS.

### 🔧 **Usage Instructions**
1. **Modify Open5GS Web UI Configuration**
   - Edit `webui/server/index.js`
   - Comment out the line `server.use(csrf);`
   - Save the file and restart the Web UI:
     ```sh
     systemctl restart open5gs-webui
     ```

2. **Run the Python script**, modifying the desired IMSI range and target address.
   ```sh
   python register_subscribers.py
   ```

3. **Refresh the web page after execution**, and you will see the newly added subscribers in the Open5GS database.

### 📜 **Script Logic**
- Connects to Open5GS Web UI API
- Iterates through and creates **180 IMSI subscriber records**
- Sends `POST` requests to store subscriber data in the Open5GS database
- Prints the registration status (success or failure) for each subscriber

## 🔮 Future Plans
- Add more Open5GS-related automation tools
- Provide user management, QoS monitoring, and network simulation features

> **📢 Note**: Ensure that the Open5GS server has API access enabled and that CSRF protection is either disabled or properly configured; otherwise, requests may fail.

🚀 **Welcome to MyTools – Making 5G Core Network Management More Efficient!**



