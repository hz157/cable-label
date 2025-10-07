// 
// Author: Ryan Zhang
// Date: 2025-08-08 21:37:59
// LastEditors: Ryan Zhang
// Email: ryanzhang@bytesycn.com
// LastEditTime: 2025-10-07 08:18:50
// FilePath: \static\script.js
// Repositories: https://github.com/hz157/cable-label
// Description: 
// 
// 
// Copyright (c) 2025 by Ryan Zhang, All Rights Reserved.
//

// File preview functionality
document.getElementById('file-upload').addEventListener('change', function() {
    const filePreview = document.getElementById('file-preview');
    if (this.files && this.files[0]) {
        filePreview.textContent = `Selected: ${this.files[0].name}`;
    } else {
        filePreview.textContent = '';
    }
});

// Update style preview
function updateStylePreview() {
    const styleList = [
        "[单行]\nStorageNode-1 OOBM\tFr: DELL_R550_IPMI\tTo: Cisco_C9300L_GE1",
        "[单行]\nStorageNode-1 OOBM\tFrom: DELL_R550_IPMI\tTo: Cisco_C9300L_GE1",
        "[单行]\n存储节点-1 带外管理\t本端: 戴尔_R550_IPMI\t对端: 思科_C9300L_GE1",
        "[单行]\nAct: StorageNode-1 OOBM\tFr: DELL_R550_IPMI\tTo: Cisco_C9300L_GE1",
        "[单行]\nAct: StorageNode-1 OOBM\tFrom: DELL_R550_IPMI\tTo: Cisco_C9300L_GE1",
        "[单行]\n用途: 存储节点-1 带外管理\t本端: 戴尔_R550_IPMI\t对端: 思科_C9300L_GE1",
        "[多行]\nAct: StorageNode-1 OOBM\nFr: DELL_R550_IPMI\nTo: Cisco_C9300L_GE1",
        "[多行]\nAct: StorageNode-1 OOBM\nFrom: DELL_R550_IPMI\nTo: Cisco_C9300L_GE1",
        "[多行]\n用途: 存储节点-1 带外管理\n本端: 戴尔_R550_IPMI\n对端: 思科_C9300L_GE1"
    ];
    
    const styleSelect = document.getElementById("style");
    const selectedStyle = styleList[styleSelect.value - 1];
    
    // Update preview
    document.getElementById("style-preview-text").textContent = selectedStyle;
}