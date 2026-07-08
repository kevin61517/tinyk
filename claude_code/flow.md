## 🎨 原始碼風格
 - 變數/函數: `snake_case`
 - 類別: `PascalCase`
 - 語言: 註解與說明請使用 **繁體中文**，變數命名一率使用英文。

## 開發流程規範
### 定義
 - 任務管理路徑: `/issues`。
  - 說明: 存放所有任務的路徑。

 - 具體的任務位置: `/issues/<issue_number>`。
  - 說明: 存放具體任務的路徑。

 - 任務描述: `/issues/<issue_number>/issue.md`
  - 說明: 任務內容描述。

 - 任務聚焦: `/issues/<issue_number>/qa.md`
  - 說明: 寫入分析完 `/issues/<issue_number>/issue.md` 文件後「已知部分」與「待確認部分」，並且紀錄與需求方討論規格的過程。

 - 開發規格書: `/issues/<issue_number>/spec.md`
  - 說明: 根據 `/issues/<issue_number>/qa.md` 的內容，提出這次的開發計畫、規格與異動內容。

 - 本次開發討論上下文: `/issues/<issue_number>/context.md`
  - 說明: 作為遺失上下文時的關鍵文件，需要紀錄從閱讀 `issue.md` 文件開始至根據 `spec.md` 文件開發完成為止的所有上下文內容，每次有新的異動時都要總結到 `context.md` 文件中，並且文件頂端要有每次異動的更新日期。

### 工作流程
 - 獲得任務: 根據被告知的 <issue_number> 查詢路徑中對應的 `issue.md` 文件。
  - 若該 <issue_number> 路徑中包含 `context.md` 文件，優先閱讀 `context.md` 文件。
  - 若該 <issue_number> 路徑中不包含 `context.md` 文件，繼續工作流程。
 - 聽取故事: 分析 `issue.md` 內容並將已理解與不理解的部分寫入 `qa.md` 文件中並等待確認。
 - 確認故事: 根據 `qa.md` 文件中已核實的所有部分，將這次的開發規格內容寫入 `spec.md` 文件中並等待確認。
 - 開始開發: 根據 `spec.md` 文件中已核實的所有部分開始開發。
 - 開發完成: 紀錄這次開發的所有內容，從聽取故事開始至「根據 `spec.md` 文件」實作完成為止，之間的所有內容。

## 效能規範
### 禁止的寫法
 - 禁止雙層巢狀迴圈（`for` 內再套 `for`、`while` 內再套 `while`）
 - 禁止在迴圈內執行查找操作（如對 `list` 做 `in` 判斷、`.index()`、`.count()`）
 - 禁止對同一集合重複全量遍歷超過一次以完成同一任務

### 遇到需要 O(n²) 的情境時
 - 優先改用 `dict` 或 `set` 將查找降為 O(1)
 - 若確實無法避免，必須先提出說明並徵得使用者同意才能實作