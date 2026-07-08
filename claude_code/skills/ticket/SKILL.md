---
name: ticket
description: 建立新工單資料夾與 issue.md 初始檔案。
argument-hint: "<TicketNumber>"
arguments: [ticket_number]
disable-model-invocation: true
allowed-tools: Read Write Bash
---

工單號：`$ticket_number`

## 參數驗證
1. 若 `$ticket_number` 為空：提醒使用者「請提供工單號，例如：/ticket CPN-0013」，並停止
2. 若 `$ticket_number` 的數字部分為 `latest`（例如 `CPN-latest`）：
   - 取出前綴（例如 `CPN`）
   - 掃描 `/issues/` 下所有符合 `前綴-數字` 格式的資料夾，找出最大數字 N
   - 若無任何現有工單，則 N = 0
   - 將 `$ticket_number` 替換為 `前綴-{N+1 補零至相同位數}`（例如最大為 `CPN-0010` → 生成 `CPN-0011`）
   - 繼續後續流程
3. 若 `$ticket_number` 不符合 `英文字母-數字` 格式（例如 `CPN-0011`、`OPS-0001`）：提醒使用者「工單號格式錯誤，請使用 英文字母-數字 的格式（例如：CPN-0011）」，並停止

## 建立工單
格式驗證通過後：
1. 檢查 `/issues/$ticket_number/` 是否已存在：若存在，提醒使用者「工單 $ticket_number 已存在，請直接編輯 /issues/$ticket_number/issue.md」，並停止
2. 在 `/issues/$ticket_number/` 建立資料夾
3. 建立 `/issues/$ticket_number/issue.md`，初始內容僅包含 `# 任務摘要`
4. 告知使用者：「工單 $ticket_number 已建立，請在 /issues/$ticket_number/issue.md 填入任務摘要。」
