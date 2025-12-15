import time

def computer_count_challenge():
    # 设定我们要数到的目标数字：一亿
    target_number = 100_000_000
    
    print("=" * 50)
    print(" 计算机 vs. 人类：数数大挑战！")
    print(f"目标：我们要从 1 数到 {target_number:,}")
    print("=" * 50)
    
    # 让学生猜一猜
    print("想一想：如果让你嘴巴不停地数，你要数多久？")
    print("准备好了吗？计算机要开始跑了！")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1... GO!")
    
    # --- 计时开始 ---
    start_time = time.time()
    
    # 计算机开始数数（循环）
    count = 0
    for i in range(target_number):
        count += 1
        
    # --- 计时结束 ---
    end_time = time.time()
    
    # 计算耗时
    time_taken = end_time - start_time
    
    print("\n" + "=" * 50)
    print("完成！")
    print("=" * 50)
    print(f" 计算机数完 1 亿个数字，只用了：{time_taken:.4f} 秒")
    
    # --- 趣味对比环节 ---
    # 假设人类每秒钟数 1 个数（其实数到后面数字很大，根本做不到1秒1个）
    seconds_in_year = 365 * 24 * 60 * 60
    human_years = target_number / seconds_in_year
    
    print("\n惊人的对比：")
    print(f"如果是一个人类每秒数 1 个数，不吃饭不睡觉...")
    print(f"数完这些数需要大约：{human_years:.2f} 年！")
    print("-" * 50)
    print("这就是为什么我们需要计算机来帮我们做科学计算！")

if __name__ == "__main__":
    computer_count_challenge()