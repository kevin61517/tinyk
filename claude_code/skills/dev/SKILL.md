---
name: dev
description: 讀取指定工單的 spec.md，確認規格已獲批准後直接進入開發。
argument-hint: "<issue_number>"
arguments: [issue_number]
disable-model-invocation: true
allowed-tools: Read Write Edit Glob Grep Bash
---

工單號：`$issue_number`

## Step 1｜讀取規格
讀取 `/issues/$issue_number/spec.md`：
- 若檔案不存在：提醒使用者「找不到 /issues/$issue_number/spec.md，請先執行 /issue $issue_number 完成規格撰寫」，並停止

## Step 2｜檢查規格確認狀態
找到 `## 規格確認` 區塊，檢查其下方內容：
- **若包含「確認」兩字**：直接進入 Step 3 開發
- **若不包含「確認」兩字**（空白或其他內容）：向使用者顯示目前的規格摘要，並詢問：「規格尚未確認，請確認後再繼續。是否確認此規格？」
  - 若使用者回覆確認：將「確認」寫入 spec.md 的 `## 規格確認` 區塊，再進入 Step 3
  - 若使用者未確認：停止

## Step 3｜開發
依照 spec.md 的規格實作。

## Step 4｜寫入 context.md
開發完成後，寫入 `/issues/$issue_number/context.md`：

```
# Context - $issue_number

## 更新日期：YYYY-MM-DD

## 任務摘要
一句話說明這個 issue 做了什麼。

## 最終規格
條列本次開發的規格內容。

## 關鍵決策
記錄開發過程中「為什麼這樣做而不是那樣做」的決策原因。

## 實作異動
條列所有異動的檔案與內容。
```
