import asyncio
import librosa
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# 全局线程池用于执行阻塞操作
executor = ThreadPoolExecutor(max_workers=4)


async def async_get_instant_amplitude(mp3_path, target_freq, target_time, n_fft=2048):
    """
    异步获取瞬时频率振幅
    """
    loop = asyncio.get_running_loop()

    # 异步执行阻塞的IO和计算操作
    def _sync_task():
        y, sr = librosa.load(mp3_path, sr=None, mono=True)
        stft = librosa.stft(y, n_fft=n_fft)
        magnitude = np.abs(stft)
        freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
        times = librosa.frames_to_time(range(stft.shape[1]), sr=sr, hop_length=n_fft // 4)
        return magnitude, freqs, times, sr

    # 在线程池中执行同步任务
    magnitude, freqs, times, sr = await loop.run_in_executor(executor, _sync_task)

    # 主线程计算部分
    frame_idx = np.argmin(np.abs(times - target_time))
    freq_idx = np.argmin(np.abs(freqs - target_freq))
    return magnitude[freq_idx, frame_idx]


async def batch_analysis(tasks):
    """
    批量执行异步分析任务
    """
    # 创建异步任务列表
    coroutines = [
        async_get_instant_amplitude(
            task["path"],
            task["freq"],
            task["time"]
        )
        for task in tasks
    ]

    # 并行执行所有任务
    results = await asyncio.gather(*coroutines, return_exceptions=True)

    # 处理结果
    for task, result in zip(tasks, results):
        if isinstance(result, Exception):
            print(f"分析失败 {task['path']}: {str(result)}")
        else:
            print(f"{task['path']} 在 {task['time']}秒 的 {task['freq']}Hz 振幅: {result:.4f}")


if __name__ == "__main__":
    # # 创建测试任务列表
    # analysis_tasks = [
    #     {"path": "黄昏.mp3", "freq": 1000, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1100, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1200, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1300, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1400, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1500, "time": 5.0},
    #     {"path": "黄昏.mp3", "freq": 1600, "time": 5.0},
    #
    # ]
    #
    # # 运行异步事件循环
    # asyncio.run(batch_analysis(analysis_tasks))
    l = [
        # 20Hz-40Hz称为极低频
        20, 30, 40,
        # 40Hz-80Hz称为低频
        50, 60, 70, 80,
        # 80Hz-160Hz称为中低频
        100, 110, 120, 130, 140, 150, 160,
        # 160Hz-1280Hz称为中频
        200, 220, 240, 260, 280,
        300, 320, 340, 360, 380,
        400, 420, 440, 460, 480,
        500, 520, 540, 560, 580,
        600, 620, 640, 660, 680,
        700, 720, 740, 760, 780,
        800, 820, 840, 860, 880,
        900, 920, 940, 960, 980,
        1000, 1020, 1040, 1060, 1080,
        1100, 1120, 1140, 1160, 1180,
        1200, 1220, 1240, 1260, 1280
    ]

    print(len(l))
