import time

print("AI Commander 守衛進程已啟動...")
print("容器正在運行中，請使用 'docker exec' 進入容器。")

try:
    while True:
        time.sleep(60)  # 每分鐘睡一次，完全不占 CPU
except KeyboardInterrupt:
    print("守衛進程停止。")