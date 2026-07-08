# Docker 操作規範

## 禁止事項
- 嚴禁執行任何會停止、刪除、重啟容器的指令，包括但不限於：
  - `docker stop`
  - `docker kill`
  - `docker rm`
  - `docker restart`
  - `docker-compose down`
  - `docker-compose restart`

- 嚴禁修改其他容器的設定或網路配置。
- 嚴禁執行 `docker system prune` 或任何清理指令。

## 允許事項（唯讀操作）
- 可執行查詢類指令：
  - `docker ps`
  - `docker logs`
  - `docker inspect`
  - `docker stats`

## 例外處理
- 若任務確實需要操作容器，必須先告知用戶並取得明確同意，再執行。