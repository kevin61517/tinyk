---
name: start
description: 專案啟動流程，支援子指令：init（初始化環境）、setup（安裝依賴）
argument-hint: "[init|setup]"
arguments: [action]
allowed-tools: Read Write Edit Bash
---

子指令：`$action`

---

## init

若 `$action` 為 `init`，執行以下步驟：

1. 讀取 `CLAUDE.md`，取得 `container_name` 與 `project_path`

2. 若 `.claude` 不存在，則建立：
```bash
docker exec {container_name} bash -c "[ -d {project_path}/.claude ] || mkdir -p {project_path}/.claude"
```

3. 若 `tickets` 不存在，則建立：
```bash
docker exec {container_name} bash -c "[ -d {project_path}/tickets ] || mkdir -p {project_path}/tickets"
```

4. 若 `.claude/rules` 不存在，則從 AI 容器的 `/root/.claude/rules/` 複製：
```bash
docker exec {container_name} bash -c "[ -d {project_path}/.claude/rules ]" || docker cp /root/.claude/rules/. {container_name}:{project_path}/.claude/rules/
```

5. 若 `.claude/skills` 不存在，則從 AI 容器的 `/root/.claude/skills/` 複製：
```bash
docker exec {container_name} bash -c "[ -d {project_path}/.claude/skills ]" || docker cp /root/.claude/skills/. {container_name}:{project_path}/.claude/skills/
```

6. 若 `CLAUDE.md` 不存在，則從 `/root/.claude/rules/CLAUDE_TEMPLATE.md` 複製：
```bash
docker exec {container_name} bash -c "[ -f {project_path}/CLAUDE.md ]" || docker cp /root/.claude/rules/CLAUDE_TEMPLATE.md {container_name}:{project_path}/CLAUDE.md
```

7. 回報每個步驟是跳過（已存在）還是新建成功

---

## setup

若 `$action` 為 `setup`，執行以下步驟：

1. 讀取 `CLAUDE.md`，確認 `container_name` 與 `project_path`
2. 在容器內執行 `composer install`
3. 在容器內執行 `php artisan migrate`
4. 回報安裝結果

---

## 未知子指令

若 `$action` 不在上述清單內，回傳錯誤訊息：

```
未知的子指令：$action
可用指令：init、setup
```
