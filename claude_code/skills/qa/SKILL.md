---
name: qa
description: 管理指定工單的 QA 流程。讀取 qa.md 的當前狀態，判斷是繼續追問還是確認完畢。
argument-hint: "<issue_number>"
arguments: [issue_number]
disable-model-invocation: true
allowed-tools: Read Write Edit Bash
---

工單號：`$issue_number`

## 執行流程

### Step 1｜讀取現況
讀取 `/issues/$issue_number/qa.md`：
- 若檔案不存在：提醒使用者「找不到 /issues/$issue_number/qa.md，請先執行 /issue $issue_number 產生 QA 文件」，並停止

### Step 2｜判斷狀態
依照 qa.md 的內容判斷目前所在輪次：

**情況 A：最新的 `## 問題答覆 N` 區塊內容為空**
→ 使用者尚未回答，提醒使用者填寫答覆後再執行此指令，並停止

**情況 B：最新的 `## 問題答覆 N` 已有內容**
→ 根據答覆內容判斷：
- 若仍有需要確認的疑點：在 qa.md 末端補上新的問題段落，接著加上下一個流水號的 `## 問題答覆 N+1`（內容留空），告知使用者新問題已補充，停下等待
- 若所有疑點已釐清：回覆使用者「QA 已完成，可執行 /issue $issue_number 進入規格確認階段」，並停止

## qa.md 寫入規則
- 新問題段落緊接在最新「問題答覆」區塊之後
- 流水號從現有最大值 +1 遞增
- 每輪結尾固定為空白的 `## 問題答覆 N`，留給使用者填寫
