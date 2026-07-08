---
name: issue
description: 執行 issue 開發流程。接收 issue 編號，依序完成 qa、spec、開發、context 四個階段。
argument-hint: "[issue_number]"
arguments: [issue_number]
disable-model-invocation: true
allowed-tools: Read Write Edit Glob Grep Bash
---

issue 編號：`$issue_number`

## Step 1｜取得任務
- 根據 issue 編號找到對應的任務資料夾
- 若資料夾中包含 `context.md` → 優先閱讀，任務已完成，依使用者指示行動
- 若存在 `spec.md` → 讀取 `spec.md`（任務進行中，規格已確認，直接進入開發）
- 若存在 `qa.md` → 讀取 `qa.md`（任務進行中，分析已完成，進入 Step 3）
- 否則 → 讀取 `issue.md`，從 Step 2 開始

## Step 2｜分析故事
- 將已理解的部分與待確認的部分寫入 `/issues/$issue_number/qa.md`
- `qa.md` 須遵守以下 Pattern：
  - 第一輪結尾加上 `## 問題答覆 1`，內容留空等待使用者填寫
  - 若使用者填寫後仍有新一輪問答，每輪依序遞增：`## 問題答覆 2`、`## 問題答覆 3`……
  - 每次新增提問時，在最新的「問題答覆」區塊**之後**附加新的問題段落，再接上下一個流水號的 `## 問題答覆 N` 結尾
- 寫完後停下來等待使用者確認，不得進行下一步

## Step 3｜確認規格
- 根據 qa.md 中已核實的內容撰寫 `/issues/$issue_number/spec.md`
- 內容包含：開發目標、異動清單
- `spec.md` 末端固定加上 `## 規格確認`，內容留空等待使用者填寫
- 寫完後停下來等待使用者確認，得到明確確認後才開始開發

## Step 4｜開發
- 依照 spec.md 的規格實作

## Step 5｜寫入 context.md
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
