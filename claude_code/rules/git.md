# git 操作規範
## 執行方式
 - 執行 git 指令前，先讀取當前專案的 `CLAUDE.md` 取得 `container_name` 與 `project_path`
 - git 指令統一使用以下格式： `docker exec {container_name} git -C {project_path} <command>`
 - 禁止直接在 `/workspace` 執行 git 指令

## 缺少參數時
 - 若專案未配置 `container_name` 或 `project_path`，停止操作並提示用戶補充配置

## 唯讀操作（無需確認）
 - `git status`
 - `git log`
 - `git diff`
 - `git branch`

## 寫入操作（執行前需告知用戶）
### add
- 指令：`git add <file>`
- 說明：新增本次任務所有的異動。
- 規則：放入這次開發的所有異動。

### commit
- 指令：`git commit -m "<message>"`
- 說明：將本次任務內容以條列的方式寫在<message>中。
- 規則：-

### push
- 指令：`git push origin HEAD`
- 說明：將本次commit內容推送至branch源。
- 規則：-

### reset
- 指令：`git reset`
- 說明：-
- 規則：使用前必需先告知用戶。

### checkout
- 指令：`git checkout`
- 說明：-
- 規則：使用前必需先告知用戶。